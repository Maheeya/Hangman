import Players

print('hi welcome to hangman')
p1 = input('Player 1 please type in a word: ')
display = Players.CheckWord()
guessWord = display.displayEmptyWord(p1)
print(guessWord)
guessList = []
guesses = 0

while guessWord != p1 and guesses < 7:

    p2 = input('Player 2 please guess a letter: ')
    guess = Players.CheckWord()
    check = guess.checkAlreadyGuessed(p2, guessList)
    result = guess.CheckCorrect(p1, p2)
    guessList.append(p2)

    if check:
        result = 2
    else:
        pass

    if result == 1:
        guessWord = guess.fillInMissingLetters(p1, p2, guessWord)
    elif result == 0:
        print("too bad, guess another letter: ")
        guesses = guess.addGuess(guesses)
        draw = Players.DrawHangman()
        draw.hangmanStages(guesses)
    else:
        print(' Already guessed this letter')

    print(guessWord)
