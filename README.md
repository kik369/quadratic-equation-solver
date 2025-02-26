# Quadratic Equation Solver

## Description

The `quadratic-equation-solver` is a robust Python script designed to solve quadratic equations, handling both real and complex roots. It incorporates comprehensive error handling and presents results clearly, including a graphical visualization of the equation. The code is structured for maintainability and testability, following best practices for professional software development.

## Installation

To use this script, you'll need Python installed on your system along with the `matplotlib` and `numpy` libraries.

### Prerequisites

-   Python 3.x
-   matplotlib
-   numpy

### Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/kik369/quadratic-equation-solver.git
    ```
2.  Navigate to the cloned directory:
    ```bash
    cd quadratic-equation-solver
    ```
3.  (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv  # Create a virtual environment (Use python -m venv .venv on Windows)
    source .venv/bin/activate  # Activate the virtual environment (Use .venv\Scripts\activate on Windows)
    ```
4.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script by passing the coefficients of the quadratic equation as command-line arguments:

```bash
python quadratic.py <a> <b> <c>
```

## Example Output

Here are some example outputs showing the graph of the quadratic equation and its solutions:

![Example 1](https://raw.githubusercontent.com/kik369/quadratic-equation-solver/main/img/Figure_1.png)
![Example 2](https://raw.githubusercontent.com/kik369/quadratic-equation-solver/main/img/Figure_2.png)
![Example 3](https://raw.githubusercontent.com/kik369/quadratic-equation-solver/main/img/Figure_3.png)
![Example 4](https://raw.githubusercontent.com/kik369/quadratic-equation-solver/main/img/Figure_4.png)
