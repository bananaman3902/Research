# clean code > clever code is a principle about keeping code readable so other people can understand and maintain the code.

# The example is: to take a variable and double it if it is greater than 2 or halves it if it's less than or equal to 2
def calculate(a):
    # calculate doubles the given value if it is larger than 2 and halves the given value otherwise
    if a>2:
        return a*2
    else:
        return a/2
a=1
b=calculate(a)
print(b)
# This function determines takes a variable and either doubles or halves it depending on if it is greater than or less than 2. This example is clean and easier to read when broken into it's smaller parts.
