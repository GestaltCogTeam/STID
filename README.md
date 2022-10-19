# Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting

Code for our CIKM'22 short paper: "[Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting](https://arxiv.org/abs/2208.05233)".

Our code is built on [BasicTS](https://github.com/zezhishao/BasicTS), an open-source standard time series forecasting benchmark. You can also find STID in [BasicTS](https://github.com/zezhishao/BasicTS).

<img src="figures/STID_architecture.png" alt="model archtecture" style="zoom:80%;" />

> Multivariate Time Series (MTS) forecasting plays a vital role in a wide range of applications. Recently, Spatial-Temporal Graph Neural Networks (STGNNs) have become increasingly popular MTS forecasting methods due to their state-of-the-art performance. However, recent STGNN-based methods are becoming more sophisticated with limited performance improvements. This phenomenon motivates us to explore the critical factors of MTS forecasting and design a model that is as powerful as STGNNs, but more concise and efficient. In this paper, we identify the indistinguishability of samples in both spatial and temporal dimensions as a key bottleneck, and propose a simple yet effective baseline for MTS forecasting by attaching Spatial and Temporal IDentity information (STID). STID achieves the best performance and efficiency simultaneously based on simple multi-layer perceptrons (MLPs). These results suggest that by solving the indistinguishability of samples, we can design models more freely, without being limited to STGNNs.

## 1. Table of Contents

```python
File Directory:
Data Preprocess     : scripts/data_preparation/${DATASET_NAME}/generate_training_data.py
Model Architecture  : basicts/archs/STID/STID_arch.py
Training Runner     : basicts/runner/STID_runner.py
Training Configs    : basicts/options/STID/STID_${DATASET_NAME}.py
```

Replace `${DATASET_NAME}` with one of `PEMS04`, `PEMS07`, `PEMS08`, and `Electricity336`.

## 2. Requirements

```bash
pip install -r requirements.txt
```

## 3. Data Preparation

### 3.1 Download Data

Download data from anonymous link [Google Drive](https://drive.google.com/file/d/1Ox2uOQmGtYH_PZqlfd9dyfCXi6eqGc89/view?usp=sharing) or [Baidu Yun](https://pan.baidu.com/s/1yIwDwN2m50LdeCHIdCCkCA?pwd=dt96) to the code root directory.

Then, unzip data by:

```bash
unzip raw_data.zip -d datasets
rm *.zip
```

### 3.2 Data Preprocessing

```bash
python scripts/data_preparation/${DATASET_NAME}/generate_training_data.py
```

Replace `${DATASET_NAME}` with one of `PEMS04`, `PEMS07`, `PEMS08`, and `Electricity336`.

The processed data is placed in `datasets/$DATASET_NAME`.

## 4. Run STID

```bash
python basicts/run.py --cfg basicts/options/STID/STID_${DATASET_NAME}.py --gpus '0'
```

Replace `${DATASET_NAME}` with one of `PEMS04`, `PEMS07`, `PEMS08`, and `Electricity336`.

## 5. Experiment Results

<img src="figures/main_results.png" alt="main results" style="zoom:100%;" />

<img src="figures/visualizations.png" alt="visualizations" style="zoom:100%;" />

<img src="figures/efficiency_and_ablation.png" alt="efficiency and ablation" style="zoom:100%;" />

## 6. Citing

```bibtex
@inproceedings{10.1145/3511808.3557702,
author = {Shao, Zezhi and Zhang, Zhao and Wang, Fei and Wei, Wei and Xu, Yongjun},
title = {Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting},
year = {2022},
booktitle = {Proceedings of the 31st ACM International Conference on Information & Knowledge Management},
pages = {4454–4458},
location = {Atlanta, GA, USA}
}

```

## 7. More Related Works

- [D2STGNN: Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting. VLDB'22.](https://github.com/zezhishao/D2STGNN)

- [STEP: Pre-training-Enhanced Spatial-Temporal Graph Neural Network For Multivariate Time Series Forecasting. KDD'22.](https://github.com/zezhishao/STEP)

- [BasicTS: An Open Source Standard Time Series Forecasting Benchmark.](https://github.com/zezhishao/BasicTS)
