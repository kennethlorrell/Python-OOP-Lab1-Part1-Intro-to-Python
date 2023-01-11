import argparse

def knapsack(cap, weights, n):
    total = 0
    weights = sorted(weights, reverse=True)
    while cap > 0 and n>0 and len(weights) > 0:
        if weights[0] <= cap:
            total += weights[0]
            cap -= weights[0]
            weights = weights[1:]
            n -=1
        else:
            weights = weights[1:]            
    return total

parser = argparse.ArgumentParser()

parser.add_argument('-W','--capacity', required=True, type=int)
parser.add_argument('-w','--weights', nargs='+', help='<Required> Set flag', required=True, type=int)
parser.add_argument('-n','--bars_number',  required=True, type=int)

args = parser.parse_args()
cap, weights, n= args.capacity, args.weights, args.bars_number

print(knapsack(cap, weights, n))
