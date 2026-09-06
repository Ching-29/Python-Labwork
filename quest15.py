from scipy.optimize import minimize

# Define the function
def function(x):
    return x**2 - 4*x + 5

# Initial guess
x0 = [0]

# Perform minimization
result = minimize(function, x0)

# Display results
print("Minimum value of x =", result.x[0])
print("Minimum value of function =", result.fun)
