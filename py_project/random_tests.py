import random
import string
import secrets

tuple_sample = ('abcdxyz', 'ABCDXYZ', '1234567890', '~!@#$%^&*()_+":><?/')
def main():
    print(func(tuple_sample))

def func(s):
    lower1, lower2 = ''.join(random.choice(tuple_sample[0])), ''.join(random.choice(tuple_sample[0]))
    upper1, upper2 = ''.join(random.choice(tuple_sample[1])), ''.join(random.choice(tuple_sample[1]))
    num1, num2 = ''.join(random.choice(tuple_sample[2])), ''.join(random.choice(tuple_sample[2]))
    symbol1, symbol2 = ''.join(random.choice(tuple_sample[3])), ''.join(random.choice(tuple_sample[3]))
    return str(lower1 + lower2 + upper1 + upper2 + num1 + num2 + symbol1 + symbol2)

if __name__ == '__main__':
    main()