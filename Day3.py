#!/usr/bin/python

# This function will determine whether the N variable will meet the specifications of the task. Laziness 
# has prevented me from typing them all in here.

def weird(N):
    if N % 2 == 0 and 1 <= N <= 20 or N % 2 == 1 and 20 <= N:
        i = "Not Weird"
    else:
        i = "Weird"

    return i

# Get N from the user. Send it off to weird() for processing and await a reply.

def main():

    N = int(input("Enter a number: "))
    print(weird(N))



main()
