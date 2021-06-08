# Fibonnaci example:
# sum of two elements defines next element

# Setting up variables needed.
a, b = 0, 1

# Run inside while loop until the output is greater than or equal to 10.
while a < 10:
#while True:

    # Print the current value of A
    print(a)

    # A gets B (current value), B gets A+B (next value)
    a, b = b, a+b
