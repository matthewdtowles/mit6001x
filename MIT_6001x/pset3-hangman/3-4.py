def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long')
    lettersGuessed = []
    mistakesAllowed = 8
    availableLetters = getAvailableLetters(lettersGuessed)
    guessedWord = getGuessedWord(secretWord,lettersGuessed)
    while mistakesAllowed > 0:
        print('-----------')
        if guessedWord == secretWord:
            print('Congratulations, you won!')
            return
        print('You have ' + str(mistakesAllowed) + ' guesses left')
        print('Available letters: ' + str(availableLetters))
        guess = input('Please guess a letter: ').lower()
        availableLetters = availableLetters.replace(guess,'')
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ' + guessedWord)
        elif guess in secretWord:
            lettersGuessed.append(guess)
            guessedWord = getGuessedWord(secretWord,lettersGuessed)
            print('Good guess: ' + guessedWord)
        else:
            mistakesAllowed -= 1
            lettersGuessed.append(guess)
            guessedWord = getGuessedWord(secretWord,lettersGuessed)
            print('Oops! That letter is not in my word: ' + guessedWord)
    print('-----------')
    print('Sorry, you ran out of guesses. The word was '+str(secretWord))