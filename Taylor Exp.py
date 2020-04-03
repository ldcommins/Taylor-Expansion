# taylor expansion for cosine around 0
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + x^8/8! - ...

import numpy as np
import matplotlib.pyplot as plt

# Initialize range and number of terms
xrange = np.arange(-10, 10, .1)

print('\n\nThe Taylor Expansion of Cosine around 0 takes the form:\n'
      'cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + x^8/8! - ... \n'
      'The more terms you include in the expansion, \n'
      'the better approximation of cosx\n')
user_req_terms = int(input('How many terms of this expansion would you like me to plot?\n'))

# Create list of powers [2,4,6,...]
num_terms = []
for a in range(1, user_req_terms+1):
    num_terms.append(a*2)

# Factorial called in n_terms()
def factorial(power):
    multiple = 1
    for a in range(1, power + 1):
        multiple = multiple * a
    return multiple

# n_terms called in taylor()
def n_terms(a):
    y = 0
    for n in num_terms:
        if num_terms.index(n) % 2 == 0:
            y = y + a ** n / factorial(n)
        else:
            y = y - a ** n / factorial(n)
    return(y)

# Creates and plots taylor function
def taylor():
    taylor_func = []
    for a in xrange:
        z = 1 - n_terms(a)
        taylor_func.append(z)
    plt.plot(xrange, taylor_func, 'b+')

# Cosine for reference
def cos():
    cos_ref = []
    for a in xrange:
        z = np.cos(a)
        cos_ref.append(z)
    plt.plot(xrange, cos_ref, 'y')


taylor()
cos()
plt.ylim(-1, 1)
plt.show()
