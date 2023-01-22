"""This is an attempt to use a single element tuple as a constant"""
# Tuples as Constants - it works with a single element - could I use more?

# Declare a single element as a constant
pi_cdm = (3.14,)
print(type(pi_cdm))

# What is the value of the first element
print(pi_cdm[0])
print(type(pi_cdm[0]))

AMOUNT = 135 * pi_cdm[0]
print(AMOUNT)
