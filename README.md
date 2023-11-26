# Matrix Condition Number Calculator

a Simple implementation for calculating condition number of a matrix with Python!

## What is Condition Number?

Condition number is a measure of the sensitivity of a function's output with respect to its input. In the context of a matrix, it is the ratio of the largest singular value of the matrix to the smallest singular value of the matrix. The smaller the condition number, the better conditioned the matrix is. A matrix with a condition number of 1 is a perfectly conditioned matrix.

### How to calculate Condition Number?

The condition number of a matrix can be calculated by using the following formula:

```math
\text{cn} = \| A \| \cdot \| A^{-1} \|
```

where ||A|| is the norm of the matrix and ||A^-1|| is the norm of the inverse of the matrix.

## How to use this script?

```bash

git clone https://github.com/smrrazavian/matrix_cn_calculator.git
cd matrix_cn_calculator
pip install numpy
```

change the matrix in main.py file and run the script!

```bash
python main.py
```
