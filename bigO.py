# This program runs a single for loop with a arithmetic statment inside the loop.
# In order to generate a set of performances in time, this has a outerloop
# which runs ten times.
# n is set to 1 million so that the data can be in seconds. too less iterations
# produces micro seconds or even lesser than that.
# The time data is written into
import time
timedata = open('timedatafororderofn.csv','w') # create a csv file.
n = 1000000
sum = 0
prod = 1
for t in range(1,11): # to run ten times 
    t0 = time.process_time() # initial time
    print (t0)
    for i in range(n*t):
            prod = prod * i
    t1 = time.process_time() # final time after the loop
    timedata.write(str(t1-t0)+'\n') # time difference is written into csv file.
    print(t1-t0)
timedata.close()