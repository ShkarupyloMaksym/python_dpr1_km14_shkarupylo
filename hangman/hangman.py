# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

lower = ''
for i in range(10):
    lower += '_'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    return set(secret_word) & set(letters_guessed) == set(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    returning_str = ''
    right_letters = list(set(secret_word) and set(letters_guessed))
    for i in secret_word:
        if i in right_letters:
            returning_str += i
        else:
            returning_str += '_ '
    return returning_str


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    not_guessed = ''
    for i in string.ascii_lowercase:
        if not i in letters_guessed:
            not_guessed += i
    return not_guessed


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    global lower
    print('Welcome to the game Hangman!\nI am thinking of a word that is {word_len} letters long.\n{lower}'.format(
        word_len=len(secret_word), lower=lower))
    letters_guessed = []
    guesses_remaining = 6
    markup = 3
    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        print('You have {number_life} guesses left. Available letters: {text}'.format(
            number_life=guesses_remaining, text=get_available_letters(letters_guessed)))
        guesses_letter = input('Please guess a letter:').lower()
        if guesses_letter.isalpha() and len(guesses_letter) == 1:
            if guesses_letter in letters_guessed:
                if markup > 0:
                    markup -= 1
                    print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(
                        markup, get_guessed_word(secret_word, letters_guessed)))
                    if markup == 0:
                        print("It was your last warning! The next mistake will decrease your number of guesses")
                else:
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "
                          "{}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                letters_guessed.append(guesses_letter)
                if guesses_letter in secret_word:
                    print('Good guess: {}'.format(get_guessed_word(secret_word, letters_guessed)))
                else:
                    print('Oops! That letter is not in my word: {}'.format(
                        get_guessed_word(secret_word, letters_guessed)))
                    if guesses_letter in 'aeiou':
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
        else:
            if markup > 0:
                markup -= 1
                print("Oops! That is not a valid letter. You have {} warnings left: {}".format(
                    markup, get_guessed_word(secret_word, letters_guessed)))
                if markup == 0:
                    print("It was your last warning! The next mistake will decrease your number of guesses")
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess "
                      "{}".format(guesses_remaining, get_guessed_word(secret_word, letters_guessed)))
        print(lower)
    if guesses_remaining <= 0:
        print('Sorry, you ran out of guesses.The word was {}'.format(secret_word))
    else:
        print('Congratulations, you won!\nYour total score for this game is: {}'.format(
            guesses_remaining * len(set(secret_word))))
    # When you've completed your hangman function, scroll down to the bottom


# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    my_word = ''.join(my_word.split())
    if len(my_word) == len(other_word):
        for i in my_word:
            if i != '_':
                my_word_splited = my_word.split(i)
                other_word_splited = other_word.split(i)
                if len(my_word_splited) != len(other_word_splited):
                    return False
                else:
                    for j in range(len(my_word_splited)):
                        if len(my_word_splited[j]) != len(other_word_splited[j]):
                            return False
    else:
        return False
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    global wordlist
    for i in wordlist:
        if match_with_gaps(my_word, i):
            print(i, end=' ')
    print()


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    global lower
    print(
        'Welcome to the game Hangman with hints!\nI am thinking of a word that is {word_len} letters long.\n{lower}'.format(
            word_len=len(secret_word), lower=lower))
    letters_guessed = []
    guesses_remaining = 6
    markup = 3
    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        print('You have {number_life} guesses left. Available letters: {text}'.format(
            number_life=guesses_remaining, text=get_available_letters(letters_guessed)))
        guesses_letter = input('Please guess a letter:').lower()
        if guesses_letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif guesses_letter.isalpha() and len(guesses_letter) == 1:
            if guesses_letter in letters_guessed:
                if markup > 0:
                    markup -= 1
                    print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(
                        markup, get_guessed_word(secret_word, letters_guessed)))
                    if markup == 0:
                        print("It was your last warning! The next mistake will decrease your number of guesses")
                else:
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "
                          "{}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                letters_guessed.append(guesses_letter)
                if guesses_letter in secret_word:
                    print('Good guess: {}'.format(get_guessed_word(secret_word, letters_guessed)))
                else:
                    print('Oops! That letter is not in my word: {}'.format(
                        get_guessed_word(secret_word, letters_guessed)))
                    if guesses_letter in 'aeiou':
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
        else:
            if markup > 0:
                markup -= 1
                print("Oops! That is not a valid letter. You have {} warnings left: {}".format(
                    markup, get_guessed_word(secret_word, letters_guessed)))
                if markup == 0:
                    print("It was your last warning! The next mistake will decrease your number of guesses")
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess "
                      "{}".format(guesses_remaining, get_guessed_word(secret_word, letters_guessed)))
        print(lower)
    if guesses_remaining <= 0:
        print('Sorry, you ran out of guesses.The word was {}'.format(secret_word))
    else:
        print('Congratulations, you won!\nYour total score for this game is: {}'.format(
            guesses_remaining * len(set(secret_word))))
    pass


if __name__ == "__main__":
    pass

print("\nHi user, you are playing in a very interesting game!\nIf you want to play common hangman press'1'\nIf you "
      "want to play with hints press '2'")
while True:
    n = input('1 or 2: ')
    if n == '1' or n == '2':
        break
if n == 1:
    secret_word = choose_word(wordlist)
    hangman(secret_word)
else:
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
