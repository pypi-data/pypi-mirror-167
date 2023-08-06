import pickle
import numpy as np
import pandas as pd
from joblib import Parallel, delayed, effective_n_jobs
from sklearn.model_selection  import train_test_split

__all__ = ['WalkTestDataSet']

class WalkTestDataSet():

    features = [
        'x_useraccel', 'y_useraccel', 'z_useraccel', 
        'x_attitude', 'y_attitude', 'z_attitude', 'w_attitude']
    
    # code 0 is reversed for padding
    seg_code2str = pd.Series(data=['outbound', 'return', 'rest'], index=[1, 2, 3])
    
    def __init__(self, meta_df_fp, demo_df_fp, data_fp, dp_theta=4,
            seed=42, partition={'train': 0.8, 'test': 0.2}, ts_segs=['test'],
            load_sensor_data=True, sample_rate=10, min_len=10, 
            add_world_frame=True, use_cache=True):
        """
        To be used with the data files produced by `datasteps.ipynb`
        
        An instance of this class holds patient-survey observations with depression labels, 
         and historical walking test sensor data that can be used for depression prediction.
        
        Args:
            meta_df_fp: see `datasteps.ipynb`
            demo_df_fp: see `datasteps.ipynb`
            data_fp: see `datasteps.ipynb`
            
            dp_theta: the threshold for defining depression labels
            
            seed (int, optional): Defaults to 42.
              random seed used for dataset partition
            
            partition (dict, optional): Defaults to {'train': 0.8, 'test': 0.2}.
              see the docstr of instance method `split_to_segments`
              
            ts_segs: Defaults to ['test'].
              see the docstr of instance method `split_to_segments`
              
            load_sensor_data (bool, optional): Defaults to True.
              whether the instance attribute "sensor_obs_d" storing sensor data should be created
              see the docstring of instance method `load_sensor_data`
              
            sample_rate (int, optional): Defaults to 10.
            min_len (int, optional): Defaults to 10
            add_world_frame (bool, optional): Defaults to True.
            use_cache (bool, optional): Defaults to True.
              see the docstring of instance method `load_sensor_data`
        """
        # the dataframe of patient-survey (p-s) observations
        meta_df = pd.read_pickle(meta_df_fp)

        # the dataframe of p-s level meta information
        usecols = ['depression_score', 
                   'medTimepoint', 'healthCode', 'survey_id', 
                   't_demo', 't_survey', 'delta_t_to_survey']
        ps_obs_df = meta_df.groupby('healthCodeExt', as_index=True)[usecols].first()
        # define the depression label for each p-s obs
        ps_obs_df['depress'] = (ps_obs_df['depression_score'] >= dp_theta).astype(int)
        self.dp_theta = dp_theta
        # sort p-s obs by their labeling time (survey time) from past to recent
        self.ps_obs_df = ps_obs_df.sort_values('t_survey', ascending=True)
        
        # dataset partition
        self.set_rng(seed)
        self.split_into_segments(partition, ts_segs)
        
        # the dataframe mapping each p-s obs to its historical test observations
        # only record when which test occurred
        self.meta_df = meta_df[['healthCodeExt', 'test_id', 't_test']].sort_values(
            ['healthCodeExt', 't_test'], ascending=True).reset_index(drop=True)
        self.meta_df['t_test_day'] = self.meta_df['t_test'].dt.strftime("%Y%m%d")
        self.test_id_l = self.meta_df['test_id'].unique()
        # load per test sensor data by creating the instance attribute `self.sensor_obs_d`
        # which is a dictionary of which keys are linked with the "test_id" column of `self.meta_df`
        self.meta_df_fp = meta_df_fp
        self.data_fp = data_fp
        if load_sensor_data:
            self.load_sensor_data(sample_rate, min_len, add_world_frame, use_cache)
                
        # load patients' demographic data
        demo_df = pd.read_pickle(demo_df_fp)
        self.demo_df = demo_df
    
    def process_one_record(self, record_id):
        '''
        intended to be called internally by self.load_sensor_data
        '''
        store = pd.HDFStore(self.data_fp, mode='r')
        sensor_df = store[f"/walk/{record_id}"][::self.sample_rate].reset_index(drop=True)
        store.close()
        if sensor_df.shape[0] <= self.min_len:
            result = (record_id, None)
        else:
            sensor_data = sensor_df[self.features].values # [n_time_step, 7]
            if self.add_world_frame:
                # `acc_v_hat` is of shape [n_time_step, 3]
                acc_v_hat = self.acc_v_phone2world(sensor_df)
                sensor_data = np.hstack((acc_v_hat, sensor_data))
            segcodes = sensor_df['segment'].values
            result = (record_id, (sensor_data, segcodes))
        return result
    
    @staticmethod
    def acc_v_phone2world(sensor_df):
        '''
        intended to be called internally by self.process_one_record
        convert the acceleration vector measured with phone's frame to the world's frame 
        see `datasteps.ipynb`
        '''
        # `acc_v` is of shape [n_time_step, 3] then expanded to [n_time_step, 3, 1]
        acc_v = sensor_df[[f"{k}_useraccel" for k in ['x', 'y', 'z']]].values[:, :, None]
        # each value in `ad` is of shape [n_time_step,], ad means the dictionary of attitude values
        ad = {k: sensor_df[f"{k}_attitude"].values for k in ['x', 'y', 'z', 'w']}
        # `R` is of shape [3, 3, n_time_step] then transposed to [n_time_step, 3, 3]
        R = np.array([
            [ad['w']**2+ad['x']**2-ad['y']**2-ad['z']**2, 
            2*ad['x']*ad['y']-2*ad['w']*ad['z'],  
            2*ad['x']*ad['z']+2*ad['w']*ad['y']],
            [2*ad['x']*ad['y']+2*ad['w']*ad['z'],         
            ad['w']**2-ad['x']**2+ad['y']**2-ad['z']**2, 
            2*ad['y']*ad['z']-2*ad['w']*ad['x']],
            [2*ad['x']*ad['z']-2*ad['w']*ad['y'],         
            2*ad['y']*ad['z']+2*ad['w']*ad['x'],         
            ad['w']**2-ad['x']**2-ad['y']**2+ad['z']**2],
        ]).transpose(2, 0, 1)
        # `acc_v_hat` is of shape [n_time_step, 3, 1] then squeezed to [n_time_step, 3]
        acc_v_hat = (R @ acc_v).squeeze(-1)
        return acc_v_hat
    
    def __getitem__(self, i):
        store = pd.HDFStore(self.data_fp, mode='r')
        rid = self.test_id_l[i]
        sensor_df = store[f"/walk/{rid}"]
        store.close()
        return rid, sensor_df
    
    def load_sensor_data(self, sample_rate, min_len, add_world_frame, use_cache):
        '''
        create instance attribute `self.sensor_obs_d`, which is a dictionary 
          containing the sensor data of walking tests, and is of structure
          {
              test_id: down_sampled_walk_data
            }
          where 
        
        + "test_id" is the unique id of the test record 
          (walking test is only one subtask, at most 4 subtasks could exists for a given unique test id)
        
        + "down_sampled_walk_data" is a tuple of structure (sensor_data, segment_codes)
          
          - "sensor_data" is a numpy array of shape [n_time_step, n_feature]
            1. "n_time_step" equals to original sensor sequence length divided by `sample_rate`
              (a sensor read is sampled every `sample_rate` time steps or 0.01 seconds)
            2. "n_feature" is 7 when `add_world_frame` is False,
               namely, 
               ['x_useraccel', 'y_useraccel', 'z_useraccel', 
                'x_attitude', 'y_attitude', 'z_attitude', 'w_attitude']
               
               "n_feature" is 10 when `add_world_frame` is True
               namely, 
               ['x_useraccel_world', 'y_useraccel_world', 'z_useraccel_world', 
                'x_useraccel', 'y_useraccel', 'z_useraccel', 
                'x_attitude', 'y_attitude', 'z_attitude', 'w_attitude']
                
          - "segment_codes" is a numpy array of shape [n_time_step, ]
          
        use_cache: determines whether "self.sensor_obs_d" 
          should be computed on the fly (use_cache=False) 
          or loaded from the saved cache if exists (use_cache=True)
        '''
        self.sample_rate = sample_rate
        self.min_len = min_len
        self.add_world_frame = add_world_frame
        suffix = str(self.meta_df_fp).split('.pkl')[0].split('_')[-1]
        cache_fp = f"cache_wtd_sr{sample_rate}_ml{min_len}_awf{add_world_frame}_{suffix}.pkl"
        cache_fp = self.meta_df_fp.parent/cache_fp
        self.cache_fp = cache_fp
        if (not use_cache) or (not cache_fp.is_file()):
            # create on the fly
            print('... collecting sensor data ...')
            res = Parallel(n_jobs=effective_n_jobs())(
                delayed(self.process_one_record)(test_id) 
                for test_id in self.test_id_l)
            self.sensor_obs_d = {
                test_id: sensor_data 
                for test_id, sensor_data in res 
                if sensor_data is not None}
            with open(cache_fp, 'wb') as f:
                pickle.dump(self.sensor_obs_d, f)
            print(f"... cache created at {cache_fp} ...")
        else:
            # load cached version
            with open(cache_fp, 'rb') as f:
                self.sensor_obs_d = pickle.load(f)
            print(f"... cache loaded from {cache_fp} ...")
        # the feature dimension of walking test sensor data
        self.feature_dim = len(self.features)
        if add_world_frame:
            self.feature_dim += 3
    
    def set_rng(self, seed):
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        
    def split_into_segments(self, partition, ts_segs):
        '''
        partition: the dataset partition plan, should be provided as a dictionary
          where keys are segment names and values are segment sizes (in percentage)
          must have keys 'train' and 'test'
          e.g., partition={'train': 0.8, 'test': 0.2}
          
        ts_segs: a list of segment names, determines which segments in `partition` should be
          splitted in a way sensitive to observation time.
          "ts_segs" is short for "time sensitive segments"
            
        The dataset of patient-survey (p-s) samples will be splitted into segments in the following way.
          
        1. Sort p-s samples by survey time in ascending order (from past to recent).
        2. For `m`=`len(ts_segs)-1`, `len(ts_segs)-2`, ..., `0` 
           + assign the tail `partition[ts_segs[m]]` percentage of samples to segment `ts_segs[m]`
           + based on the left samples, do the next round of iteration
        3. Laslty, randomly split the left samples into the left time-neural segments (those in `partition` but not in `ts_segs`)
        
        For example,
          `ts_segs=['test]` means the 'test' segment will always be comprised of
          those lastly observed patient-survey samples 
        '''
        for seg in ['train', 'test']:
            assert seg in partition
        for seg in ts_segs:
            assert seg in partition
        assert sum(partition.values()) == 1
        
        self.partition = partition.copy()
        self.ts_segs = ts_segs
        
        n = self.n_ps_obs
        # compute number of obs in each segment
        seg_size_d = {seg_name: int(n*seg_prop) for seg_name, seg_prop in partition.items()}
        # allocate left over samples to the train segment
        seg_size_d['train'] = seg_size_d['train'] + (n-sum(seg_size_d.values()))

        # do the partition by assigning segment tags 
        # to observations in `ps_obs_df`
        # start with the time sensitive segments
        n_left = n
        idx = self.ps_obs_df.index.values
        self.ps_obs_df['segment'] = pd.NA
        for seg_name in ts_segs[::-1]:
            start = n_left - seg_size_d.pop(seg_name)
            self.ps_obs_df.loc[idx[start:n_left], 'segment'] = seg_name
            n_left = start
        idx = idx[:n_left]
        y = self.ps_obs_df.loc[idx, 'depress']
        # deal with other segments
        # do stratified sampling
        for seg_name, seg_size in seg_size_d.items():
            if seg_size == n_left:
                # should be the last segment and the last iteration
                idx_assigned = idx
            else:
                idx, idx_assigned = train_test_split(
                    idx, test_size=seg_size, 
                    stratify=y.values, 
                    random_state=self.rng.integers(999))
            y = y.loc[idx]
            n_left -= seg_size
            self.ps_obs_df.loc[idx_assigned, 'segment'] = seg_name

    
    def get_segment_df(self, segment='train'):
        in_seg = self.ps_obs_df['segment'] == segment
        return self.ps_obs_df[in_seg]
    
    def gen_samples(self, segments='train', mode='label_seq', keep_last=False):
        '''
        mode: determines how to generate samples for each patient-survey (p-s) observation
          in the segment specified by argument `segment`
          
          by construction, each p-s obs has only one "y" (the depression label)
          but a sequence of "X_t" (the t-th walking test sensor data) 
          that is, [X_t|t=1,2,...,L], with L varying across p-s obs
          
          the sample generation strategy is then:
          mode='label_seq':  generate 1 sample for the entire sequence,
            that is, ([X_t|t=1,2,...,L], y)          
          mode='label_all':  generate L samples for each walking test, 
            that is, (X_t, y) for t=1,2,...,L
          mode='label_last': generate 1 sample for the last walking test, 
            that is, (X_L, y)
          
        keep_last: if True, then if a p-s obs is associated with more than one 
          historical test records in a day, only keep the last one
        '''
        assert mode in ['label_seq', 'label_all', 'label_last']
        assert hasattr(self, 'sensor_obs_d')
        if not isinstance(segments, list):
            segments = [segments]
        in_seg = self.ps_obs_df['segment'].isin(set(segments))
        ps_id_l = self.ps_obs_df.index.values[in_seg]
        # recall that `meta_pd` has been sorted by column `healthCodeExt` ascendingly
        grped = self.meta_df.groupby('healthCodeExt', sort=False)
        samples = []
        for ps_id in ps_id_l:
            sub_pd = grped.get_group(ps_id)
            # in case some test records do not 
            # have walking sensor data
            has_data = sub_pd['test_id'].isin(self.sensor_obs_d)
            sub_pd = sub_pd[has_data]
            if sub_pd.shape[0] == 0:
                continue
            self.sub_pd = sub_pd
            if keep_last:
                # recall that `meta_pd` has been sorted by column `t_test` ascendingly in every p-s group
                sub_pd = sub_pd.groupby('t_test_day', sort=False, as_index=False).last()
            y = self.ps_obs_df.loc[ps_id, 'depress']
            if mode == 'label_seq':
                samples.append({
                    'test_id_l': sub_pd['test_id'].values, 
                    'y': y, 
                    'ps_id': ps_id,
                    'test_t_l': sub_pd['t_test'].values})
            elif mode == 'label_all':
                samples.extend([
                    {'test_id_l': row['test_id'], 
                        'y': y, 'ps_id': ps_id, 
                        'test_t_l': row['t_test']}
                    for _, row in sub_pd.iterrows()])
            else: # label_last
                # the most recent test record before the survey
                # since `meta_pd` has been sorted by column `t_test` ascendingly in every p-s group
                # this amounts to select the last row in the group dataframe
                samples.append({
                    'test_id_l': sub_pd.iloc[-1]['test_id'],
                    'y': y, 'ps_id': ps_id, 
                    'test_t_l': sub_pd.iloc[-1]['t_test']})
        return samples
    
    @property
    def n_psm_obs(self):
        """
        number of patient-survey-test observations
        indexed by (p, s, m), meaning the m-th test record 
          in the sequence of historical test records 
          that will be used to predict the s-th survey of the p-th patient
        """
        return self.meta_df.shape[0]
     
    @property
    def n_p_obs(self):
        """
        number of patient observations
        """
        return self.demo_df.shape[0]
    
    @property
    def n_ps_obs(self):
        """
        number of patient-survey observations
        indexed by (p, s), meaning the s-th survey of the p-th patient
        """
        return self.ps_obs_df.shape[0]
    
    @property
    def split_time(self):
        """
        the day after which patient-survey observations
        will be treated as test instances
        """
        if self.time_sensitive:
            in_test = self.ps_obs_df['segment'] == 'test'
            row = self.ps_obs_df[in_test].iloc[0]
            return row['t_survey']
        else:
            return None