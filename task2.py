import argparse
from operator import add, mul, pow, floordiv, mod, sub, truediv

func_dict = {
  'add': add, 
  'mul': mul, 
  'pow': pow,
  'floordiv': floordiv,
  'mod': mod, 
  'sub': sub,
  'truediv': truediv
}

parser = argparse.ArgumentParser()

parser.add_argument('f',  type=str)  
parser.add_argument('num1',  type=int)
parser.add_argument('num2',  type=int)

args = parser.parse_args()
f, num1, num2 = args.f, args.num1, args.num2

print(func_dict.get(f, lambda x, y: print('Unknown function!'))(num1, num2))
