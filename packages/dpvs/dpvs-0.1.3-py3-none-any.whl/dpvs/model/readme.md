Here are a list of torch/sklearn models available to use

### Hpnet

```yaml
# from configs/model/hpnet.yaml
_target_: dpvs.model.hpnet.HierarchicalProtoNetCLS
flayer: 
  _target_: dpvs.model.hpnet.FeatureNet
  backbone: cnn_wide
slayer: {
    _target_: dpvs.model.hpnet.SymptomNet,
    _partial_: true,
    n_proto: 5,
    rd: 1.0, re: 0.1, rc: 0.1, rs: 0.1, d_min: 2.0
  }
tlayer: {
    _target_: dpvs.model.hpnet.TrendGenerative,
    _partial_: true,
    n_proto: 5,
    time_dim: 8, t0: null, beta: 0, rd: 1.0, re: 0.1, rc: 0.1, rt: 0.1, d_min: 1.0
  }
```
```python
class HierarchicalProtoNetCLS(nn.Module):

    def __init__(
        self, flayer, slayer, tlayer, normalize=False, pos_weight=1.0
    ):
    super(HierarchicalProtoNetCLS, self).__init__()
    self.flayer = flayer
    self.slayer = slayer(in_dim=self.flayer.out_dim) # see _partial_:true in slayer
    self.tlayer = tlayer(in_dim=self.slayer.out_dim) # see _partial_:true in tlayer
    ...

    def forward(
        self, seq_data_bh, seq_len_bh, test_t_l, task_len_bh, demo_bh, ps_id, test_id_bh, **kwargs
    ):
        """process one batch of data (see make_tensor in datasets for batch info)
        
        :input seq_data_bh:     (batch-size, task-dim, 3, sequence-dim, feature-dim)
        :input seq_len_bh:      (batch-size, task-dim, 3)
        :input task_len_bh:     (batch-size)
        :input test_t_l  :      (batch-size, task-dim)

        :flayer embedding:      (pack-ntask, 3x5, out-dim)  (3xseq-dim) => (3x5) hid
        :flayer seq_len:        xpack object (used to unpack ntask)

        :slayer s_itm:          (batch-size, task-dim, n-symptom)
        :slayer pos:    (batch-size, taskdim), the most similar patch in (3x5) hidden

        :tlayer logits:         (batch-size), predicted logits of instance
        """
        embedding, seq_len = self.flayer(
            seq_data_bh, demo_bh, seq_len_bh, task_len_bh
        )
        if self.normalize: 
            embedding = normalize(embedding)
        s_itm, pos = self.slayer(embedding)
        s_itm, pos = seq_len.pad(s_itm), seq_len.pad(pos)  # pack-all-task -> patient-task
        logits = self.tlayer(s_itm, test_t_l, task_len_bh, demo_bh)
        self.xpack = seq_len     
        return logits
```
