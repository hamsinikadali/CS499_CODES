# Intel paper code column wise
# long multiplication

import time

# BigInteger class to handle large integers
class BigInteger:
    def __init__(self, num_str):
        # Storing digits in reverse order for efficient processing
        self.digits = [int(digit) for digit in reversed(num_str)]

    def __str__(self):
        # Reversing digits for clear string representation
        return ''.join(map(str, reversed(self.digits)))

    def __mul__(self, other):
        # Initializing result list with zeros to store intermediate results
        result = [0] * (len(self.digits) + len(other.digits))

        # using Nested loops for long multiplication
        for i in range(len(self.digits)):
            carry = 0
            for j in range(len(other.digits)):
                # Calculate product and update result
                product = self.digits[i] * other.digits[j] + result[i + j] + carry
                carry = product // 10
                result[i + j] = product % 10

            # Updating result with any remaining carry
            if carry:
                result[i + len(other.digits)] += carry

        # Eliminating leading zeros from the result
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Creating a BigInteger object with the reversed result
        return BigInteger(''.join(map(str, reversed(result))))

num1 = BigInteger("114701722186227725530857903247788731566117812708912875331083418612132595800326")
num2 = BigInteger("987643221443489764384795643298746382985736482736487365847365874387458437564327")

# Execution time
start_time = time.time()
product_result = num1 * num2
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")
print(product_result)
