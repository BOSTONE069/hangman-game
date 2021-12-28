import random
def hangman():
    word = random.choice(["pugger" , "thor" , "littlepugger" , "kenya" , "uganda" , "tanzania" , "nairobi" , "bostone" , "boston" , "software"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0: # this check for the length of the word within the word list provided
        main = ""
        missed = 0

        for letter in word: # this allows for the interation of the guessmade
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word: # this is for showing a win when the user has done a correct guess
            print(main)
            print("You won!")
            print("You won!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters: # this interates the guesses that the user in masking within the program
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word: # this condition calculates the turns that the user is making if he or she gets a wrong guess
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     0      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     0      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     0      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     0      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ 0      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ 0 /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ 0 /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ 0_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     0_|    ")
                print("    /|\     ")
                print("    / \     ")
                break


name = input("Enter your name") # this is the welcome input for the user
print("Welcome" , name)
print("----------------------")
print("Try to guess the word in less than 10 attempts")
hangman()
print()
