import random


def get_word():
    list_with_words = ["apple", "lion", "tiger", "football", "love", "basket", "planet", "paok"]

    choice = random.choice(list_with_words)
    return choice


def play(text):
    print("Find the hidden text: ")

    list_with_underline = []
    list_with_guesses = []
    for i in range(len(text)):
        list_with_underline.append("_")  # I create a single _ list, about the same size as the text characters

    total_guess = 8  # is the number of guesses a player can make,if i want to change the ,just i modify this variable
    hidden_text_found = False  # The variable flag show if the list "list_with_underline" has "underline",or the player has found the hidden text
    # when the player finds the word, the list has no lower bounds but the characters of text

    while total_guess > 0:

        print("--------------------------------------------------")

        guess = give_the_guess_of_player()

        while guess in list_with_guesses:  # check if the player has already made this choice
            print("You have already made this choice")
            guess = give_the_guess_of_player()
        list_with_guesses.append(guess)

        if guess in text:  # I check if the guess is in the hidden text
            print("CORRECT")
            print("You have ", total_guess, "attempts")
            indices = [i for i, a in enumerate(text) if
                       a == guess]  # create a list of positions where the letter is located

            i = 0
            while i < indices.__len__():
                list_with_underline[indices[i]] = guess
                i = i + 1
            # x = text.index(guess)
            # list_with_underline[x] = guess
        else:
            print("This letter is not in the hidden text")
            total_guess = total_guess - 1
            print("You have ", total_guess, "attempts")

        if "_" not in list_with_underline:  # if this list has none "-" then it means that the hidden text was found
            hidden_text_found = True;
            print("Bravo,you find the hidden text")

        if hidden_text_found:
            print(*list_with_underline)
            break;
        else:
            print(*list_with_underline)

    if hidden_text_found is False:
        print("You don't find the hidden text")
        print("The hidden text is ", text)


def give_the_guess_of_player():
    guess = input("Guess: ")
    guess_lower = guess.lower()  # I turn every character into a lowercase, because the hidden text is lowercase

    while True:
        if guess.__len__() == 1:  # i want only one character
            return guess_lower
        elif guess.__len__() == 0:  # I do not accept the enter option or space
            print("Please ,enter a character")
            guess = input("Guess: ")
            guess_lower = guess.lower()
        elif guess.__len__() > 1:  # i do not accept tow or more characters
            print("Please ,enter only one character")
            guess = input("Guess: ")
            guess_lower = guess.lower()


