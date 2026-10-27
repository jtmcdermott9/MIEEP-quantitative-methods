#---PS 1: Static Partial Equilibrium Model---#

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Define known variables and parameters
gamma = 0.5
sigma = 3

# Create a 1D array of hours worked values from 0 to 1 with 100 increments
hours = np.linspace(0, 1, 100)

# Define function f(h) - NDArray -> NDArray

def utility(hours):

    return (1-hours) - gamma*(hours**sigma)

# Define function that uses bisection to find a function's zero point !TODO: implement error handling/infinite loop check

def bisection(a,b):

    tolerance = 10 ** -8

    while (b-a) > tolerance:
        midpoint = (a + b) / 2
        if utility(midpoint) > 0:
            a = midpoint
        else:
            b = midpoint
    
    return a


#Use bisection to find zero of f(h)

zero_bisection = bisection(0,1)
print(f"Zero of f(h): {zero_bisection}")


f_h = utility(hours)

fig, ax = plt.subplots()

ax.plot(hours, f_h)
ax.set_xlabel('Share of Hours Worked')
ax.set_ylabel('f(h)')
ax.set_title('Hours Worked vs. Utility')
ax.axhline(0, color='gray', linestyle='--')

ax.plot(zero_bisection, 0, 'bo')
ax.annotate('bisection',xy=(zero_bisection, 0))

plt.show()

