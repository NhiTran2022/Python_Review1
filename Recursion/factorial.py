"""
    Calculate the factorial of a number
    If n = 0 then factorial(n) = 1
    if n > 0 then factorial(n) = n * factorial(n-1)
"""

# This program uses recursion to calculate 
# the factorial of a number.

def main():
    # The factorial function used recursion to 
    # calculate the factorial of its argument,
    # which is assumed to be nonnegative.
    def factorial(num):
        if num == 0:
            return 1

        else:
            return num * factorial(num - 1)

    # Get a number from the user.
    number = int(input("Enter a nonnegative number: "))

    # Get the factorial number.
    fact = factorial(number)

    # Display the factorial.
    print("The factorial of", number, "is", fact)
main()