import argparse

parser = argparse.ArgumentParser(description='Meow like a cat')#appears in help msg
parser.add_argument('-n', default=1, help='Number of times to meow', type=int)#initializes arg -n, gives help msg & converts n to int
args = parser.parse_args()#passes args to args variable

for _ in range(args.n):
print('meow')