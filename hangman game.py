
import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'game', 'developer', 'code']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
        else:
            attempts -= 1
            print("Incorrect!")
            print("Attempts left:", attempts)
            print(display_word(word, guessed_letters))

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break
        elif attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()
