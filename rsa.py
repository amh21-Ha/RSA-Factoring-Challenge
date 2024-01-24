#!/usr/bin/python3 
#rsa.py
# A program that can find the prime factors of a large number
# Usage: factors <number>
# where <number> is a large number to factor
# Output format: n=p*q
# where p and q are prime factors of n

import sys
import math

# Check if a file name is given as an argument
if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)


# Open the file for reading
try:
    file = open(sys.argv[1], "r")
except IOError:
    print("Error: cannot open file", sys.argv[1])
    sys.exit(2)
# Read the file line by line
for line in file:
    # Converting the argument value to integer n
    n = int(line.strip())

    # Find the prime factors of n using trial division
    # Start from 2 and go up to the square root of n
    # If a factor is found, divide n by it and repeat
    # Store the factors in a list
    
    factors = []
    i = 2
    p=n
    while i <= math.sqrt(p):
        if p % i == 0:
            factors.append(i)
            p //= i
        else:
            i += 1

    # If n is not 1, it is the last prime factor
    if p != 1:
        factors.append(p)

    # Print the output in the format n=p*q
    # If there are more than two factors, use parentheses
    if len(factors) == 2:
        print(f"{n}={factors[0]}*{factors[1]}")
    elif len(factors) > 2:
        print(f"{n}=({factors[0]}*{factors[1]})*{factors[2]}")
    else:
        print(f"{n} = {n}*{1} ")

# Close the file

file.close()
