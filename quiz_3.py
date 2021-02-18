# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
import re

s = '0' * nb_of_leading_zeroes + f'{int(code):o}.'
num_list = re.findall(r'[0-9]',s)
print(num_list)
num_list.reverse()  # list has already been reversed

direction = []
x = 0
y = 0
direction.insert(0,[0,0])

x_right_boundary = 0
x_left_boundary = 0
y_top_boundary = 0
y_bottom_boundary = 0

for item in num_list:
    if item == "0":
        if y == y_top_boundary:
            y_top_boundary +=1
        y += 1        
        direction.append([x,y])
    if item == "1":
        if x == x_right_boundary:
            x_right_boundary +=1
        if y == y_top_boundary:
            y_top_boundary +=1
        x += 1
        y += 1
        direction.append([x,y])
    if item == "2":
        if x == x_right_boundary:
            x_right_boundary +=1
        x += 1
        direction.append([x,y])
    if item == "3":
        if x == x_right_boundary:
            x_right_boundary +=1
        if y == y_bottom_boundary:
            y_bottom_boundary -=1
        x += 1
        y = y-1
        direction.append([x,y])
    if item == "4":
        if y == y_bottom_boundary:
            y_bottom_boundary -=1
        y = y-1       
        direction.append([x,y])
    if item == "5":
        if x == x_left_boundary:
            x_left_boundary -=1
        if y == y_bottom_boundary:
            y_bottom_boundary -=1
        x -= 1
        y -= 1
        direction.append([x,y])
    if item == "6":
        if x == x_left_boundary:
            x_left_boundary -=1
        x = x-1
        direction.append([x,y])
    if item == "7":
        if x == x_left_boundary:
            x_left_boundary -=1
        if y == y_top_boundary:
            y_top_boundary +=1            
        x = x-1
        y = y+1
        direction.append([x,y])

for i in direction:
    times = direction.count(i)
    if times%2==0:
        while i in direction:
            direction.remove(i)

all_black = True
while all_black:
    for i in range(x_left_boundary,x_right_boundary+1):
        if [i,y_top_boundary] in direction:
            all_black = False
            break
    if all_black:
        y_top_boundary -= 1
        all_black = True
    if y_top_boundary < y_bottom_boundary:
        break
    
for i in range(y_top_boundary,y_bottom_boundary-1,-1):
    for j in range(x_left_boundary,x_right_boundary+1):
        temp = [j,i]
        if temp in direction:
            print(on,end='')
        else:
            print(off,end='')
    print()














