# LibriTTS

## Install deps
```
pip install librosa==0.8.1
```

## Prepare Dataset
```
cd egs/libritts

# Those stages are very time-consuming
bash prepare.sh --stage -1 --stop-stage 3
```
#### data

```
##  train
Cut statistics:
╒═══════════════════════════╤═══════════╕
│ Cuts count:               │ 354780    │
├───────────────────────────┼───────────┤
│ Total duration (hh:mm:ss) │ 555:09:48 │
├───────────────────────────┼───────────┤
│ mean                      │ 5.6       │
├───────────────────────────┼───────────┤
│ std                       │ 4.5       │
├───────────────────────────┼───────────┤
│ min                       │ 0.1       │
├───────────────────────────┼───────────┤
│ 25%                       │ 2.3       │
├───────────────────────────┼───────────┤
│ 50%                       │ 4.3       │
├───────────────────────────┼───────────┤
│ 75%                       │ 7.6       │
├───────────────────────────┼───────────┤
│ 80%                       │ 8.7       │
├───────────────────────────┼───────────┤
│ 85%                       │ 10.0      │
├───────────────────────────┼───────────┤
│ 90%                       │ 11.8      │
├───────────────────────────┼───────────┤
│ 95%                       │ 14.8      │
├───────────────────────────┼───────────┤
│ 99%                       │ 20.9      │
├───────────────────────────┼───────────┤
│ 99.5%                     │ 23.1      │
├───────────────────────────┼───────────┤
│ 99.9%                     │ 27.4      │
├───────────────────────────┼───────────┤
│ max                       │ 43.9      │
├───────────────────────────┼───────────┤
│ Recordings available:     │ 354780    │
├───────────────────────────┼───────────┤
│ Features available:       │ 354780    │
├───────────────────────────┼───────────┤
│ Supervisions available:   │ 354780    │
╘═══════════════════════════╧═══════════╛
SUPERVISION custom fields:
Speech duration statistics:
╒══════════════════════════════╤═══════════╤══════════════════════╕
│ Total speech duration        │ 555:09:48 │ 100.00% of recording │
├──────────────────────────────┼───────────┼──────────────────────┤
│ Total speaking time duration │ 555:09:48 │ 100.00% of recording │
├──────────────────────────────┼───────────┼──────────────────────┤
│ Total silence duration       │ 00:00:01  │ 0.00% of recording   │
╘══════════════════════════════╧═══════════╧══════════════════════╛
```

## Training & Inference
refer to [Training](../../README.md##Training&Inference)