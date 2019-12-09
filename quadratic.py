import math
import matplotlib.pyplot as plt
import numpy as np

print('The form of a quadratic equation is ax\u00B2 + bx + c = 0')

a = float(input('a =  '))
b = float(input('b =  '))
c = float(input('c =  '))

print(f'Solving {a}x\u00B2 + {b}x + {c} = 0')

discriminant = round(b**2 - (4*a*c), 2)

# x and y coordinates of the vertex
x_vertex = -b / (2 * a)
y_vertex = a * (x_vertex**2) + (b * x_vertex) + c

x_vertex = round(x_vertex, 2)
y_vertex = round(y_vertex, 2)

x_plot = []
y_plot = []

if discriminant > 0:
    print('Discriminant > 0')
    print(f'Discriminant = {discriminant}')
    print('Two real solutions')
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)

    x1 = round(x1, 2)
    x2 = round(x2, 2)

    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    print(f'Vertex = ({x_vertex}, {y_vertex})')

    for x in np.linspace(x_vertex - 3, x_vertex + 3):
        y = a * (x**2) + (b * x) + c
        x_plot.append(x)
        y_plot.append(y)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x_plot, y_plot, color='lightblue', linewidth=3)
    ax.plot(x1, 0, marker='o', markersize=10, color='b', alpha=0.65)
    ax.plot(x2, 0, marker='o', markersize=10, color='b', alpha=0.65)
    ax.plot(x_vertex, y_vertex, marker='o',
            markersize=10, color='b', alpha=0.65)
    ax.annotate(f'x\u2081 ({x1}, 0)', xy=(
        x1, 0), xytext=(0, 25), textcoords='offset points')
    ax.annotate(f'x\u2082 ({x2}, 0)', xy=(
        x2, 0), xytext=(0, 25), textcoords='offset points')
    ax.annotate(f'vertex ({x_vertex}, {y_vertex})', xy=(
        x_vertex, y_vertex), xytext=(0, 25), textcoords='offset points')


elif discriminant == 0:
    print('Discriminant = 0')
    print('One real solution')
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x1 = round(x1, 2)
    print(f'x = {x1}')
    print(f'Vertex = ({x_vertex}, {y_vertex})')

    for x in np.linspace(x_vertex - 3, x_vertex + 3):
        y = a * (x**2) + (b * x) + c
        x_plot.append(x)
        y_plot.append(y)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x_plot, y_plot, color='lightblue', linewidth=3)
    ax.plot(x1, 0, marker='o', markersize=10, color='b', alpha=0.65)
    ax.annotate(f'x\u2081 = vertex ({x_vertex}, {y_vertex})', xy=(
        x_vertex, y_vertex), xytext=(0, 25), textcoords='offset points')

else:  # Discriminant < 0
    print('Discriminant < 0')
    print(f'Discriminant = {discriminant}')
    print('Two complex solutions')
    discriminant = abs(discriminant)
    imaginary = math.sqrt(discriminant) / (2*a)
    real_part = -b / (2*a)

    imaginary = round(imaginary, 2)
    real_part = round(real_part, 2)

    print(f'x1 = {real_part} + {imaginary}i')
    print(f'x2 = {real_part} - {imaginary}i')
    print(f'Vertex = ({x_vertex}, {y_vertex})')

    for x in np.linspace(x_vertex - 3, x_vertex + 3):
        y = a * (x**2) + (b * x) + c
        x_plot.append(x)
        y_plot.append(y)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x_plot, y_plot, color='lightblue', linewidth=3)
    ax.plot(x_vertex, y_vertex, marker='o',
            markersize=10, color='b', alpha=0.65)

    ax.annotate(f'vertex ({x_vertex}, {y_vertex})', xy=(
        x_vertex, y_vertex), xytext=(0, 25), textcoords='offset points')


plt.plot(0, 0, marker='o',
         markersize=10, color='orange', alpha=0.65)
ax.annotate(f'(0, 0)', xy=(
    0, 0), xytext=(5, 5), textcoords='offset points')
plt.axhline(y=0, linewidth=3, color='orange', alpha=0.65)
plt.axvline(x=0, linewidth=3, color='orange', alpha=0.65)
plt.title(f'{a}x\u00B2 + {b}x + {c} = 0')
plt.grid()
plt.show()
