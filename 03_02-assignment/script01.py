"""
Polynomial Multiplication (Brute Force)
"""

# Functions

def multiply(poly1: list, poly2: list) -> list:
    m = len(poly1)
    n = len(poly2)

    p = (m-1)+(n-1)
    poly = (p+1)*[0]

    for i in range(m):
        for j in range(n):
            p = i+j
            poly[p] += poly1[i] * poly2[j]

    return poly

# Main

if __name__ == '__main__':
    poly1 = [2, 0, 5, 7]
    poly2 = [3, 4, 2]

    poly = multiply(poly1, poly2)
    print(poly)
