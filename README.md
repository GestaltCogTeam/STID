# Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting

🔥 ***[New Results] We added the performance of STID on large scale MTS datasets.***


Code for our CIKM'22 short paper: "[Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting](https://arxiv.org/abs/2208.05233)".

> [!IMPORTANT]  
> STID is built on [BasicTS](https://github.com/zezhishao/BasicTS), an open-source standard time series forecasting benchmark. 
> **We highly recommend you to reproduce STID and any other MTS forecasting models on any dataset using [BasicTS](https://github.com/zezhishao/BasicTS).**
> This repo will not be updated frequently, and we will update the code in [BasicTS](https://github.com/zezhishao/BasicTS)

<img src="figures/STID_architecture.png" alt="model archtecture" style="zoom:80%;" />

> [!NOTE]  
> Multivariate Time Series (MTS) forecasting plays a vital role in a wide range of applications. Recently, Spatial-Temporal Graph Neural Networks (STGNNs) have become increasingly popular MTS forecasting methods due to their state-of-the-art performance. However, recent STGNN-based methods are becoming more sophisticated with limited performance improvements. This phenomenon motivates us to explore the critical factors of MTS forecasting and design a model that is as powerful as STGNNs, but more concise and efficient. In this paper, we identify the indistinguishability of samples in both spatial and temporal dimensions as a key bottleneck, and propose a simple yet effective baseline for MTS forecasting by attaching Spatial and Temporal IDentity information (STID). STID achieves the best performance and efficiency simultaneously based on simple multi-layer perceptrons (MLPs). These results suggest that by solving the indistinguishability of samples, we can design models more freely, without being limited to STGNNs.

## 📚 Table of Contents

```text
basicts   --> The BasicTS, which provides standard pipelines for training MTS forecasting models. Don't worry if you don't know it, because it doesn't prevent you from understanding STID's code.

datasets  --> Raw datasets and preprocessed data

experiments  --> Training scripts.

figures   --> Some figures used in README.

scripts   --> Data preprocessing scripts.

stid/arch      --> The implementation of STID.

stid/${DATASET_NAME}.py    --> Training configs.
```

Replace `${DATASET_NAME}` with one of `PEMS03`, `PEMS04`, `PEMS07`, `PEMS08`, `METR-LA`, `PEMS-BAY`, or any other dataset you want to use.

## 💿Requirements

The code is built with BasicTS, you can easily install the requirements by (take Python 3.11 + PyTorch 2.3.1 + CUDA 12.1 as an example):

```bash
# Install Python
conda create -n BasicTS python=3.11
conda activate BasicTS
# Install PyTorch
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121
# Install other dependencies
pip install -r requirements.txt
```

More details can be found in [BasicTS](https://github.com/GestaltCogTeam/BasicTS).

## 📦 Data Preparation

### **Download Data**

You can download the `all_data.zip` file from [Google Drive](https://drive.google.com/drive/folders/14EJVODCU48fGK0FkyeVom_9lETh80Yjp?usp=sharing) or [Baidu Netdisk](https://pan.baidu.com/s/1shA2scuMdZHlx6pj35Dl7A?pwd=s2xe). Unzip the files to the `datasets/` directory:

```bash
cd /path/to/BasicTS
unzip /path/to/all_data.zip -d datasets/
mv datasets/all_data/* datasets/
rmdir datasets/all_data
```

These datasets have been preprocessed and are ready for use.

## 🎯 Train STID

```bash
python experiments/train.py --cfg stid/${DATASET_NAME}.py --gpus '0'
```

Replace `${DATASET_NAME}` with one of `PEMS03`, `PEMS04`, `PEMS07`, `PEMS08`, `METR-LA`, `PEMS-BAY`, or any other dataset you want to use.

```bash
python experiments/train.py --cfg stid/PEMS04.py --gpus '0'
```

## 📈 Experiment Results

<img src="figures/main_results.png" alt="main results" style="zoom:100%;" />

<img src="figures/perf_large_mts.png" alt="main results" style="zoom:100%;" />

<img src="figures/visualizations.png" alt="visualizations" style="zoom:100%;" />

<img src="figures/efficiency_and_ablation.png" alt="efficiency and ablation" style="zoom:100%;" />

## 🔗 More Related Works

- [D2STGNN: Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting. VLDB'22.](https://github.com/zezhishao/D2STGNN)

- [STEP: Pre-training-Enhanced Spatial-Temporal Graph Neural Network For Multivariate Time Series Forecasting. KDD'22.](https://github.com/zezhishao/STEP)

- [BasicTS: A Fair and Scalable Time Series Forecasting Benchmark and Toolkit.](https://github.com/zezhishao/BasicTS)

## Citing

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
