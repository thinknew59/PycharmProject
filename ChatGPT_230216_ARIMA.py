import yfinance as yf
import pandas as pd

# 데이터를 가져올 기간 설정
start_date = '2010-01-01'
end_date = '2022-02-16'

# 애플 주식 데이터 가져오기
apple = yf.Ticker("AAPL")
apple_stock = apple.history(start=start_date, end=end_date)
# print(apple_stock)

# 종가 데이터만 추출
apple_close = apple_stock['Close']
# print(apple_close)

# 결측치 제거
apple_close = apple_close.dropna()
# print(apple_close)

from statsmodels.tsa.arima.model import ARIMA

# ARIMA 모델 학습
model = ARIMA(apple_close, order=(1, 1, 1))
model_fit = model.fit()

# 예측 결과 출력
# print(model_fit.summary())

# 애플 주식 가격 예측
forecast = model_fit.forecast(steps=30)

# 예측 결과 출력
print(forecast)