conda create -n anomaly_detection python=3.11 -y
onda activate anomaly_detection
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0  pytorch-cuda=11.8 -c pytorch -c nvidia -y
pip install -r requirements.txt