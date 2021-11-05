def first_menu():
    print("The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:\n"
          "1. If n is even, the next number n is n / 2.\n"
          "2. If n is odd, the next number n is n * 3 + 1\n"
          "3. If n is 1, stop. Otherwise, repeat.\n")
    choice()

def choice():
    numchoice = input("Enter a starting number (greater than 0) or QUIT: ")
    if numchoice.lower() == 'quit':
        exit()
    elif int(numchoice) < 1:
        print("Invalid number. ")
        choice()
    else:
        print(numchoice)
        collatz(numchoice)

def collatz(number):
    number = int(number)
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
        elif number % 2 == 1:
            number = int(number * 3 + 1)
        print(number)

def main():
    first_menu()

if __name__ == '__main__':
    main()