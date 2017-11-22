def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handsize = 0
    for letter in hand:
        handsize += hand[letter]
    return handsize