
import random

def unique_letter(unique_letters, secret_word):
    '''This function keep track of unique letters in secret word'''
    k = []
    for i in secret_word:
        if i not in k:
            k.append(i)
            unique_letters +=1
    return unique_letters

def check_letter(letter, secret_word):
    "function to check if a letter is in the secret word"

    if letter in secret_word:
        return True
    else:
        return False

def update_dashes(letter, dashes, secret_word):
    "function to update the dashes with correctly guessed letters"
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            dashes[i] = letter
    return dashes


def play_round(secret_word, dashes, guesses, warning, used_letters):
    "function to handle a single round of the game"
    global letter
    # show remaining letters
    print("Available letters: ", end="")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in used_letters:
            print(letter, end=" ")
    print()
    # get letter from user

    letter = input("\nPlease guess a letter: ").lower()
    vowels = 'aeiou'
    # warning if letter has already been used or entered character is not a letter
    if letter in used_letters:
        if warning == 0:
            print("Oops! You've already quessed that letter.")
            if letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
        else:
            print("Oops! You've already quessed that letter.")
            warning -= 1
    elif not "a"<= letter <= "z" :
        if warning == 0:
            print("***Please select a letter***")
            guesses -= 1
        else:
            print("***Please select a letter***")
            warning -= 1
    elif len(letter)> 1:
        print("***Please enter one letter at a time***")


    # check if letter is in the word
    elif check_letter(letter, secret_word,):
        print("Good guess!")
        dashes = update_dashes(letter, dashes, secret_word)
    else:
        print("Oops! That letter is not in my word:")
        if letter in vowels:
            guesses -= 2
        else:
            guesses -= 1
    #printing Hangman
    if guesses == 5:
        print("_______________")
        print("       O      ")
    elif guesses == 4:
        print("_______________")
        print("       O      ")
        print("       I      ")
    elif guesses == 3:
        print("_______________")
        print("       O      ")
        print("       I      ")
        print("      / \     ")
    elif guesses == 2:
        print("_______________")
        print("      \O/      ")
        print("       I       ")
        print("      / \      ")
    elif guesses == 1:
        print("_________________")
        print("      \O/___      ")
        print("       I       ")
        print("      / \      ")
    elif guesses == 0:
        print("_________________")
        print("       O___|      ")
        print("      /I\       ")
        print("      / \      ")
    # print remaining guesses and warnings
    print("You have", warning, "warnings left.")
    print("You have", guesses, "guesses left.")
    return dashes, guesses, warning, used_letters


def scores(guesses, unique_letters, secret_word, name):
    "fuction to calculate score and maintain the record of high score"
    with open("highscore.txt", "r+") as hs:
        guesse_remaining = guesses
        score = guesse_remaining * unique_letter(unique_letters, secret_word)
        print("\n*****************\nYour Score:", score)
        reading_score = hs.read().split(",")
        highest_score = reading_score[0]
        high_scorer = reading_score[1]
        h = int(highest_score)
        if score >= h:
            h = score
            high_scorer = name
            print("Hurray!! you set a new high score\n")
            with open("highscore.txt", "w") as f:
                f.write(str(h) + "," + high_scorer)
        print("Highest Score:", h, "by", high_scorer)
        return score, h, highest_score

def play_hangman():
    "main function to run the game"
    name = input("\n Your name? ")
    global letter
    # welcome message
    print("Welcome", name, '''to the game Hangman!
    Instructions:
    1-You are given 3 warnings and 6 guesses.
    2-Guess one letter at a time.
    3-On entering already guessed letter or any character other
    then letter you will lose one warning and if you have no warnings
    left you will lose a guess.
    4-On guessing wrong consonant you will lose one guess and on 
    guessing wrong vowel you will lose two guesses.''')
    print("Loading word list from file...")
    # list of words to choose from
    with open("words.txt","r")as file:
        a=file.read().split()
        secret_word=random.choice(a)
    #words = ["python", "programming", "code", "computer", "science"]
    print(len(a), "words loaded.")
    # choose a random word
    #word = random.choice(words)
    # create list of dashes for hidden word
    dashes = ["_" for letter in secret_word]
    # number of guesses
    guesses = 6
    # number of warnings
    warning = 3
    #unique letters
    unique_letters = 0
    # used letters
    used_letters = []
    # print the length of the word
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    # game loop
    while "_" in dashes and guesses > 0:
        print(dashes)
        dashes, guesses, warning, used_letters = play_round(secret_word, dashes, guesses, warning, used_letters)
        used_letters.append(letter)
    # game over message
    if "_" not in dashes:
        print("\nCongratulations! You guessed the word: ", secret_word)
        scores(guesses, unique_letters, secret_word, name)
        play_again = input("Want to Play again?\nPress 'Y' for yes or press Enter for exit: ").upper()
        if play_again == "Y":
            play_hangman()
    elif guesses <= 0:
        print("\nSorry, you ran out of guesses or warnings.\nThe word was", '"'+ secret_word +'"')
        scores(guesses, unique_letters, secret_word, name)
        play_again = input("Want to Play again?\nPress 'Y' for yes or press Enter for exit: ").upper()
        if play_again == "Y":
            play_hangman()
