#!/usr/bin/python


def weird(N):
    if N % 2 == 0 and 1 <= N <= 20 or N % 2 == 1 and 20 <= N:
        i = "Not Weird"
    else:
        i = "Weird"

    return i

def main():

    N = int(input("Enter a number: "))
    print(weird(N))



main()
