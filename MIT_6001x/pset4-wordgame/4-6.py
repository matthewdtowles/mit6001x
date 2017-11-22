def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    thisHand = ''
    while True:
        control = input("Enter 'n' for new hand. Enter 'r' to replay last hand. Enter 'e' to exit.")
        if control not in 'nre':
            print("Invalid entry.")
        else:
            if control == 'n':
                thisHand = dealHand(HAND_SIZE)
                playHand(thisHand.copy(), wordList, HAND_SIZE)
            elif control == 'r' and thisHand != '':
                playHand(thisHand.copy(), wordList, HAND_SIZE)
            elif control == 'r' and thisHand == '':
                print("You have not played a hand yet.")
            else:
                break
            print()