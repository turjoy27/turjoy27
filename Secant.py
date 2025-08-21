import math

def f(x):
    return x**3 - x - 2   
def secant(x0, x1, tol, max_iter):
    for iteration in range(1, max_iter+1):
        if f(x1) - f(x0) == 0:
            print("Division by zero error in Secant method.")
            return None
        
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        
        print(f"Iteration {iteration}: x0={x0}, x1={x1}, x2={x2}, f(x2)={f(x2)}")
        
        if abs(f(x2)) < tol:
            return x2
        
        x0, x1 = x1, x2
    
    return x2  
x0 = 1   
x1 = 2   
tol = 1e-6
max_iter = 50

root = secant(x0, x1, tol, max_iter)
if root is not None:
    print("\nApproximate root:", root)


print("Turjoy Mondal")
