# 논문 구조



##### keyword 

- Data Augmentation for timeseries forecast
- CNN-Attention BiLSTM  hybrid model
- Interpretable timeseries using Grad-CAM





#### Introduction 

- 시계열 데이터에 대한 연구는 텍스트, 이미지에 비해 연구가 많이 이루어지지 않음.
- Data Augmentation의 경우도 classification 쪽으론 많이 쓰이지만 forecasting 쪽으론 쓰인 논문 찾지 못함.
- Grad-CAM을 이용해서 해석력을 추가.



#### Prior research 

1. Data Augmentation for time series
2. Grad-CAM
3. Interpretable lstm, 1dcnn ...



#### Data Description

1. bitcoin data
2. pm2.5 beijing data
3. nasdaq data (?)



#### Experiment

1. Interpretable forecasting model using Grad-CAM

-> 성능은 평범하지만 시각화로 해석력을 추가

2. Good performance Model (CNN-Attention BiLSTM with Data Augmentation)

-> multi-input Model이 기존 논문보다 좋은 성능을 이끌었지만 Grad-CAM이 안되는 문제가 있음



#### conclusion

#### Future work

