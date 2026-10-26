#---PS 1: Static Partial Equilibrium Model---#

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Define known variables and parameters
gamma = 0.5
sigma = 3

# Create a 1D array of hours worked values from 0 to 1 with 100 increments
hours = np.linspace(0, 1, 100)

# Define function f(h)

def utility(hours):
    return (1-hours) - gamma*(hours**sigma)

f_h = utility(hours)

fig, ax = plt.subplots()

ax.plot(hours, f_h)
ax.set_xlabel('Share of Hours Worked')
ax.set_ylabel('f(h)')
ax.set_title('Hours Worked vs. Utility')

plt.show()