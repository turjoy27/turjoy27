import math

def gauss_elimination(a, b):
    n = len(b)

 
    for i in range(n):
        if a[i][i] == 0:
            print("Mathematical Error: Zero pivot encountered!")
            return None
        
        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] = a[j][k] - ratio * a[i][k]
            b[j] = b[j] - ratio * b[i]

    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    
    return x


a = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

b = [8, -11, -3]

solution = gauss_elimination(a, b)
print("Solution:", solution)

print("Turjoy Mondal")