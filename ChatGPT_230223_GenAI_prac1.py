import turtle
import random

shapes = {'원': turtle.circle, '사각형': turtle.begin_fill, '삼각형': turtle.begin_fill, '마름모': turtle.begin_fill,
          '오각형': turtle.begin_fill}

sizes = {'small': 20, 'medium': 50, 'large': 80}

colors = ['red', 'blue', 'yellow', 'green', 'purple']

num_shapes = random.randint(1, 10)

turtle.speed('fastest')

for i in range(num_shapes):
    shape = random.choice(list(shapes.keys()))
    size = random.choice(list(sizes.keys()))
    color = random.choice(colors)

    turtle.color(color)

    if shape == '원':
        shapes[shape](sizes[size])
    else:
        sides = {'사각형': 4, '삼각형': 3, '마름모': 4, '오각형': 5}
        angle = {'사각형': 90, '삼각형': 120, '마름모': 45, '오각형': 72}
        turtle.right(angle[shape] /2)
        for j in range(sides[shape]):
            turtle.forward(sizes[size])
            turtle.right(angle[shape])
        turtle.left(angle[shape]/2)
        turtle.end_fill()

turtle.done()