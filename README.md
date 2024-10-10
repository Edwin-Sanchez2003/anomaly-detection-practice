# Anomaly Detection Example

This repository contains code that exemplifies the process of performing anomaly detection using an example dataset, [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) (Please see [Acknowledgements](#acknowledgements) for more information on the dataset used).

## Index

- [Anomaly Detection Example](#anomaly-detection-example)
  - [Index](#index)
  - [Setup](#setup)
    - [Dataset](#dataset)
    - [Environment](#environment)
  - [Acknowledgements](#acknowledgements)

## Setup

### Dataset

1. Go to [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) OR [Kaggle CIC-IDS2017](https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset).
2. Follow the instructions to download the dataset.
3. Save the exported data to the following folder in the project directory: `./CIC-IDS2017/` (ex: `./anomaly-detection-practice/CIC-IDS2017/`).

### Environment

Feel free to change package versions as necessary.

1. `conda create -n anomaly_detection python=3.11 -y`
2. `conda activate anomaly_detection`
3. `conda install anaconda::ipykernel==6.29.5`
4. `conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0  pytorch-cuda=11.8 -c pytorch -c nvidia -y`
5. `pip install -r requirements.txt`

**OR** (Unix-based Operating Systems)

1. `bash install.sh`

## Acknowledgements

- **Dataset:** Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani, “Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”, 4th International Conference on Information Systems Security and Privacy (ICISSP), Purtogal, January 2018
- **ArcFace (Additive Angular Margin Loss):** J. Deng, J. Guo, J. Yang, N. Xue, I. Kotsia, and S. Zafeiriou, “ArcFace: Additive Angular Margin Loss for Deep Face Recognition,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 44, no. 10, pp. 5962–5979, Oct. 2022, doi: 10.1109/tpami.2021.3087709.
- **PyTorch Metric Learning (Loss Function Implementations & Other Tools)**
  - [GitHub](https://github.com/KevinMusgrave/pytorch-metric-learning)
  - [Documentation](https://kevinmusgrave.github.io/pytorch-metric-learning/)
