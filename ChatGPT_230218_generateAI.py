import random

# # 생성 AI의 예제 코드
# def generate_shape():
#     # 도형의 형태를 무작위로 선택
#     shape_type = random.choice(["square", "circle", "triangle"])
#
#     # 도형의 크기를 무작위로 선택
#     size = random.randint(1, 10)
#
#     # 도형의 색상을 무작위로 선택
#     color = random.choice(["red", "green", "blue"])
#
#     # 도형을 생성하여 반환
#     if shape_type == "square":
#         return f"Square(size={size}, color='{color}')"
#     elif shape_type == "circle":
#         return f"Circle(radius={size}, color='{color}')"
#     else:
#         return f"Triangle(size={size}, color='{color}')"
#
#
# # 예제 코드를 실행하여 생성된 도형 출력
# print(generate_shape())

# # Square, Circle, Triangle 클래스 정의
# class Square:
#     def __init__(self, size, color):
#         self.size = size
#         self.color = color
#
#     def draw(self):
#         print(f"Drawing a square of size {self.size} and color {self.color}")
#
#
# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def draw(self):
#         print(f"Drawing a circle of radius {self.radius} and color {self.color}")
#
#
# class Triangle:
#     def __init__(self, size, color):
#         self.size = size
#         self.color = color
#
#     def draw(self):
#         print(f"Drawing a triangle of size {self.size} and color {self.color}")
#
# # 생성 AI의 예제 코드
# def generate_shape():
#     # 도형의 형태를 무작위로 선택
#     shape_type = random.choice(["square", "circle", "triangle"])
#
#     # 도형의 크기를 무작위로 선택
#     size = random.randint(1, 10)
#
#     # 도형의 색상을 무작위로 선택
#     color = random.choice(["red", "green", "blue"])
#
#     # 도형을 생성하여 반환
#     if shape_type == "square":
#         return Square(size=size, color=color)
#     elif shape_type == "circle":
#         return Circle(radius=size, color=color)
#     else:
#         return Triangle(size=size, color=color)
#
# # 생성된 도형을 화면에 출력하는 코드
# shape = generate_shape()
# shape.draw()

import random
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Square, Circle, Triangle 클래스 정의
class Square:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        img = Image.new('RGB', (self.size, self.size), color=self.color)
        return img

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def draw(self):
        img = Image.new('RGB', (self.radius * 2, self.radius * 2), color=self.color)
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, self.radius * 2, self.radius * 2), fill=self.color)
        return img

class Triangle:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        img = Image.new('RGB', (self.size, self.size), color=self.color)
        draw = ImageDraw.Draw(img)
        draw.polygon([(0, self.size), (self.size, self.size), (self.size // 2, 0)], fill=self.color)
        return img

# 생성 AI의 예제 코드
def generate_shape():
    # 도형의 형태를 무작위로 선택
    shape_type = random.choice(["square", "circle", "triangle"])

    # 도형의 크기를 무작위로 선택
    size = random.randint(1, 10)

    # 도형의 색상을 무작위로 선택
    color = random.choice(["red", "green", "blue"])

    # 도형을 생성하여 반환
    if shape_type == "square":
        return Square(size=size, color=color)
    elif shape_type == "circle":
        return Circle(radius=size, color=color)
    else:
        return Triangle(size=size, color=color)

# 생성된 도형을 이미지 파일로 저장하고, 그래프로 출력하는 코드
shape = generate_shape()
img = shape.draw()
img.save("generated_shape.png")
plt.imshow(img)
plt.show()