"""
Polynomial Multiplication (Divide and Conquer)
"""

# Functions

def split_polynomial(poly: list):
    mid = len(poly) // 2
    return poly[:mid], poly[mid:]

def add_polynomial(polya: list, polyb: list) -> list:
    result = [0] * max(len(polya), len(polyb))
    for i in range(len(result)):
        if i < len(polya):
            result[i] += polya[i]
        if i < len(polyb):
            result[i] += polyb[i]
    return result

def increase_exponent(poly, n):
    return [0] * n + poly

def multiply(polya: list, polyb: list) -> list:
    if len(polya) == 1:
        return [polya[0] * value for value in polyb]

    if len(polyb) == 1:
        return [polyb[0] * value for value in polya]

    a0, a1 = split_polynomial(polya)
    b0, b1 = split_polynomial(polyb)

    a0b0 = multiply(a0, b0)
    a0b1 = multiply(a0, b1)
    a1b0 = multiply(a1, b0)
    a1b1 = multiply(a1, b1)

    m = len(polya)
    n = len(polyb)

    a0b1 = increase_exponent(a0b1, n // 2)
    a1b0 = increase_exponent(a1b0, m // 2)
    a1b1 = increase_exponent(a1b1, (m // 2) + (n // 2))

    result = add_polynomial(a0b0, a0b1)
    result = add_polynomial(result, a1b0)
    result = add_polynomial(result, a1b1)

    return result

# Main

if __name__ == '__main__':
    polya = [2, 5, 3, 1, -1]
    polyb = [1, 2, 2, 3, 6]

    poly = multiply(polya, polyb)
    print(poly)

    poly1 = [2, 0, 5, 7]
    poly2 = [3, 4, 2]

    poly = multiply(poly1, poly2)
    print(poly)
