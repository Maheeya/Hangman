class CheckWord:

    def displayEmptyWord(self, p1):
        word = p1
        emptyWord = ''
        pos = 0
        while pos < len(word):
            emptyWord = emptyWord + '_'
            pos = pos + 1
        return emptyWord

    def CheckCorrect(self, p1, p2):
        word = p1
        letter = p2
        a = 0
        Correct = 0
        while a < len(word):
            if word[a:a + 1] == letter:
                Correct = 1
            elif letter != word[a:a + 1]:
                pass
            a = a + 1
        return Correct

    def addGuess(self, guess):
        guess = guess + 1
        return guess

    def checkAlreadyGuessed(self, p2, guess_list):
        history = guess_list
        pos = 0
        alreadyGuessed = False
        while pos < len(history):
            if history[pos] == p2:
                alreadyGuessed = True
            else:
                pass
            pos = pos + 1
        return alreadyGuessed

    def checkString(self, p1, p2):
        word = p1
        letter = p2
        pos = []
        a = 0
        while a < len(word):
            if word[a:a + 1] == letter:
                pos.append(1)
            elif letter != word[a:a + 1]:
                pos.append(0)
            a = a + 1
        return pos

    def fillInMissingLetters(self, p1, p2, guess_word):
        positions = self.checkString(p1, p2)
        pos = 0
        letter = p2
        update = list(guess_word)
        while pos < len(p1):
            if positions[pos] == 0:
                pass
            elif positions[pos] == 1:
                update[pos] = letter
            else:
                pass
            pos = pos + 1
        progressUpdate = ''.join(update)
        return progressUpdate


class DrawHangman:

    def hangmanStages(self, guesses):
        if guesses == 1:
            self.stage1()
        elif guesses == 2:
            self.stage2()
        elif guesses == 3:
            self.stage3()
        elif guesses == 4:
            self.stage4()
        elif guesses == 5:
            self.stage5()
        elif guesses == 6:
            self.stage6()
        else:
            self.stage7()

    def stage1(self):
        print('__________________')

    def stage2(self):
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('____________________')

    def stage3(self):
        print('__________________')
        print('|                 |')
        print('|                 |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('____________________')

    def stage4(self):
        print('__________________')
        print('|                 |')
        print('|                 |')
        print('|                 O')
        print('|')
        print('|')
        print('|')
        print('____________________')

    def stage5(self):
        print('__________________')
        print('|                 |')
        print('|                 |')
        print('|                 O')
        print('|                 |')
        print('|                 |')
        print('|')
        print('____________________')

    def stage6(self):
        print('__________________')
        print('|                 |')
        print('|                 |')
        print('|                 O')
        print('|                \|/')
        print('|                 |')
        print('|')
        print('____________________')

    def stage7(self):
        print('__________________')
        print('|                 |  ')
        print('|                 |  ')
        print('|                 O  ')
        print('|                \|/ ')
        print('|                 |  ')
        print('|                / \ ')
        print('____________________ ')