#!/usr/bin/env python3

def print_fibonacci(length): 
    sequence = []
    a,b = 0,1 # two "boxes" a and b that have values 0 and 1 to start us off
    #create a for loop to loop through the length
    for _ in range(length):
        sequence.append(a)#append at the end of the list the new value of a
        a,b = b,a+b
      #print the new values in the sequence
    print(sequence)


