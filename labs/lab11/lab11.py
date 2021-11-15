"""
Name: <Sydney Wertz>
<lab11>.py
"""

from random import randint

def words(in_file):
    file = open(in_file, "r")
    return file.readlines()

def secret_word(word_list):
    word = randint(0, (len(word_list))-1)
    word = word_list[word]
    return word.strip()

def fill(word, letter_list):
    secret = ["_"] * len(word)

    for letter in letter_list:
        for i in range(len(word)):
            if letter in word[i]:
                secret[i] = letter
    return "".join(secret)

def word_check(word, letter_list):
    guessed_word = fill(word, letter_list)
    if guessed_word == word:
        return True
    else:
        return False

def play():
    play_word = words("hangman_words.txt")
    random_word = secret_word(play_word)

    incorrect = 0
    guesses = []
    still_playing = True

    while (still_playing == True) and (incorrect < 7):
        display = fill(random_word, guesses)
        print(display)
        print(guesses)

        user_letter = input("Enter a letter: ")
        guesses.append(user_letter)

        display = fill(random_word, guesses)
        running = word_check(random_word, guesses)

        if user_letter not in random_word:
            incorrect += 1
            print("Incorrect:", incorrect)

        if running == True:
            print(display)
            print("Word guessed correctly, game over")
            still_playing = False

def main():
    play()
    pass

main()
