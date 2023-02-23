# # # import random
# # #
# # # shapes = ["원", "사각형", "삼각형", "마름모", "오각형"]
# # # sizes = ["작은", "중간", "큰"]
# # # colors = ["빨간색", "파란색", "노란색", "초록색", "보라색"]
# # # num_shapes = random.randint(1, 10)
# # #
# # # for i in range(num_shapes):
# # #     shape = random.choice(shapes)
# # #     size = random.choice(sizes)
# # #     color = random.choice(colors)
# # #     print(f"{size} {color} {shape}")
# #
# # import turtle
# # import random
# #
# # shapes = ["circle", "square", "triangle"]
# # sizes = [20, 50, 80]
# # colors = ["red", "blue", "green", "purple", "yellow"]
# # num_shapes = random.randint(1, 10)
# #
# # turtle.speed("fastest")
# #
# # for i in range(num_shapes):
# #     shape = random.choice(shapes)
# #     size = random.choice(sizes)
# #     color = random.choice(colors)
# #     x = random.randint(-300, 300)
# #     y = random.randint(-300, 300)
# #
# #     turtle.penup()
# #     turtle.goto(x, y)
# #     turtle.pendown()
# #     turtle.color(color)
# #     if shape == "circle":
# #         turtle.circle(size)
# #     elif shape == "square":
# #         for j in range(4):
# #             turtle.forward(size)
# #             turtle.right(90)
# #     elif shape == "triangle":
# #         for j in range(3):
# #             turtle.forward(size)
# #             turtle.right(120)
# #
# # turtle.done()
#
# import turtle
# import random
#
# shapes = ["원", "사각형", "삼각형", "마름모", "오각형"]
# sizes = ["작은", "중간", "큰"]
# colors = ["빨간색", "파란색", "노란색", "초록색", "보라색"]
# num_shapes = random.randint(1, 10)
#
# turtle.speed("fastest")
#
# for i in range(num_shapes):
#     shape = random.choice(shapes)
#     size = random.choice(sizes)
#     color = random.choice(colors)
#
#     turtle.color(color)
#     if shape == "원":
#         if size == "작은":
#             turtle.circle(20)
#         elif size == "중간":
#             turtle.circle(50)
#         elif size == "큰":
#             turtle.circle(80)
#     elif shape == "사각형":
#         if size == "작은":
#             for j in range(4):
#                 turtle.forward(20)
#                 turtle.right(90)
#         elif size == "중간":
#             for j in range(4):
#                 turtle.forward(50)
#                 turtle.right(90)
#         elif size == "큰":
#             for j in range(4):
#                 turtle.forward(80)
#                 turtle.right(90)
#     elif shape == "삼각형":
#         if size == "작은":
#             for j in range(3):
#                 turtle.forward(20)
#                 turtle.right(120)
#         elif size == "중간":
#             for j in range(3):
#                 turtle.forward(50)
#                 turtle.right(120)
#         elif size == "큰":
#             for j in range(3):
#                 turtle.forward(80)
#                 turtle.right(120)
#     elif shape == "마름모":
#         if size == "작은":
#             turtle.begin_fill()
#             for j in range(4):
#                 turtle.forward(20)
#                 turtle.right(45)
#             turtle.end_fill()
#         elif size == "중간":
#             turtle.begin_fill()
#             for j in range(4):
#                 turtle.forward(50)
#                 turtle.right(45)
#             turtle.end_fill()
#         elif size == "큰":
#             turtle.begin_fill()
#             for j in range(4):
#                 turtle.forward(80)
#                 turtle.right(45)
#             turtle.end_fill()
#     elif shape == "오각형":
#         if size == "작은":
#             turtle.begin_fill()
#             for j in range(5):
#                 turtle.forward(20)
#                 turtle.right(72)
#             turtle.end_fill()
#         elif size == "중간":
#             turtle.begin_fill()
#             for j in range(5):
#                 turtle.forward(50)
#                 turtle.right(72)
#             turtle.end_fill()
#         elif size == "큰":
#             turtle.begin_fill()
#             for j in range(5):
#                 turtle.forward(80)
#                 turtle.right(72)
#             turtle.end_fill()
#
# turtle.done()

import turtle
import random

shapes = {
    "원": turtle.circle,
    "사각형": turtle.begin_fill,
    "삼각형": turtle.begin_fill,
    "마름모": turtle.begin_fill,
    "오각형": turtle.begin_fill,
}

sizes = {
    "작은": 20,
    "중간": 50,
    "큰": 80,
}

colors = ["빨간색", "파란색", "노란색", "초록색", "보라색"]

num_shapes = random.randint(1, 10)

turtle.speed("fastest")

for i in range(num_shapes):
    shape = random.choice(list(shapes.keys()))
    size = random.choice(list(sizes.keys()))
    color = random.choice(colors)

    turtle.color(color)

    if shape == "원":
        shapes[shape](sizes[size])
    else:
        sides = {
            "사각형": 4,
            "삼각형": 3,
            "마름모": 4,
            "오각형": 5,
        }
        angle = {
            "사각형": 90,
            "삼각형": 120,
            "마름모": 45,
            "오각형": 72,
        }
        turtle.right(angle[shape] / 2)
        for j in range(sides[shape]):
            turtle.forward(sizes[size])
            turtle.right(angle[shape])
        turtle.left(angle[shape] / 2)
        turtle.end_fill()

turtle.done()

"""
turtle.TurtleGraphicsError: bad color string: 노란색
"""