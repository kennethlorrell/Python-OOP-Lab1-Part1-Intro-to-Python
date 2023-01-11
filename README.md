# Lab #01. Part 1 (Intro to Python)

## Task #01
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. 
The type of operator and data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2
Notes:
Use the argparse module to parse command line arguments. 
Your implementation shouldn't require entering any parameters (like -f or --function).

## Task #02
Write a Python-script that performs the standard math functions on the data.
The name of function and data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2
Notes:
Function names must match the standard math functions from the built-in libraries.
Use the argparse module to parse command line arguments. 
Your implementation shouldn't require entering any parameters (like -f or --function).

## Task #03
Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF syntax (without using regular expressions).
Formula = Number* | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)
Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)
Example how to call the script from CLI:
$ python task_1_ex_3.py 1+5-2
Hint: use argparse module for parsing arguments from CLI
Task #04
You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not (hence you cannot take a fraction of a bar).
Write a function that returns the maximum weight of gold that fits into a knapsack's capacity.
The first parameter contains 'capacity' - integer describing the capacity of a knapsack.
The next parameter contains 'weights' - list of weights of each gold bar.
The last parameter contains 'bars_number' - integer describing the number of gold bars.
Output : Maximum weight of gold that fits into a knapsack with capacity of W.
Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity).
Example of how the task should be called:
$ python task3_1.py -W 56 -w 3 4 5 6 -n 4
