import random

class Guess:
    def __init__(self, letters, heart):
        self.heart = int(heart)
        self.letters = letters
        self.words = [["ananas"],["orange"],["strawberry"],["grape"],["coconut"],["banana"],["plum"],["apricot"]]


    def correct(self,words):
        print("thats correct")


    def notCorrect(self,words):
        print("thats not correct")


def check():
    guess = Guess(letters='letters', heart=3)
    comp = {}
    rnd = random.randrange(0, len(guess.words))
    gameWord = list(guess.words[rnd][0])
    guess.heart = 3
    user = {}


    for n in gameWord:
        if n in comp:
            comp[n] += 1
        else:
            comp[n] = 1


    while guess.heart > 0:
        userGuess = input("Hey, what's your guess ?")
        if userGuess in comp:
            if userGuess in user:
                if user[userGuess] < comp[userGuess]:
                    print("Hey, That's Correct !")
                    user[userGuess] += 1  
                    
                else:
                    user[userGuess] > comp[userGuess]
                    print("You should be careful!")
                    guess.heart -= 1
                    
                    
            else:
                print("Hey, That's Correct !")
                user[userGuess] = 1


            if user == comp:
                print("hey you won !")
                print(f"it was {gameWord} :) ")
                break

        else:
            print("You should be careful!")
            guess.heart -= 1




        if guess.heart == 0:
            print("Hey, dont worry and try again")

            




            print(user)


check()




