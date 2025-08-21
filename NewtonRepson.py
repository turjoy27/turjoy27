import math

def f(x):
    return x**3 - x - 2   

def df(x):
    return 3*x**2 - 1    

def newton_raphson(x0, tol, max_iter):
    for iteration in range(1, max_iter+1):
        if df(x0) == 0:
            print("Derivative is zero. Method fails.")
            return None
        
        x1 = x0 - f(x0)/df(x0)  
        
        print(f"Iteration {iteration}: x0={x0}, x1={x1}, f(x1)={f(x1)}")
        
        if abs(f(x1)) < tol:
            return x1
        
        x0 = x1  
        
    return x1  

x0 = 1.5   
tol = 1e-6
max_iter = 50

root = newton_raphson(x0, tol, max_iter)
if root is not None:
    print("\nApproximate root:", root)

print("Turjoy Mondal")