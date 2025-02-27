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


class QuadraticEquation:
    """A class representing a quadratic equation in the form ax² + bx + c = 0."""

    def __init__(self, a: float, b: float, c: float):
        """Initialize the quadratic equation with coefficients a, b, and c.

        Args:
            a: The coefficient of x²
            b: The coefficient of x
            c: The constant term

        Raises:
            NonZeroCoeffiecientError: If coefficient 'a' is zero
        """
        if a == 0:
            raise NonZeroCoeffiecientError("Coefficient 'a' must be non-zero.")
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self._calculate_discriminant()
        self.roots = self._find_roots()
        self.vertex = self._calculate_vertex()

    @classmethod
    def from_command_line_args(cls, args: list[str]) -> 'QuadraticEquation':
        """Create a QuadraticEquation instance from command line arguments.

        Args:
            args: A list of command-line arguments (including the script name).

        Returns:
            A QuadraticEquation instance.

        Raises:
            InvalidInputError: If the command line arguments are incorrect.
        """
        if len(args) != 4:
            raise ValueError("Usage: python quadratic.py <a> <b> <c>")

        try:
            a_str, b_str, c_str = args[1], args[2], args[3]
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
            return cls(a, b, c)
        except ValueError as e:
            raise InvalidInputError(f"Invalid input: {e}") from e
        except TypeError as e:
            raise InvalidInputError(f"Invalid input: {e}") from e

    def _calculate_discriminant(self) -> float:
        """Calculate the discriminant of the quadratic equation.

        Returns:
            The calculated discriminant.
        """
        return self.b**2 - 4 * self.a * self.c

    def _find_roots(self) -> list[float | complex]:
        """Find the roots of the quadratic equation.

        Returns:
            A list containing the roots (either real numbers or complex numbers).
        """
        sqrt_discriminant = math.sqrt(abs(self.discriminant))
        if self.discriminant > 0:
            return [
                (-self.b + sqrt_discriminant) / (2 * self.a),
                (-self.b - sqrt_discriminant) / (2 * self.a)
            ]
        elif self.discriminant == 0:
            return [-self.b / (2 * self.a)]
        else:  # Complex roots
            real_part = -self.b / (2 * self.a)
            imaginary_part = sqrt_discriminant / (2 * self.a)
            return [complex(real_part, imaginary_part),
                    complex(real_part, -imaginary_part)]

    def _calculate_vertex(self) -> tuple[float, float]:
        """Calculate the vertex of the parabola.

        Returns:
            A tuple (x, y) representing the vertex coordinates.
        """
        x = -self.b / (2 * self.a)
        y = self.a * x**2 + self.b * x + self.c
        return (x, y)

    def print_info(self) -> None:
        """Print the equation information, including the equation itself,
        discriminant, nature of solutions, solutions, and vertex."""
        print(f"Solving {self.a}x² + {self.b}x + {self.c} = 0")
        print(f"Discriminant = {self.discriminant}")

        if self.discriminant > 0:
            print("Two real solutions")
        elif self.discriminant == 0:
            print("One real solution")
        else:
            print("Two complex solutions")

        for i, root in enumerate(self.roots, start=1):
            print(f"x{i} = {root}")

        print(f"Vertex = {self.vertex}")

    def plot(self) -> None:
        """Plot the quadratic equation graph."""
        plt.figure(facecolor=FIGURE_FACECOLOR)
        ax = plt.gca()
        ax.set_facecolor(AXIS_FACECOLOR)

        # Determine range for x values
        if all(isinstance(root, complex) for root in self.roots):
            # For complex roots, plot around the vertex
            x_range = np.linspace(
                self.vertex[0] - 5, self.vertex[0] + 5, X_RANGE_POINTS
            )
        else:
            # For real roots, extend the range a bit beyond the roots
            min_real_root = (
                min(root.real for root in self.roots
                    if not isinstance(root, complex))
                if any(not isinstance(root, complex) for root in self.roots) else 0
            )
            max_real_root = (
                max(root.real for root in self.roots
                    if not isinstance(root, complex))
                if any(not isinstance(root, complex) for root in self.roots) else 0
            )
            x_range = np.linspace(
                min_real_root - PLOT_RANGE_EXTENSION,
                max_real_root + PLOT_RANGE_EXTENSION, X_RANGE_POINTS
            )

        y_values = self.a * x_range**2 + self.b * x_range + self.c

        ax.plot(x_range, y_values, color=PLOT_COLOR, linewidth=2)
        for root in self.roots:
            if not isinstance(root, complex):
                ax.plot(
                    root.real,
                    self.a * root.real**2 + self.b * root.real + self.c,
                    "ro"
                )  # Plotting the real roots

        ax.plot(self.vertex[0], self.vertex[1], "go", label="Vertex")

        plt.axhline(0, color=GRID_COLOR, linewidth=AXIS_LINEWIDTH)  # x-axis
        plt.axvline(0, color=GRID_COLOR, linewidth=AXIS_LINEWIDTH)  # y-axis
        plt.grid(color=GRID_COLOR, linestyle=":", linewidth=GRID_LINEWIDTH)
        plt.title(f"Graph of {self.a}x² + {self.b}x + {self.c} = 0")
        plt.tight_layout()
        plt.show()


def main():
    """Main function to run the quadratic equation solver."""
    try:
        equation = QuadraticEquation.from_command_line_args(sys.argv)
        equation.print_info()
        equation.plot()

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
