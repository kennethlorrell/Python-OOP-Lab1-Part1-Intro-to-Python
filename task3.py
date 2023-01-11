import argparse

def is_formula(str_f):
    if str_f and str_f[0].isdigit():
        str_f = str_f.lstrip('0123456789')
        if not str_f or str_f == '.':
            return True
        if str_f[0] in "+-*":
            return is_formula(str_f[1:])
    return False

parser = argparse.ArgumentParser()

parser.add_argument('formula',  type=str)  

args = parser.parse_args()
formula = args.formula

if is_formula(formula):
	print(is_formula(formula), eval(formula))
else:
	print(is_formula(formula), None)
