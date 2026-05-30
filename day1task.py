import random
secret=random.randint(1,100)
while True:
    guess=int(input("guess the number"))
    if guess > secret:
        print("to high")
    elif guess < secret:
        print("'to low")
    else:
        print("çorrect ypur geussed")
        break