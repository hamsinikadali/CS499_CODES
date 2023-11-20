#include <stdio.h>
#include <string.h>
#include <time.h>


// Function to remove leading zeros from a string representing a number
void removeLeadingZero(char num[]) {
    int n = strlen(num) - 1;
    int i;
    for (i = 0; i < strlen(num) - 1; ++i) {
        if (num[i] != '0') {
            n = i;
            break;
        }
    }

    // Shifting the non-zero part to the beginning
    memmove(num, num + n, strlen(num) - n);
    num[strlen(num) - n] = '\0';
}

// Function to multiply two large numbers represented as strings
char* multiply(char num1[], char num2[], char result[]) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);

    // Initializing the result array with zeros
    for (int i = 0; i < len1 + len2; ++i) {
        result[i] = '0';
    }
    result[len1 + len2] = '\0';

    // Multiplying each digit and add to the result
    for (int i = len1 - 1; i >= 0; --i) {
        int carry = 0;
        for (int j = len2 - 1; j >= 0; --j) {
            int temp = (num1[i] - '0') * (num2[j] - '0') + (result[i + j + 1] - '0') + carry;
            result[i + j + 1] = temp % 10 + '0';
            carry = temp / 10;
        }
        result[i] += carry; // Add the carry to the current digit
    }

    // Removing leading zeros from the result
    removeLeadingZero(result);

    return result;
}

int main() {
    char num1[] = "114701722186227725530857903247788731566117812708912875331083418612132595800326";
    char num2[] = "987643221443489764384795643298746382985736482736487365847365874387458437564327";
    char result[1000];

    clock_t start_time = clock(); // Record the start time

    multiply(num1, num2, result);

    clock_t end_time = clock(); // Record the end time
    
    multiply(num1, num2, result);

    printf("The product of %s and %s is: %s\n", num1, num2, result);
    
    double execution_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    printf("Execution Time: %f seconds\n", execution_time);

    return 0;
}
