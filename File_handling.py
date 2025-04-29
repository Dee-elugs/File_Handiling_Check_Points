
#Check Point

# 1. Begin by importing the necessary libraries, numpy.
# 2. Use the open() function to open csv file and assign the result to a variable.
# # 3. Use the numpy array to perform some basic statistical analysis on the data, such as finding the mean, median, and standard deviation of the loan amounts.

import numpy as np

with open("Loan.csv", "r") as f:
    data = f.read()
    print(data)

data = np.genfromtxt("Loan.csv", delimiter = ",", usecols=(8), filling_values=0)
print(data)

Loan = np.array(data)

mean = np.mean(Loan)
print(f"The mean is : {mean}")
print(Loan)

median = np.median(Loan)
print(f"The median is : {median}")

std = np.std(Loan)
print(f"The std is : {std}")


