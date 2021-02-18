# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE

#For question "The list of integers between 1 and 4 that are not keys of the mapping is:"
for j in range(1,upper_bound):
    if j not in list (mapping):
        nonkeys.append(j)


#For question "Represented as a list, the mapping is:"


for k in range(0,upper_bound):
    if k in list(mapping):
        mapping_as_a_list.append(mapping[k])
    else:
        mapping_as_a_list.append(None)


#For question "The one-to-one part of the mapping is:"
one_to_one_part_of_mapping = {}

a = mapping.keys()
b = mapping.values()
ax = mapping.keys()
bx = mapping.values()

for a,b in mapping.items():
    count=0
    for ax,bx in mapping.items():
        if b==bx:
            count = count +1
    if count >=2:
        continue
    else:
            one_to_one_part_of_mapping[a] = b

#End of Luo Hongpei's quiz1.



print()
print('The mappings\'s so-called "keys" make up a set whose number of elements is',len(mapping))
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


