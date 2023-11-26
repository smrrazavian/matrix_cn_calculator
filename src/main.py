"""the main file of the Matrix's Condition Number."""
import numpy as np


def calculate_condition_number(A: np.ndarray) -> np.float64:
    """
    Calculate the condition number of a matrix.

    Parameters:
    A (numpy.ndarray): A square matrix.

    Returns:
    float: The condition number of the matrix.
    """
    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square to calculate condition number.")
    try:
        norm_A = np.linalg.norm(A)
        inv_A = np.linalg.inv(A)
        norm_inv_A = np.linalg.norm(inv_A)
        cond_number = norm_A * norm_inv_A
        return cond_number
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is singular and cannot have a condition number.")
    except Exception as e:
        raise e


def main():
    """Main function of the project."""
    A = np.array([[1, 2], [1.01, 2]])
    cond_number = calculate_condition_number(A)
    print("Condition Number of the matrix is:", cond_number)


if __name__ == "__main__":
    main()
