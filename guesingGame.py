import random

SpecialNumber = random.randrange(1, 100)
print('''======================================
 WELCOME TO A SIMPLE GUESSING GAME \n
 --------------------------------------\n
rules: you have 5 guesses try and predict our number\n
====================================================\n''')
trials = 5


def check(var):
    if var > SpecialNumber:
        print("your guess is higher, go low")
    elif var < SpecialNumber:
        print("value quoted is low! ,go high")
    elif var == SpecialNumber:
        print(
            f"good guess {SpecialNumber} is the right answer\n you have won nothing but you got good prediction skills")
    return var


while trials > 0:
    userInput = int(input("enter your guess here: "))
    trials -= 1
    check(userInput)
    if trials == 1:
        print("this is your last chance, Don't waste it\n")

    else:
        if userInput == SpecialNumber:
            break
        print(f" you have: {trials} remaining guesses\n")

else:
    print('SORRY YOU HAVE EXHAUSTED YOUR TRIAL AND DID NOT GET ANY CORRECT.\n and by the way the number was ',
          SpecialNumber, "\n BYE! BYE!")
