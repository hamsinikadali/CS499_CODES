import numpy as np
import time

class GFG:
    a, b = 0, 0
    def schonhage_strassen_multiplication():
        a_digits = GFG.get_digits(GFG.a)
        b_digits = GFG.get_digits(GFG.b)

        result_fft = np.fft.fft(
            a_digits + [0] * (len(a_digits) - 1)) * np.fft.fft(b_digits + [0] * (len(b_digits) - 1))
        result = np.fft.ifft(result_fft).real.round().astype(int)

        # Handle carries
        for i in range(len(result) - 1, 0, -1):
            result[i - 1] += result[i] // 10
            result[i] %= 10

        product = int(''.join(map(str, result)))
        print("\nThe Product is:", product)

    def get_digits(num):
        # Converting the number to a list of digits
        return [int(digit) for digit in str(num)]


if __name__ == "__main__":
    GFG.a = 114701722186227725530857903247788731566117812708912875331083418612132595800326
    GFG.b = 987643221443489764384795643298746382985736482736487365847365874387458437564327
    start_time = time.time()
    GFG.schonhage_strassen_multiplication()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time} seconds")

