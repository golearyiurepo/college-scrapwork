import sys

low = 0
high = 1000

print("Think of a number from 1 to 1000 but don't tell me!")

guessing = True

while guessing:
    guess = (high + low) / 2
    user = raw_input("My guess is %d, is that right, too high or too low?:" %guess)
    if user == "right":
        print "Lucky me!"
        sys.exit()
    elif user == "too high":
        high = guess

    elif user == "too low":
        low = guess

    else:
        print "I don't understand"

