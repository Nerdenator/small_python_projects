from random import randrange

STARTING_BALANCE = 5000
CHO_OR_HAN = ['cho', 'han']


def main():
    intro()
    wager = betting_amount()
    print("The dealer swirls the cup and you hear the rattle of the dice.\n"
          "The dealer slams the cup on the floor, still covering the dice and asks you for your bet.")
    result, selection, num1, num2 = cho_or_han()
    print(f"\t{num1} - {num2}")
    if result == selection:
        fee = int(wager) // 10
        print(f"You won! You take {wager} mon.")
        print(f"The house takes a {fee} fee.")
    else:
        purse = STARTING_BALANCE - int(wager)
        print(f"You lost! Your purse is now {purse}")
        if purse <= 0:
            print(f"You ran out of money! Prepare for the local Yakuza to break your shins")



def intro():
    print("In this traditional Japanese dice game, two dice are rolled in a bamboo cup by the dealer "
          "sitting on the floor. The player must guess if the dice total to an even (cho) or an odd (han) "
          "number.")


def betting_amount():
    print(f"You have {STARTING_BALANCE} mon. How much do you bet? (or QUIT)")
    amount = input("> ")
    if int(amount) <= 0:
        betting_amount()
    return amount


def cho_or_han():
    selection = input("\tCHO (even) or HAN (odd)? >").lower()
    if selection not in CHO_OR_HAN:
        cho_or_han()
    num1 = randrange(1, 7)
    num2 = randrange(1, 7)
    sum_of_nums = num1 + num2
    print("The dealer lifts the cup to reveal: ")
    if sum_of_nums % 2 == 0:
        return 'cho', selection, num1, num2
    else:
        return 'han', selection, num1, num2


if __name__ == '__main__':
    main()
