def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretCopy = secretWord
    for letter in lettersGuessed:
        if letter in secretWord:
            secretCopy = secretCopy.replace(letter, "")
    if secretCopy == "":
        return True
    return False
