import random
#get positive int as level
while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    #where level is not an int
    except:
        pass
            
#use n to store random number
n = random.randint(1, level)
#get guesses
while True:
    try:
        guess = int(input('Guess: '))
        if guess > 0:
            if guess > n:
                print('Too large!')
            elif guess < n:
                print('Too small!')
            else:
                print('Just right!')
                break
        else:
            pass
    #where guess is not an int
    except:
        pass
