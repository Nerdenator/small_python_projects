# Bagels, a deductive logic game

import random

print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say:\tThat means:")
print("\tPico\t\tOne digit is correct but in the wrong position")
print("\tFermi\t\tOne digit is correct and in the right position")
print("\tBagels\t\tNo digit is correct.")


def game():
    print("I have thought up a number.")
    # generate a number
    num = str(random.randrange(100, 999))
    rand = bool(random.getrandbits(1))
    if rand:
        n = list(num)
        n[0] = '0'
        num = ''.join(n)
    print("You have 10 guesses to get it.")
    i = 1
    while i is not 11:
        prompt = f"Guess #{i}: "
        guess = input(prompt)
        result = guess_checker(num, guess)
        if result == "You got it!":
            exit_menu()
        else:
            print(result)
        i += 1
    print(f"You ran out of guesses. The number was {num}.")


def guess_checker(num_str, guess_str):
    if len(guess_str) != 3:
        return "Enter a three-digit number."
    else:
        if guess_str == num_str:
            return 'You got it!'
        else:
            return_list = []
            length = len(guess_str)
            for i in range(len(guess_str)):
                compare = guess_str[i]
                if compare == num_str[i]:
                    return_list.append('Fermi')
                elif compare in num_str:
                    return_list.append('Pico')
            if len(return_list) == 0:
                return "Bagels"
            else:
                return_list.sort()
                return ' '.join(return_list)


def exit_menu():
    selection = input("Do you want to play again?")
    if selection in ['Yes', 'yes', 'y', 'Y']:
        game()
    else:
        exit()


game()
