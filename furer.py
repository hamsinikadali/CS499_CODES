def furer_multiply(x, y):
    
    #checking size of number
    if x < 2**64 or y < 2**64:
        return x * y
        
    #Determining the size of the numbers and dividing them into halves
    m = min(x.bit_length(), y.bit_length())
    m2 = m // 2

    # Creating a mask to extract the lower m/2 bits
    mask = (1 << m2) - 1

    # Spliting the numbers into four parts
    a = x >> m2
    b = x & mask
    c = y >> m2
    d = y & mask

    # Recursively computing multiplications
    ac = furer_multiply(a, c)
    bd = furer_multiply(b, d)
    ad_bc = furer_multiply(a + b, c + d) - ac - bd

    result = (ac << (2 * m2)) + (ad_bc << m2) + bd
    return result


# Example:
x = 114701722186227725530857903247788731566117812708912875331083418612132595800326
y = 987643221443489764384795643298746382985736482736487365847365874387458437564327
result = furer_multiply(x, y)
print(result)
