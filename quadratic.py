import math
import matplotlib.pyplot as plt
import numpy as np
import sys

# Styling constants from col.txt
FIGURE_FACECOLOR = "#EFF0F2"
AXIS_FACECOLOR = "#EFF0F2"
GRID_COLOR = "#857C79"
PLOT_COLOR = "#555386"  # Assuming this color for the plot line


def get_coefficients():
    """
    Prompts the user to input coefficients a, b, and c for a quadratic equation.
    Ensures that 'a' is not zero.
    """
    print("The form of a quadratic equation is ax² + bx + c = 0")

    while True:
        try:
            a = float(input("Enter coefficient a (must be non-zero): "))
            if a == 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Coefficient 'a' must be a non-zero number.")

    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    return a, b, c


def calculate_discriminant(a, b, c):
    """
    Calculates and returns the discriminant of the quadratic equation.
    """
    return b**2 - 4 * a * c


def find_roots(a, b, discriminant):
    """
    Finds and returns the roots of the quadratic equation.
    """
    sqrt_discriminant = math.sqrt(abs(discriminant))
    if discriminant > 0:
        return [(-b + sqrt_discriminant) / (2 * a), (-b - sqrt_discriminant) / (2 * a)]
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:  # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = sqrt_discriminant / (2 * a)
        return [complex(real_part, imaginary_part), complex(real_part, -imaginary_part)]


def print_equation_info(a, b, c, discriminant, roots):
    """
    Prints the equation, discriminant, nature of solutions, solutions, and vertex.
    """
    print(f"Solving {a}x² + {b}x + {c} = 0")
    print(f"Discriminant = {discriminant}")

    if discriminant > 0:
        print("Two real solutions")
    elif discriminant == 0:
        print("One real solution")
    else:
        print("Two complex solutions")

    for i, root in enumerate(roots, start=1):
        print(f"x{i} = {root}")

    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    print(f"Vertex = ({vertex_x}, {vertex_y})")


def plot_graph(a, b, c, roots):
    """
    Plots the quadratic equation.
    Handles both real and complex roots.
    """
    plt.figure(facecolor=FIGURE_FACECOLOR)
    ax = plt.gca()
    ax.set_facecolor(AXIS_FACECOLOR)

    # Determine range for x values
    if all(isinstance(root, complex) for root in roots):
        # For complex roots, plot around the vertex
        vertex_x = -b / (2 * a)
        x_range = np.linspace(vertex_x - 5, vertex_x + 5, 400)
    else:
        # For real roots, extend the range a bit beyond the roots
        x_range = np.linspace(min(roots).real - 1, max(roots).real + 1, 400)

    y_values = a * x_range**2 + b * x_range + c

    ax.plot(x_range, y_values, color=PLOT_COLOR, linewidth=2)
    for root in roots:
        if not isinstance(root, complex):
            ax.plot(
                root.real, a * root.real**2 + b * root.real + c, "ro"
            )  # Plotting the real roots

    plt.axhline(0, color=GRID_COLOR)  # x-axis
    plt.axvline(0, color=GRID_COLOR)  # y-axis
    plt.grid(color=GRID_COLOR, linestyle=":")
    plt.title(f"Graph of {a}x² + {b}x + {c} = 0")
    plt.tight_layout()
    plt.show()


def main():
    try:
        a, b, c = get_coefficients()
        discriminant = calculate_discriminant(a, b, c)
        roots = find_roots(a, b, discriminant)
        print_equation_info(a, b, c, discriminant, roots)
        plot_graph(a, b, c, roots)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
