# 논문 구조



###### keyword 

- CNN-LSTM hybrid model (CNN-LSTM, LSTM-CNN, LSTM-resCNN)  
- Interpretable model using Grad-CAM





### Introduction 

(이부분은 효정학생 논문 Intro 앞부분 괜찮은 것 같아요.)  
(효정학생 논문 초안에서 Grad-CAM을 이용해서 해석력을 추가 부분 정도 기여한 부분에 더 넣으면 좋을 것 같아요)

### Prior research 
1. CNN-LSTM  
2. Grad-CAM  
3. Interpretable timeseries forecasting model ...  

### Proposed Model

(이 부분 효정학생의 3.모델 제안 부분쪽 쓰면 좋을 것 같아요)

### Experiments

#### Data Description

1. bitcoin data  
2. pm2.5 beijing data  
3. SeoulBike data  

#### Experimental Setup 

각 데이터 별로 어떻게 트레이닝이 되었는지, train, valid, test 어떤 식으로 잡았는지, 어떤 모형들이 실험되었는지, 어떤 컴퓨터를 사용했는지, 등등 셋업 부분 언급

#### Experimental Resluts

각 데이터 별로 모형들의 성능 비교 (모형들: CNN-LSTM, LSTM-CNN, LSTM-resCNN Architecture )

1. one-step prediction  

  1.1 RMSE, MAE Table  
  1.2 prediction graph  

2. multi-step prediction  

  2.1 요일별 평균 RMSE, MAE 그래프   
  2.2 prediction graph  

3.데이터 별 변수중요도, step 중요도 Grad-CAM  

#### Discussion
1. RNN-CNN 과 CNN-RNN 의 구조적인 부분에 대한 논의가 있으면 좋을 것 같아요.. CNN-RNN은 많으니, RNN-CNN 페이퍼들 몇 개 보면서 논의하고 저희 꺼 비교하는 내용 하나 추가되면 좋을 것 같아요.   
2. Future work 언급   

### conclusion
결과 정리


