from sklearn.linear_model import LinearRegression

# 데이터 준비
X_train = [[0.5], [1.0], [1.5], [2.0]]
y_train = [1.0, 2.0, 2.5, 3.5]

# 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
X_test = [[2.5], [3.0], [3.5]]
y_pred = model.predict(X_test)

print(y_pred)