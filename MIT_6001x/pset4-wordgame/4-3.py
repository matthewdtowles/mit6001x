def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    handCopy = hand.copy()
    for letter in word:
        if letter not in handCopy:
            return False
        handCopy[letter] -= 1
        if handCopy[letter] <= 0:
            try:
                del handCopy[letter]
            except:
                return False
    return True