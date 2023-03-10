"""
    uses recursion to sum a range of items in a list. The function takes the
    following arguments: a list that contains the range of elements to be
    summed, an integer specifying the index of the starting item in the range,
    and an integer specifying the index of the ending item in the range.
"""

def main():
    # The range_sum function returns the sum of a 
    # specified range of items in num_list. The start 
    # parameter specifies the index of the starting 
    # item. The end parameter specifies the index of the 
    # ending item.
    def range_sum(num_list, start, end):
        if start > end:
            return 0
        else:
            return num_list[start] + range_sum(num_list, start + 1, end)

    # Create a list of numbers
    numbers = [1,2,3,4,5,6,7,8,9]

    # Get the sum of the items at indexes 2 through 5
    my_sum = range_sum(numbers, 2, 5)

    # Display the sum
    print("The sum of items 2 through 5 is", my_sum)
# Call the main function
main()