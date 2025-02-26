import math
import sys

import matplotlib.pyplot as plt
import numpy as np

# Styling constants
FIGURE_FACECOLOR = "#EFF0F2"
AXIS_FACECOLOR = "#EFF0F2"
GRID_COLOR = "#857C79"
PLOT_COLOR = "#555386"
AXIS_LINEWIDTH = 1.5
GRID_LINEWIDTH = 0.8
X_RANGE_POINTS = 400
PLOT_RANGE_EXTENSION = 1


class InvalidInputError(Exception):
    """Custom exception for invalid input."""

    pass


class NonZeroCoeffiecientError(Exception):
    """Custom exception for when the coeffiecient a is zero."""

    pass


def get_coefficients_from_args(args: list[str]) -> tuple[float, float, float]:
    """
    Gets coefficients a, b, and c from a list of string arguments.  Corrected to handle negative numbers.

    Args:
        args: A list of command-line arguments (including the script name).

    Returns:
        A tuple containing the coefficients (a, b, c).

    Raises:
        ValueError: If the number of arguments is incorrect.
        TypeError: If any of the coefficients are not numbers.
        NonZeroCoeffiecientError: If the coefficient 'a' is zero.
    """
    if len(args) != 4:
        raise ValueError("Usage: python quadratic.py <a> <b> <c>")

    try:
        a_str, b_str, c_str = args[1], args[2], args[3]

        a = float(a_str)
        b = float(b_str)
        c = float(c_str)

        if a == 0:
            raise NonZeroCoeffiecientError("Coefficient 'a' must be non-zero.")

        return a, b, c
    except ValueError as e:
        raise InvalidInputError(f"Invalid input: {e}") from e
    except TypeError as e:
        raise InvalidInputError(f"Invalid input: {e}") from e


def calculate_discriminant(a: float, b: float, c: float) -> float:
    """
    Calculates and returns the discriminant of the quadratic equation.

    Args:
        a: The coefficient 'a' of the equation.
        b: The coefficient 'b' of the equation.
        c: The coefficient 'c' of the equation.

    Returns:
        The calculated discriminant.
    """
    return b**2 - 4 * a * c


def find_roots(a: float, b: float, discriminant: float) -> list[float | complex]:
    """Finds and returns the roots of the quadratic equation.

    Args:
        a: The coefficient 'a' of the equation.
        b: The coefficient 'b' of the equation.
        discriminant: The calculated discriminant.

    Returns:
        A list containing the roots (either real numbers or complex numbers).
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


def print_equation_info(
    a: float, b: float, c: float, discriminant: float, roots: list[float | complex]
) -> None:
    """
    Prints the equation, discriminant, nature of solutions, solutions, and vertex.

    Args:
        a: The coefficient 'a' of the equation.
        b: The coefficient 'b' of the equation.
        c: The coefficient 'c' of the equation.
        discriminant: The calculated discriminant.
        roots: A list of the calculated roots.
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


def plot_graph(a: float, b: float, c: float, roots: list[float | complex]) -> None:
    """
    Plots the quadratic equation.
    Handles both real and complex roots.

    Args:
        a: The coefficient 'a' of the equation.
        b: The coefficient 'b' of the equation.
        c: The coefficient 'c' of the equation.
        roots: A list of the calculated roots.
    """
    plt.figure(facecolor=FIGURE_FACECOLOR)
    ax = plt.gca()
    ax.set_facecolor(AXIS_FACECOLOR)

    # Determine range for x values
    if all(isinstance(root, complex) for root in roots):
        # For complex roots, plot around the vertex
        vertex_x = -b / (2 * a)
        x_range = np.linspace(vertex_x - 5, vertex_x + 5, X_RANGE_POINTS)
    else:
        # For real roots, extend the range a bit beyond the roots
        min_real_root = (
            min(root.real for root in roots if not isinstance(root, complex))
            if any(not isinstance(root, complex) for root in roots)
            else 0
        )
        max_real_root = (
            max(root.real for root in roots if not isinstance(root, complex))
            if any(not isinstance(root, complex) for root in roots)
            else 0
        )
        x_range = np.linspace(
            min_real_root - PLOT_RANGE_EXTENSION,
            max_real_root + PLOT_RANGE_EXTENSION,
            X_RANGE_POINTS,
        )

    y_values = a * x_range**2 + b * x_range + c

    ax.plot(x_range, y_values, color=PLOT_COLOR, linewidth=2)
    for root in roots:
        if not isinstance(root, complex):
            ax.plot(
                root.real, a * root.real**2 + b * root.real + c, "ro"
            )  # Plotting the real roots

    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    ax.plot(vertex_x, vertex_y, "go", label="Vertex")

    plt.axhline(0, color=GRID_COLOR, linewidth=AXIS_LINEWIDTH)  # x-axis
    plt.axvline(0, color=GRID_COLOR, linewidth=AXIS_LINEWIDTH)  # y-axis
    plt.grid(color=GRID_COLOR, linestyle=":", linewidth=GRID_LINEWIDTH)
    plt.title(f"Graph of {a}x² + {b}x + {c} = 0")
    plt.tight_layout()
    plt.show()


def quadratic_solver(
    args: list[str],
) -> tuple[float, float, float, float, list[float | complex]]:
    """
    Solves the quadratic equation based on command line arguments.

    Args:
        args: A list of command-line arguments (including the script name).

    Returns:
        a tuple containing (a,b,c, discriminant, roots)
    Raises:
        InvalidInputError: if the command line arguments are incorrect
    """
    a, b, c = get_coefficients_from_args(args)
    discriminant = calculate_discriminant(a, b, c)
    roots = find_roots(a, b, discriminant)
    return a, b, c, discriminant, roots


def main():
    """
    Main function to run the quadratic equation solver.
    """
    try:
        a, b, c, discriminant, roots = quadratic_solver(sys.argv)
        print_equation_info(a, b, c, discriminant, roots)
        plot_graph(a, b, c, roots)

    except InvalidInputError as e:
        print(e)
        print("Usage: python quadratic.py <a> <b> <c>")
        print("a, b, and c are coefficients of the quadratic equation (ax² + bx + c)")
        sys.exit(1)
    except NonZeroCoeffiecientError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
