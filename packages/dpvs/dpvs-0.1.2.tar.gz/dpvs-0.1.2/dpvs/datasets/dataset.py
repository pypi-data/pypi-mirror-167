import numpy as np
from torch.utils.data import Dataset
from .utils import xpad

__all__ = ['DPvSDataset', 'BatchCollator']


class DPvSDataset(Dataset):

    def __init__(self, samples, sensor_obs_d, demo_info_d, label_mode=None, seq_test=True):
        """
        a dataset holder for training models 
        solving the classification task of Depression Prediction via Sensor data (DPvS) 
        samples:       given by utils.TaskDataSet.gen_data(...)
        sensor_obs_d:  given by utils.TaskDataSet.sensor_obs_d
        demo_info_d:    the dictionary that maps each patient from her id to her encoded demographic info
        seq_test:      whether the sequence of historical tests is provided
          for each patient-survey observation, the instance is provided as
          + seq_test=True:  (test1, test2, ...), label
          + seq_test=False: (test1, label), (test2, label), ...
        """
        self.samples = samples
        self.sensor_obs_d = sensor_obs_d
        self.demo_info_d = demo_info_d
        self.label_mode = label_mode
        self.seq_test = seq_test
                
    def __getitem__(self, i):
        sample_d = self.samples[i].copy()
        p_id = sample_d['ps_id'].split('|')[0] # patient id
        sample_d['demo'] = self.demo_info_d[p_id].values
        tids = sample_d['test_id_l']
        if not self.seq_test: 
            tids = [tids]
        else:
            tids = tids.tolist()
        sample_d['test_id_l'] = tids
        # here, the "seq" prefix means the sequence of sensor reads 
        # for a particular walking test record
        sample_d['seq_data_l'] = [self.sensor_obs_d[tid][0] for tid in tids]
        sample_d['seq_seg_l'] = [self.sensor_obs_d[tid][1] for tid in tids]
        sample_d['seq_len_l'] = [self.sensor_obs_d[tid][1].shape[0] for tid in tids]
        sample_d['n_seq'] = len(sample_d['seq_len_l'])
        return sample_d
    
    def __len__(self):
        return len(self.samples)
    
    @property
    def seq_len_all(self):
        return np.array([self[i]['n_seq'] for i in range(len(self))])
    
    @property
    def y(self):
        return np.array([sample_d['y'] for sample_d in self.samples])
    
    @property
    def y_ratio(self):
        return self.y.mean()
    
    def baseline_performance(self, score_fun_d, major_class):
        y_l = self.y
        y_pred_l = np.full(len(y_l), fill_value=major_class)
        result_d = {'major_class': major_class}
        for name, fun in score_fun_d.items():
            # if name in ['roc']:
            #     continue
            score = fun(y_l, y_pred_l)
            result_d[name] = round(score, 4)
        result_d['size'] = len(self)
        return result_d
    
    
class BatchCollator():
    
    FIELDS = [
        'seq_data_bh', 'seq_seg_bh', 'demo_bh', 
        'seq_len_bh', 'test_id_bh',
        'y', 'ps_id', 'n_seq_bh']
    
    def __init__(self, feature_dim=10, demo_dim=88, seq_test=True, max_seqlen=300):
        self.seq_test = seq_test
        self.feature_dim = feature_dim
        self.demo_dim = demo_dim
        self.max_seqlen = max_seqlen

    @staticmethod
    def time2int(ts: list, scale: float = 5):
        """ convert list of time to list of float (offset days since first task)
        
        the global average day difference is 4.9182 days (in training set) in between current task and the 1st task this subject has finished. the max value after transformation is 2.8 in the training set
        """
        def f(x, y):
            return (x.astype('datetime64[D]')-y.astype('datetime64[D]'))/np.timedelta64(scale, 'D')
        ts = np.array([f(x,ts[0]) for x in ts])
        return ts
    
    @staticmethod
    def seg2array(seq_seg_l:list, seq_data_l: list):
        """ split aggregated walking-test signals into seperates
        
        some basic statsitics about valid-length to different parts 
                outbound       return        rest
        mean         191          170         297
        min           60           29         267
        max          311          312         315      
        var         4505         4412         112
        """
        def gen():
            for seg, data in zip(seq_seg_l, seq_data_l):
                idx, cnt = np.unique(seg, return_counts=True)
                cnt_all = np.zeros(4, dtype=int)
                cnt_all[idx] = cnt
                split = np.split(data, np.cumsum(cnt_all)[1:-1])
                yield split, cnt_all[1:]
        return zip(*gen())


    def __call__(self, samples):
        """make a batch of the following data

        Notation:
            :symbol B:      batch size
            :symbol sL:     sequence length
            :symbol tL:     task length
            :symbol kL:     fixed value (3), the number of walking tests type
            :symbol fL:     feature length

        Return:
            :attr seq_data_bh: [B, tL, kL, sL, fL]
            :attr seq_len_bh:  [B, tL, kL]
            :attr task_len_bh: [B]
            :attr test_t_l  :  [B, tL]   the relative (to first task) timestamp to engage in a task
        """
        def gen():
            for s in samples:
                yield s['y'], s['ps_id'], s['demo'], self.time2int(s['test_t_l']), *self.seg2array(s['seq_seg_l'], s['seq_data_l']), len(s['test_t_l']), np.array(s['test_id_l'])

        y, ps_id, demo_bh, test_t_l, seq_data_bh, seq_len_bh, task_len_bh, test_id_bh = zip(*gen())
        max_tL, batch_size = max(task_len_bh), len(test_t_l)
        seq_len_bh = np.array([xpad(x, max_tL, 3, dtype=int) for x in seq_len_bh])
        batch_d = {
            'y': np.array(y, dtype=float), 
            'ps_id': np.array(ps_id, dtype=str),
            'test_id_bh': xpad(test_id_bh, batch_size, max_tL, dtype=test_id_bh[0].dtype, pad_value=''),
            'demo_bh': np.array(demo_bh, dtype=int),
            'task_len_bh': np.array(task_len_bh),
            'test_t_l': xpad(test_t_l, batch_size, max_tL),
            'seq_len_bh': seq_len_bh.clip(None, self.max_seqlen),
            'seq_data_bh': np.array([xpad(x, max_tL, 3, self.max_seqlen, 10) for x in seq_data_bh]),
        }
        return batch_d, batch_d.pop('y')
    
