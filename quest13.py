import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad

# Define mathematical function
def f(x):
    return x**2 + 2*x + 1


# Point at which derivative is required
x = 2

# Numerical differentiation
h = 0.0001

derivative_value = (f(x + h) - f(x - h)) / (2 * h)

print("Function: f(x) = x^2 + 2x + 1")

print("\nNumerical Derivative at x =", x)
print(derivative_value)


# Numerical integration
lower_limit = 0
upper_limit = 2

integral_value, error = quad(f, lower_limit, upper_limit)

print("\nNumerical Integration")
print("Limits:", lower_limit, "to", upper_limit)
print("Integral:", integral_value)
print("Estimated Error:", error)
