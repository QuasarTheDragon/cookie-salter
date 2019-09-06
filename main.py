import random
import string
import math


def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


cookie = ' '
complete = ' '
while True:
    cmd = input("> ")

    if 'start' in cmd:
        cookie = randomStringDigits(10)
        print(f"your cookie is: {cookie}")
    elif cmd == "salt":
        if cookie != ' ':
            salt = "TJv:>["
            length = len(salt)
            first = math.floor(length / 2)
            firstHalf = cookie[0:first]
            secondHalf = cookie[first:]
            complete = firstHalf + salt + secondHalf
            print(f"your salted cookie is: {complete}")
        else:
            print("You need to generate a salt first. Type 'start' to start.")
    elif 'stop' in cmd:
        break
    elif cmd == "unsalt":
        if cookie != ' ' and complete != ' ':
            complete = complete.replace(salt, '')
            print(f"The unsalted cookie is: {complete}")
            complete = ' '
        elif cookie != ' ' and complete == ' ':
            print("You need to salt your cookie first.")
        else:
            print("You need to generate your cookie first.")
    else:
        print("Sorry I don't understand")

