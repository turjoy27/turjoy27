import math
def gauss_jordan(a, b):
    n = len(b)

    for i in range(n):
        a[i].append(b[i])

    for i in range(n):
        if a[i][i] == 0:
            print("Mathematical Error: Zero pivot encountered!")
            return None

        pivot = a[i][i]
        for j in range(i, n+1):
            a[i][j] = a[i][j] / pivot

        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(i, n+1):
                    a[k][j] = a[k][j] - factor * a[i][j]

    x = [a[i][n] for i in range(n)]
    return x

a = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

b = [8, -11, -3]

solution = gauss_jordan(a, b)
print("Solution:", solution)

print("Turjoy Mondal")