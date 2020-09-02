import sys

def collatzProcessor(number):
    print(number)
    if number%2 == 0:
        even = number // 2
        print(str(even))
        return even
    else:
        odd = 3 * number + 1
        print(str(odd))
        return odd


def collatzInput():
    try:
        print("Enter a positive integer: ", end="")
        number = int(input())
        if number < 1:
            print("No negative numbers allowed");
            collatzInput()
        while number != 1:
            number = collatzProcessor(number)
    except ValueError:
        print("You did not enter a number.")
        collatzInput()

    askForMore()

def askForMore():
    try:
        while True:
            print("Would you like to enter a new number? [y] or [n]")
            response = input()
            if response == 'y':
                collatzInput()
            elif response == 'n':
                print("Goodbye")
                break;
            else:
                print("Only [y] and [n] are accepted")
    except KeyboardInterrupt:
        print("Goodbye")
        sys.exit()

collatzInput();


