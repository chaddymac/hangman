import random


def asterisker(random_word, guesses):
    result = ""
    for letter in random_word:
        if letter in guesses:
            print(letter, end="")
        else:
            print("*", end="")
    print()
    return result


# list of words
# TODO: Get large list of words from somewhere
hangman_words = ["target", "walmart", "Dollar General", "Kroger", "CVS"]

# chooses a random word from the list
random_word = random.choice(hangman_words).lower()

# length of the random word
word_len = len(random_word)

# Print statement for the game to begin
letter_list = list(random_word)
guesses = []

len_ofword = "The word is {} letters long.".format(word_len)
print(len_ofword)
guess_letter = input(" Guess a letter ").lower()
done = False

# Checking if the letter is in the word
while not done:
    if guess_letter in random_word:
        print("That letter is correct")
    else:
        print("nope guess again!")
    for guess in guesses:
        if guess in letter_list:
            done = True
    guesses.append(guess_letter)
    asterisker(random_word, guesses)
    guess_letter = input(" Guess a letter ")


# TODO: Print partially filled out word
