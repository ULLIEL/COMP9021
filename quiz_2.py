# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
#For the first question "Properly ordered, the cycles given by the mapping are:"
a = mapping.keys()
temp_cycles = []

for a in mapping.keys():
    b = a
    while mapping[b] in mapping.keys():
        temp_cycles.append(b)
        b = mapping[b]
        if a == b:
            break
        elif b in temp_cycles:
            temp_cycles = []
            break
    if temp_cycles != []:
        if sorted(temp_cycles) not in cycles:
            cycles.append(temp_cycles)
            temp_cycles = []         #Make the temp_cycles a empty list so that [] will not appear in the list
        


#For the second question "The (triply ordered) reversed dictionary per lengths is:"
from collections import defaultdict

dict1 = defaultdict(list)
dict2 = defaultdict(dict)
for c in mapping.keys():
    dict1[mapping[c]].append(c) #This step can get the reversed list like 1:[1],3:[3],6:[5,6]

for c in dict1.keys():
    dict2[len(dict1[c])][c] = dict1[c] #To calculate the number of reversed values in a reversed key

reversed_dict_per_length = dict(dict2)
                       

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


