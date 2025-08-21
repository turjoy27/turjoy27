import math

def f(x):
    return x**3 - x - 2  

def regula_falsi(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Regula Falsi method fails. f(a) and f(b) must have opposite signs.")
        return None
    
    c = a  
    for iteration in range(1, max_iter+1):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        
        print(f"Iteration {iteration}: a={a}, b={b}, c={c}, f(c)={f(c)}")
        
        if abs(f(c)) < tol:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c 

a = 1
b = 2
tol = 1e-6
max_iter = 50

root = regula_falsi(a, b, tol, max_iter)
if root is not None:
    print("\nApproximate root:", root)
print("Turjoy Mondal")