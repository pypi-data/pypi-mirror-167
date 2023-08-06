from ..utils import pickle_load
from .dataset import DPvSDataset, BatchCollator
from .walk_ds import WalkTestDataSet
from .utils import Dataloaders, DataLoader, Datasets
from pathlib import Path
import numpy as np
from numpy import linalg as LA
from scipy.signal import find_peaks

np.seterr(invalid='raise')


def make_data(label_mode, data_dir, part_seed, train_split, sample_rate, nw,add_world_frame, use_cache):
    data_dir = Path(data_dir)
    def get_dataset(mode='train'):
        return DPvSDataset(
            walk_ds.gen_samples(mode, mode=label_mode, keep_last=True), 
            walk_ds.sensor_obs_d, 
            user_demo_wide_d, 
            label_mode=label_mode,
            seq_test=(label_mode=='label_seq')
        )
    demo_d = pickle_load(data_dir/"demo_data_wide.pkl")
    user_demo_wide_d = demo_d['user_demo_wide']
    walk_ds = WalkTestDataSet(
        data_dir/f"analysis_final_df_{nw}weeks.pkl", 
        data_dir/f"demograph_df.pkl",
        data_dir/'walking_test_data.h5', 
        seed=part_seed, partition=train_split, ts_segs=[],
        load_sensor_data=True, sample_rate=sample_rate, add_world_frame=add_world_frame, use_cache=use_cache
    )
    demo_dim = user_demo_wide_d[walk_ds.demo_df.index[0]].shape[0]
    data = Datasets(
        train = get_dataset('train'),
        val = get_dataset('valid'),
        test = get_dataset('test'),
    )
    # check_score(train=data.train, valid=data.val, test=data.test)
    return data
    
    

def make_tensor(label_mode, data_dir, part_seed, train_split, sample_rate, nw, add_world_frame, use_cache, train_sz=32, test_sz=128, demo_dim=88, **kwargs):
    data = make_data(label_mode, data_dir, part_seed, train_split, sample_rate, nw, add_world_frame, use_cache)
    collate_fn = BatchCollator(
        feature_dim=walk_ds.feature_dim, demo_dim=demo_dim, seq_test=label_mode=='label_seq'
    )
    return Dataloaders(
        train=DataLoader(data.trian, batch_size=train_sz, shuffle=True, collate_fn=collate_fn),
        val=DataLoader(data.val, batch_size=test_sz, shuffle=False, collate_fn=collate_fn),
        test=DataLoader(data.test, batch_size=test_sz, shuffle=False, collate_fn=collate_fn),
    )



def make_numpy(label_mode, data_dir, part_seed, train_split, sample_rate, nw, add_world_frame, use_cache, **kwargs):
    """
    :feature:
    'x_useraccel', 'y_useraccel', 'z_useraccel', 'x_attitude', 'y_attitude', 'z_attitude', 'w_attitude'

    :mode:
    'outbound', 'return', 'rest'
    """
    datasets: Datasets = make_data(label_mode, data_dir, part_seed, train_split, sample_rate, nw, add_world_frame, use_cache,)
    scale = 1/sample_rate
    def process(data):
        for d in data:
            d_val, d_len = BatchCollator.seg2array(d['seq_seg_l'],d['seq_data_l'])
            d_target = d['y']
            try:
                mean_axis = np.stack([np.mean(x, axis=0) for x in d_val[0]]) #3x7
                std_axis  = np.stack([np.std(x, axis=0) for x in d_val[0]])  #3x7
                raw_magtude = [LA.norm(x, axis=1) for sub in d_val[0] for x in np.split(sub, [4], axis=1)]
                mean_axis_mag = np.stack([np.mean(x) for x in raw_magtude]).reshape(3,2)   
                std_axis_mag = np.stack([np.std(x) for x in raw_magtude]).reshape(3,2)     
                jerk = [np.diff(x, axis=1) for x in d_val[0]]
                mean_jerk = np.stack([np.mean(x, axis=0) for x in jerk])     #3x7
                std_jerk = np.stack([np.std(x, axis=0) for x in jerk])       #3x7
                jerk_magtude = [LA.norm(x, axis=1) for sub in jerk for x in np.split(sub, [4], axis=1)]
                mean_jerk_mag = np.stack([np.mean(x) for x in jerk_magtude]).reshape(3,2)
                std_jerk_mag = np.stack([np.std(x) for x in jerk_magtude]).reshape(3,2)
                axis_mag_all = [np.column_stack(
                    [x, *raw_magtude[2*i:2*(i+1)]]) for i,x in enumerate(d_val[0])]
                stride = [np.diff(
                    find_peaks(x, distance=15)[0])*scale for sub in axis_mag_all for x in sub.transpose()]   # 9x3
                var_stride = np.stack([np.std(x) for x in stride]).reshape(9,3).transpose() 
            except FloatingPointError:
                continue
            yield np.column_stack([
                mean_axis,std_axis,mean_axis_mag,std_axis_mag,mean_jerk,std_jerk,mean_jerk_mag,std_jerk_mag,var_stride  # (3,43)
            ]).reshape(-1), d_target
    datasets.apply(process)
    return datasets


