import random #to use random.randint 

# The Coin class simulates a coin that can be flipped.

class Coin:
    # The __init__method initializes the __sideup data attribute with 'Head'

    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, the sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
        return self.__sideup