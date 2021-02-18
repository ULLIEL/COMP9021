# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.
        
import sys
import re
def encode(list_of_integers):
    read_as1 = f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
    list_read_as1 = list(read_as1)
    list_read_as1.remove('[')
    list_read_as1.remove(']')    
    str_read_as1 = ''.join(list_read_as1)
    l = []
    for item in str_read_as1:
        l.append(item)
        if item in ['0','1']:
            l.append(item)
    l = ''.join(l)   
    temp_result = l.replace(',','0')
    temp_result = list(temp_result)
    for item in temp_result:
        if item == ' ':            
            temp_result.remove(' ')
    temp_result = ''.join(temp_result)
    result = int(temp_result,2)
    
    return result          


def decode(integer):
    read_as2 = bin(the_input)[2 :]
    read_as2_list = list(read_as2)
    new_read_as2_list = []
    last_result = []
    i=0
    while len(read_as2_list) == 1:
        if read_as2_list[0] == '1':
            return None
        elif read_as2_list[0] == '0':
            return None
            
            
    while i < len(read_as2_list)-1:
        if read_as2_list[i] == '0' and read_as2_list[i+1] == '0':
            new_read_as2_list.append('0')
            i += 2
        elif read_as2_list[i] == '1' and read_as2_list[i+1] == '1':
            new_read_as2_list.append('1')
            i += 2
        elif read_as2_list[i] == '0' and read_as2_list[i+1] == '1':
            new_read_as2_list.append(',')
            i += 1
        elif read_as2_list[i] == '1' and read_as2_list[i+1] == '0':
            return None

    str_read_as2_list = ''.join(new_read_as2_list)    
    str_read_as2 = str_read_as2_list.split(',')

    if str_read_as2_list.count(',') % 2 !=0 and len(read_as2)%2 != 0:
        pass
    elif str_read_as2_list.count(',') % 2 ==0 and len(read_as2)%2 == 0:
        pass
    else:
        return None
    
    for item in str_read_as2:
        result = int(item,2)          
        last_result.append(result)

    return last_result



# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
