from itertools import product
import sys

fn = sys.argv[1]

with open(fn) as file:
    lines = file.read().split("\n")
    print(lines)

alpha, r = lines[:2]
r = int(r)
alphabet = alpha.split(" ")
gen = product(alphabet, repeat = r)
for i in gen:
    print("".join(i))
