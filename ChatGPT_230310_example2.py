import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy를 사용하여 랜덤한 2차원 배열 생성
arr = np.random.rand(10, 2)

# 2. Pandas를 사용하여 DataFrame 생성
df = pd.DataFrame(data=arr, columns=['x', 'y'])

# 3. Matplotlib를 사용하여 산점도 그래프 그리기
plt.scatter(df['x'], df['y'])
plt.show()


# 4. 함수를 사용하여 리스트에서 홀수만 추출하는 코드
def extract_odd(numbers):
    odds = []
    for num in numbers:
        if num % 2 == 1:
            odds.append(num)
    return odds


# 5. 리스트 컴프리헨션을 사용하여 리스트에서 홀수만 추출하는 코드
def extract_odd_comp(numbers):
    odds = [num for num in numbers if num % 2 == 1]
    return odds


# 6. 예외 처리를 사용하여 숫자를 0으로 나누는 경우 에러 처리하기
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        result = None
    return result


# 7. 클래스를 사용하여 계산기 구현하기
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            result = self.num1 / self.num2
        except ZeroDivisionError:
            print("Cannot divide by zero")
            result = None
        return result


# 예제 코드 실행
print(df.head())
print(extract_odd([1, 2, 3, 4, 5]))
print(extract_odd_comp([1, 2, 3, 4, 5]))
print(divide(5, 0))
calc = Calculator(10, 5)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())