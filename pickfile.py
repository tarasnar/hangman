import random
import re

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

def menu():
    def hangman():
                words = ['python', 'java', 'kotlin', 'javascript']
                word = random.choice(words)
                secret = list(len(word) * "-")
                letters = list()
                correcto = set()
                attempts = 8
                while attempts > 0:
                    if set(word) == correcto:
                        print(f"You guessed the word {word}\nYou survived!")
                        break
                    print()
                    print("".join(secret))
                    guess = input("Input a letter: ")
                    if len(guess) > 1:
                        print("You should input a single letter")
                    elif guess.islower() == False or has_cyrillic(guess) == True:
                        print("Please enter a lowercase English letter")
                        continue
                    elif guess not in word:
                        if guess in letters:
                            print("You've already guessed this letter")
                        else:
                            print("That letter doesn't appear in the word")
                            letters.extend(guess)
                            attempts -= 1
                    elif guess in word:
                        if guess in letters:
                            print("You've already guessed this letter")
                        else:
                            letters.extend(guess)
                            correcto.add(guess)
                            n = word.count(guess)
                            word_position = word.find(guess)
                            secret[word_position] = guess
                            if n > 1:
                                correcto.add(guess)
                                word_position_two = word.find(guess, word_position + 1)
                                secret[word_position_two] = guess
                else:
                    print("You lost!")
    menu_inpt = (input('Type "play" to play the game, "exit" to quit: '))
    counter = 0
    while counter != 1:
        if menu_inpt == "play":
            counter += 1
            return hangman()
        elif menu_inpt == "exit":
            counter += 1
            break
        else:
            menu()


print("H A N G M A N")
menu()
