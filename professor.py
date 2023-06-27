import random

def main():
    level = get_level()
    score = overall_scores(level)

    #print score
    print(f'Score: {score}')
def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except:
            pass
#generate X and Y
def generate_integer(level):
    while True:
        try:
            if level == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            elif level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
            elif level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
            return x, y
        except:
            raise ValueError

#a function to give keep tries count
def tries_counter(x, y):
    tries = 0
    while tries < 3:
        try:
            answer = int(input(f'{x} + {y} = '))
            if answer == x + y:
                return True
            else:
                tries += 1
                print('EEE')
        except:
            tries += 1
            print('EEE')
    print(f'{x} + {y} = {x+y}')
    return False

#a function to calculate and return score 
def overall_scores(level):
    score = 0
    rounds = 0
    #generate 10 tasks
    while rounds < 10:
        x, y = generate_integer(level)
        answer1 = tries_counter(x, y)
        if answer1 == True:
            score += 1
        rounds += 1
    return score

if __name__ == "__main__":
    main()
