# Problem

## Polynomial Multiplication

Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials. For example, the lists `[2, 0, 5, 7]` and `[3, 4, 2]` represent the polynomials $2 + 5x^2 + 7x^3$ and $3 + 4x + 2x^2$.

Their product is

$(2 \times 3) + (2 \times 4 + 0 \times 3)x + (2 \times 2 + 3 \times 5 + 4 \times 0)x^2 + (7 \times 3 + 5 \times 4 + 0 \times 2)x^3 + (7 \times 4 + 5 \times 2)x^4 + (7 \times 2)x^5$

i.e.

$6 + 8x + 19x^2 + 41x^3 + 38x^4 + 14x^5$

It can be represented by the list `[6, 8, 19, 41, 38, 14]`.

# List of Scripts

1. Polynomial Multiplication (Brute Force)
2. Polynomial Multiplication (Divide and Conquer)
