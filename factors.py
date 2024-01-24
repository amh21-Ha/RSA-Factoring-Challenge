#!/usr/bin/python3

'''# factors.py
# A program that can factorize numbers from a file
# Usage: factors <file>
# where <file> is a file containing natural numbers to factor
# One number per line
# Output format: n=p*q
# one factorization per line
# p and q don’t have to be prime numbers
'''
import sys

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
    # Strip the newline character and convert to integer
    n = int(line.strip())
    # Find a factor of n by trying from 2 to sqrt(n)
    for p in range(2, int(n**0.5) + 1):
        # If p divides n, then q = n / p is another factor
        if n % p == 0:
            q = n // p
            # Print the factorization
            print(f"{n}={p}*{q}")
            # Break the loop
            break
    else:
        # If no factor is found, n is prime
        print(f"{n} is prime")

# Close the file
file.close()
