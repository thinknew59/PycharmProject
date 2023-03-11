"""
Blender에서 실행 가능한 임의의 큐브 생성 코드. chatGPT
"""
import bpy
import random

def create_cube(x, y, z, size):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    bpy.context.object.scale = (size, size, size)


for i in range(10):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(-5, 5)
    size = random.uniform(-0.1, 1)
    create_cube(x, y, z, size)