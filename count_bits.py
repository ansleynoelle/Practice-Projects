def count_bits(n):
    binaryN= bin(n)
    counter = 0
    for x in binaryN:
        if x is '1':
            counter= counter+1
    return counter
    #counts "1" in binary number n
