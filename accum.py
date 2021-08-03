def accum(s):
    word = ''
    counter= 0
    for letter in s:
        letterUP= letter.upper()
        letterLOW= letter.lower()
        multipleletter= letter * counter
        word = word + letterUP 
        for i in range(counter):
            word = word + letterLOW
        word = word + '-'
        counter = counter + 1
    word = word[:-1]
    return word
