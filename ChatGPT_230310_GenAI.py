import tensorflow as tf
import numpy as np

# 학습 데이터 생성
x_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([[2], [4], [6], [8], [10]])

# 모델 정의
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

# 모델 컴파일
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss='mse')

# 모델 학습
model.fit(x_train, y_train, epochs=100)

# 모델 사용 예측
x_test = np.array([[6], [7], [8]])
y_pred = model.predict(x_test)
print(y_pred)