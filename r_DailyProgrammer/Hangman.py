import random

from definitions import ENABLE1 as WORDLIST


class Hangman:
    def __init__(self):
        self.man = ['0', '/', '|', '\\', '/', '\\']
        self.incorrect_ans = list()
        self.word = ''
        self.chosen_letters = list()
        self.continue_playing = True

    def choose_word(self):
        self.word = random.choice(WORDLIST).lower()

    def clue(self):
        def _clue(letter):
            if letter in self.chosen_letters:
                return letter
            else:
                return "_"
        return ' '.join([_clue(letter) for letter in self.word])

    def board(self):
        man = list()
        try:
            man += self.man[:len(self.incorrect_ans)]
        except IndexError:
            pass

        man += [' ' for i in range(6-len(self.incorrect_ans))]
        return f"""
Wrong Answers:
{', '.join(self.incorrect_ans)}
      _________
     |         |
     |         {man[0]}
     |        {man[1]}{man[2]}{man[3]}
     |        {man[4]} {man[5]}
     |
   __|__
   {self.clue()}
"""

    def play(self):
        while self.continue_playing:
            self.incorrect_ans = list()
            self.chosen_letters = list()
            self.choose_word()
            while True:
                # call('clear' if os.name =='posix' else 'cls')
                print(self.board())

                if len(self.incorrect_ans) == 6:
                    print(f"You lose!\nThe word was '{self.word}'")
                    break

                if '_' not in self.clue():
                    print("You win!")
                    break

                while True:
                    print("Please pick a letter:")
                    letter = input().lower()[0]
                    if len(letter) == 0:
                        print('Please select a letter.')
                    elif letter in self.chosen_letters:
                        print('Letter already selected.')
                    else:
                        break

                self.chosen_letters.append(letter)
                if letter not in self.word:
                    self.incorrect_ans.append(letter)

            print('Would you like to play again? (Yes/No)')
            if input().lower()[0] != 'y':
                self.continue_playing = False