# clean code > clever code is a principle about keeping code readable so other people can understand and maintain the code.

# The example is: to take a variable and double it if it is greater than 2 or halves it if it's less than or equal to 2
a=1
b=a*2 if a>2 else a/2
print(b)
# This function takes a variable and either doubles or halves it depending on if it is greater than or less than or equal to 2. This example is overcomplicated as while it is now all on one line and doesn't require an extra function, but it is much harder to read or edit.
