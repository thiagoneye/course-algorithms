"""
Polynomial Multiplication (Divide and Conquer)
"""

# Functions

def split_polynomial(poly: list):
    mid = len(poly) // 2
    return poly[:mid], poly[mid:]

def add_polynomial(poly1: list, poly2: list) -> list:
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def increase_exponent(poly, n):
    return [0] * n + poly

def multiply(poly1: list, poly2: list) -> list:
    if len(poly1) == 1:
        return [poly1[0] * value for value in poly2]

    if len(poly2) == 1:
        return [poly2[0] * value for value in poly1]

    polya, polyb = split_polynomial(poly1)
    polyc, polyd = split_polynomial(poly2)

    ac = multiply(polya, polyc)
    ad = multiply(polya, polyd)
    bc = multiply(polyb, polyc)
    bd = multiply(polyb, polyd)

    m = len(poly1)
    n = len(poly2)

    ad = increase_exponent(ad, n // 2)
    bc = increase_exponent(bc, m // 2)
    bd = increase_exponent(bd, (m // 2) + (n // 2))

    result = add_polynomial(ac, ad)
    result = add_polynomial(result, bc)
    result = add_polynomial(result, bd)

    return result

# Main

if __name__ == '__main__':
    poly1 = [2, 5, 3, 1, -1]
    poly2 = [1, 2, 2, 3, 6]

    poly = multiply(poly1, poly2)
    print(poly)

    poly1 = [2, 0, 5, 7]
    poly2 = [3, 4, 2]

    poly = multiply(poly1, poly2)
    print(poly)
