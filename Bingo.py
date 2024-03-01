import random
import os


# To display array
def displayArray(array, check="y"):
    # For clearing console screen
    if check == "y":
        os.system("cls" if os.name == "nt" else "clear")

    for i in range(1, 26):
        if i == 1:
            print("-" * 26)
        print(f"| {str(array[i-1]).zfill(2)} ", end="")
        if i % 5 == 0:
            print("|\n" + "-" * 26)

    time.sleep(1)


# To display timer
def displayTimer(num=3):
    os.system("cls" if os.name == "nt" else "clear")
    while num > 0:
        print("Computer's Turn")
        print(num)
        time.sleep(0.4)
        os.system("cls" if os.name == "nt" else "clear")
        num -= 1


# To convert a string to uppercase
def toUpper(string):
    return string.upper()


# Computer's functionality
def Computer(computerArray):
    # Assigning values to computer's array
    for i in range(25):
        num = random.randint(1, 25)
        while num in computerArray:
            num = random.randint(1, 25)
        computerArray[i] = num

    # Printing computer's array
    # displayArray(computerArray)


# Filling user's array
def User(userArray, name):
    # Clearing console screen
    os.system("cls" if os.name == "nt" else "clear")

    option = ""
    check = True
    num = 0
    while check:
        if num > 0:
            print("\nInvalid input.")
        print(f"\n<============== {name}'S BINGO ==============>")
        print("Press '1' to auto-fill your Bingo array.")
        print("Press '2' to fill your Bingo array yourself.")
        print("Press '3' to exit.")
        option = input()
        num += 1
        if option in ["1", "2", "3"]:
            check = False
            num = 0

    if option == "1":
        # For clearing console screen
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(25):
            num = random.randint(1, 25)
            while num < 1 or num > 25:
                num = random.randint(1, 25)
            while num in userArray:
                num = random.randint(1, 25)
            userArray[i] = num
    elif option == "2":
        # For clearing console screen
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(25):
            num = int(input("Enter value: "))

            while num < 1 or num > 25:
                print("\nInvalid input.")
                num = int(input("Enter again: "))
            while num in userArray:
                print("Enter again: ")
                num = int(input("Enter again: "))

            userArray[i] = num
            # For printing array
            displayArray(userArray)
    elif option == "3":
        exit(0)


# Check if a line is complete
def isLineComplete(arr):
    count = 0

    # Rows
    for i in range(5):
        if (
            (arr[i * 5] == -1 or arr[i * 5] == "XX")
            and (arr[i * 5 + 1] == -1 or arr[i * 5 + 1] == "XX")
            and (arr[i * 5 + 2] == -1 or arr[i * 5 + 2] == "XX")
            and (arr[i * 5 + 3] == -1 or arr[i * 5 + 3] == "XX")
            and (arr[i * 5 + 4] == -1 or arr[i * 5 + 4] == "XX")
        ):
            count += 1

    # Columns
    for i in range(5):
        if (
            (arr[i] == -1 or arr[i] == "XX")
            and (arr[i + 5] == -1 or arr[i + 5] == "XX")
            and (arr[i + 10] == -1 or arr[i + 10] == "XX")
            and (arr[i + 15] == -1 or arr[i + 15] == "XX")
            and (arr[i + 20] == -1 or arr[i + 20] == "XX")
        ):
            count += 1

    # Diagonal 1
    if (
        (arr[0] == -1 or arr[0] == "XX")
        and (arr[6] == -1 or arr[6] == "XX")
        and (arr[12] == -1 or arr[12] == "XX")
        and (arr[18] == -1 or arr[18] == "XX")
        and (arr[24] == -1 or arr[24] == "XX")
    ):
        count += 1

    # Diagonal 2
    if (
        (arr[4] == -1 or arr[4] == "XX")
        and (arr[8] == -1 or arr[8] == "XX")
        and (arr[12] == -1 or arr[12] == "XX")
        and (arr[16] == -1 or arr[16] == "XX")
        and (arr[20] == -1 or arr[20] == "XX")
    ):
        count += 1

    return count


# Main function
if __name__ == "__main__":
    import time

    name = input("Enter your name: ")
    name = toUpper(name)

    # User and Computer arrays
    userArray = [0] * 25
    computerArray = [0] * 25

    # Filling user and computer arrays
    User(userArray, name)
    Computer(computerArray)

    # Printing user and computer arrays
    displayArray(userArray)
    # displayArray(computerArray)

    # Initializing variables
    lineCount = 0
    computerCount = 0
    userCount = 0
    turnCount = 0

    while True:
        turnCount += 1

        # User's turn
        print(f"\n<=============== {name}'S TURN ===============>")
        num = int(input("Enter value: "))

        # Checking number in computer's array
        if num in computerArray:
            index = computerArray.index(num)
            computerArray[index] = "XX"
            computerCount += 1

        # Checking number in user's array
        if num in userArray:
            index = userArray.index(num)
            userArray[index] = "XX"
            userCount += 1

        # Printing arrays after each turn
        displayArray(userArray)
        # displayArray(computerArray, "n")

        # Checking lines completion
        lineCount = isLineComplete(userArray)
        if lineCount >= 5:
            print(f"\n<=============== {name} WINS ===============>")
            print(f"You took {turnCount} turns.")
            print(f"You completed {lineCount} lines.")
            break

        # Computer's turn
        displayTimer()
        num = random.choice(computerArray)

        # Checking number in user's array
        if num in userArray:
            index = userArray.index(num)
            userArray[index] = "XX"
            userCount += 1

        # Checking number in computer's array
        if num in computerArray:
            index = computerArray.index(num)
            computerArray[index] = "XX"
            computerCount += 1

        # Printing arrays after each turn
        displayArray(userArray)
        # displayArray(computerArray, "n")

        # Checking lines completion
        lineCount = isLineComplete(computerArray)
        if lineCount >= 5:
            print(f"\n<============= COMPUTER WINS =============>")
            print(f"You took {turnCount} turns.")
            print(f"You completed {userCount} lines.")
            break
