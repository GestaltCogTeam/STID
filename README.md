# Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting

Code for our paper Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting.
Our code is built on [BasicTS](https://github.com/zezhishao/BasicTS), an open-source standard time series forecasting benchmark.


<img src="figures/STID_architecture.png" alt="model archtecture" style="zoom:80%;" />

## 1. Data Preparation

### 1.1 Download Data

Download data from anonymous link [Google Drive](https://drive.google.com/file/d/1Ox2uOQmGtYH_PZqlfd9dyfCXi6eqGc89/view?usp=sharing) or [Baidu Yun](https://pan.baidu.com/s/1yIwDwN2m50LdeCHIdCCkCA?pwd=dt96) to the code root directory.

Then, unzip data by:

```bash
unzip raw_data.zip -d datasets
rm *.zip
```

### 1.2 Process Data

```bash
python scripts/data_preparation/${DATASET_NAME}/generate_training_data.py
```

Replace `${DATASET_NAME}` with one of `PEMS04`, `PEMS07`, `PEMS08`, and `Electricity336`.

The processed data is placed in `datasets/$DATASET_NAME`.

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run STID

```bash
python basicts/run.py --cfg basicts/options/STID/STID_${DATASET_NAME}.py --gpus '0'
```

Replace `${DATASET_NAME}` with one of `PEMS04`, `PEMS07`, `PEMS08`, and `Electricity336`.

## 4. Experiment Results

<img src="figures/main_results.png" alt="main results" style="zoom:100%;" />

<img src="figures/visualizations.png" alt="visualizations" style="zoom:100%;" />

<img src="figures/efficiency_and_ablation.png" alt="efficiency and ablation" style="zoom:100%;" />
