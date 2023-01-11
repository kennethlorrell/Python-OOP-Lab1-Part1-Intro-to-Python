import argparse

parser = argparse.ArgumentParser()

parser.add_argument('num1', type=int)  
parser.add_argument('sign', type=str)
parser.add_argument('num2', type=int)

args = parser.parse_args()
num1, sign, num2 = args.num1, args.sign, args.num2

if sign == '+':
     print(num1 + num2)
elif sign == '-':
     print(num1 - num2)
elif sign == '*':
     print(num1 * num2)
elif sign == '/':
     print(num1 / num2)
else:
     print('Something went wrong...')
