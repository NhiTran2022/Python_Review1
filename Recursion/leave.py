
'''
This program is to traverse through a tree
and get the total number of leaves by
recursion
'''
import random
totLeaves = 0
def leaves(bcount):
        global totLeaves
        currentLeaves = random.randint(0,50)
        print("In Branch : ", bcount)
        print("No Of Leaves : ", currentLeaves)
        totLeaves += currentLeaves
        print("Cur. Total :", totLeaves)
        bcount = random.randint(0,2)
        print("This has ",bcount, " branches")
        if bcount == 0:
                return totLeaves
        else:
                for i in range(1,bcount+1):
                        leaves(i)
                return totLeaves
totalLeaves = leaves(1)
print(" Total No of Leaves :", totalLeaves)
