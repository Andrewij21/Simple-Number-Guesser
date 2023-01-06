import random
print("Welcome to Number Guesser game :)")

def number(input):
    if(not input.isdigit()):
        print("Please type a number.")
        return False
    else:
        return True

def zero(input):
    if(int(input)<=0):
        print("Please type a number above zero.")
        return False
    else:
        return True

def is_correct(guess,random_number):
    user_guess = int(guess)
    if(user_guess == random_number):
        return True
    elif(user_guess>random_number):   
        print("You were above the number!.")
        return False
    else:
        print("You were below the number!.")
        return False

while True:
    max_number_value = input("Type a number: ")

    if(not number(max_number_value) or not zero(max_number_value)):
        continue

    random_number = random.randint(0,int(max_number_value))
    print(random_number)
    guesses = 0

    while True:
        user_guess = input("Make a guess: ")
        guesses+=1
        if(not number(user_guess)):
            continue
        elif(is_correct(user_guess,random_number)):
            break
        else:
            continue
    break
print("="*30)
print("You got it in",guesses,"guesses")
print("="*30)