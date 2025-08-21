def f(x):
    return x**3 - x - 2   # Example: f(x) = x^3 - x - 2

def bisection(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2  
        if f(c) == 0:    
            return c
        elif f(a) * f(c) < 0: 
            b = c
        else:  
            a = c
        iteration += 1

    return (a + b) / 2 

a = 1  
b = 2      
tol = 1e-6 
max_iter = 100

root = bisection(a, b, tol, max_iter)
print("Approximate root:", root)
