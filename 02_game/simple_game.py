import random


def digits():
        digits = [str(num) for num in range(10)]
        random.shuffle(digits)
        solution = digits[:3]
        return solution
print(digits())


def get_user_input():
    #get ther user input numbers
    return list(input("What is your guess?\n"))


def check_user_input(user_input , game_code):
    if user_input == game_code:
        return "Game Win"

    result = []

    for index,number in enumerate(user_input):
        if number == game_code[index]:
            result.append("Match")
        elif number in game_code:
            result.append("Close")

    if result == []:
        return "Nope"
    else:
        return result


print("Game Start")
code = digits()
result = []

while result != "Game Win":
    user_guess= get_user_input()
    result = check_user_input(user_guess,code)

    print("Here is the result of your guess:")

    if result == "Game Won":
        print("Game Won!!")
    else:
        for clue in result:
            print(clue)
