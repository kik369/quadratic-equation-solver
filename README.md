# Quadratic Equation Solver

## Description

The `quadratic-equation-solver` is a Python script for solving quadratic equations. It can handle equations with real and complex roots, and it visualizes the equation on a graph.

## Installation

To use this script, you'll need Python installed on your system along with a few additional libraries.

### Prerequisites

-   Python 3.x
-   matplotlib
-   numpy

### Setup

1. Clone the repository:
    ```
    git clone https://github.com/kik369/quadratic-equation-solver.git
    ```
2. Navigate to the cloned directory:
    ```
    cd quadratic-equation-solver
    ```
3. (Optional) Create and activate a virtual environment:
    ```
    python -m venv env
    env\Scripts\activate # On Windows
    source env/bin/activate  # On Unix or MacOS
    ```
4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

Run the script by passing the coefficients of the quadratic equation as arguments:

```
python quadratic.py <a> <b> <c>
```

For example:

```
python quadratic.py 1 -5 6
```

This will solve the equation `x² - 5x + 6 = 0`.

## Screenshots

![Figure_4](https://github.com/kik369/quadratic-equation-solver/blob/main/img/Figure_4.png)
![Figure_1](https://github.com/kik369/quadratic-equation-solver/blob/main/img/Figure_1.png)
![Figure_2](https://github.com/kik369/quadratic-equation-solver/blob/main/img/Figure_2.png)
![Figure_3](https://github.com/kik369/quadratic-equation-solver/blob/main/img/Figure_3.png)

## License

Distributed under the MIT License. See `LICENSE` for more information.
