"""
    this function actually has two base cases: when n is equal to 0,
and when n is equal to 1. In either case, the function returns a value
without making a recursive call.
"""
def main():
    # The fib function returns the nth number
    # in the Fibonacci series.
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
    print("The first 10 numbers in the")
    print("Fibonacci series are:")

    for number in range(1,11):
        print(fib(number))

# Call the main function
main()