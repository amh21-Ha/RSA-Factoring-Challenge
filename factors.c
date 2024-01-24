// factors.c
// A program that factorizes natural numbers into a product of two smaller numbers

#include <stdio.h>
#include <stdlib.h>

// A function that prints a factorization of a number n
void print_factorization(unsigned long long n) {
  // Find the smallest divisor of n
  unsigned long long divisor = 2;
  while (divisor * divisor <= n) {
    if (n % divisor == 0) {
      // Print the factorization
      printf("%llu=%llu*%llu\n", n, divisor, n / divisor);
      return;
    }
    divisor++;
  }
  // If n is prime, print n=1*n
  printf("%llu=1*%llu\n", n, n);
}

// A function that reads a file and factorizes each number in it
void factorize_file(char *filename) {
  // Open the file
  FILE *file = fopen(filename, "r");
  if (file == NULL) {
    printf("Error: cannot open file %s\n", filename);
    exit(1);
  }
  // Read each number and factorize it
  unsigned long long number;
  while (fscanf(file, "%llu", &number) == 1) {
    print_factorization(number);
  }
  // Close the file
  fclose(file);
}

// The main function that takes a file name as an argument
int main(int argc, char *argv[]) {
  // Check if the argument is given
  if (argc != 2) {
    printf("Usage: factors <file>\n");
    exit(1);
  }
  // Factorize the file
  factorize_file(argv[1]);
  return 0;
}
