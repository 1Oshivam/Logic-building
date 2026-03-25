#include <stdio.h>

int main() {
    int num1, num2, sum;

    // Taking input from user
    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    // Adding numbers
    sum = num1 + num2;

    // Display result
    printf("Sum = %d\n", sum);

    return 0;
}