import math
import matplotlib.pyplot as plt
import numpy as np

print('The form of a quadratic equation is ax^2 + bx + c = 0')

a = float(input('a =  '))
b = float(input('b =  '))
c = float(input('c =  '))

print(f'Solving {a}x^2 + {b}x + {c}')

discriminant = (math.pow(b, 2) - 4*a*c)

# x and y coordinates of the vertex
x_vertex = (-b / (2 * a))
y_vertex = a * (x_vertex**2) + (b * x_vertex) + c

x_plot = []
y_plot = []

if discriminant > 0:
    print('Discriminant > 0')
    print(f'Discriminant = {discriminant}')
    print('Two real solutions')
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    print(f'Vertex = ({x_vertex}, {y_vertex})')

    for x in np.linspace(x1, x2):
        y = a * (x**2) + (b * x) + c
        x_plot.append(x)
        y_plot.append(y)

    plt.plot(x1, 0, marker='o', markersize=10, color='b', alpha=0.65)
    plt.plot(x2, 0, marker='o', markersize=10, color='b', alpha=0.65)
    plt.plot(x_vertex, y_vertex, marker='o', markersize=10, color='b', alpha=0.65)

    plt.text(x1, 0, f'x\u2081 = ({x1}, 0)', fontsize=14)
    plt.text(x2, 0, f'x\u2082 = ({x2}, 0)', fontsize=14)
    plt.text(x_vertex, y_vertex, f'({x_vertex}, {y_vertex})', fontsize=14)

elif discriminant == 0:
    print('Discriminant = 0')
    print('One real solution')
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    print(f'x = {x1}')
    print(f'Vertex = ({x_vertex}, {y_vertex})')

    for x in np.linspace(-25, 25):
        y = a * (x**2) + (b * x) + c
        x_plot.append(x)
        y_plot.append(y)

    plt.plot(x1, 0, marker='o', markersize=10, color='b', alpha=0.65)

    plt.text(x1, 0, f'({x1}, 0)', fontsize=14)


else: #Discriminant < 0
    print('Discriminant < 0')
    print(f'Discriminant = {discriminant}')
    print('Two complex solutions')
    discriminant = discriminant * (-1)
    imaginary = math.sqrt(discriminant) / (2*a)
    real_part = -b / (2*a)
    print(f'x1 = {real_part} + {imaginary}i')
    print(f'x2 = {real_part} - {imaginary}i')
    print(f'Vertex = ({x_vertex}, {y_vertex})')

    for x in np.linspace(-25,25):
        y = a * (x**2) + (b * x) + c
        x_plot.append(x)
        y_plot.append(y)
    
    plt.plot(x_vertex, y_vertex, marker='o', markersize=10, color='b', alpha=0.65)
    plt.text(x_vertex, y_vertex, f'({x_vertex}, {y_vertex})', fontsize=14)

plt.plot(x_plot, y_plot)
# plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.grid()
plt.title(f'{a}x^2 + {b}x + {c}')
plt.show()
