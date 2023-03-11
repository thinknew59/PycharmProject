# 숫자를 입력받아서 제곱 값을 출력하는 함수
def square(x):
    return x * x

# 숫자를 입력받아서 짝수이면 True, 홀수이면 False를 출력하는 함수
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# 리스트에서 최댓값을 구하는 함수
def max_list(a):
    max_value = a[0]
    for value in a:
        if value > max_value:
            max_value = value
    return max_value

# 예제 코드 실행
print(square(3))
print(is_even(4))
print(max_list([1, 5, 2, 9, 3]))