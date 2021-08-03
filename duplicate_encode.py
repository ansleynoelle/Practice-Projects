def duplicate_encode(word):
    '''The goal of this exercise is to convert a string to a 
    new string where each character in the new string is "(" if that
    character appears only once in the original string, or ")" if that 
    character appears more than once in the original string. 
    Ignore capitalization when determining if a character is a duplicate.'''
    word = word.lower()
    newWord = ''
    for letter in word:
        counter= word.count(letter)
        if counter > 1:
            newWord = newWord + ')'
        else:
            newWord = newWord + '('
    return newWord
