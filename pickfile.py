"""import random

def choose_random_word():
    words=[]
    with open('sowpods.txt', 'r') as file:
        line = file.readline()
        while line:
            words.append(line.replace("\n","".strip()))
            line = file.readline()
    choice=words[random.randint(0,len(words)-1)]
    return choice


print("Welcome to Hangman!")
secret_word=choose_random_word()
dashes=list(secret_word)
display_list=[]
for i in dashes:
    display_list.append("_")
count=len(secret_word)
guesses=0
letter = 0
used_list=[]
while count != 0 and letter != "exit":
    print(" ".join(display_list))
    letter=input("Guess your letter: ")

    if letter.upper() in used_list:
        print("Oops! Already guessed that letter.")
    else:
        for i in range(0,len(secret_word)):
            if letter.upper() == secret_word[i]:
                display_list[i]=letter.upper()
                count -= 1
        guesses +=1
    used_list.append(letter.upper())

if letter == "exit":
    print("Thanks!")
else:
    print(" ".join(display_list))
    print("Good job! You figured that the word is "+secret_word+" after guessing %s letters!" % guesses)"""

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
