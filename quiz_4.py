# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


#The arithmetic is finding the first ")", then making a slice, cut the ")",and keep the content before it.
#And finding the nearest "(", having a slice again, and get the content between "("")".
#Count the number of comma, the num = arity -1
#Then add the "("")" for the content, replace it into a blank. Continue this process.
#If there has "_" and" " in the word, make more discuss.

#算法是先找到第一个右括号，然后做切片，切割左括号之前的内容。
#然后再找到离该右括号最近的左括号，再做切片，对两个括号中间的逗号计数，逗号数量应该等于arity-1。
#接着给已切片的括号内内容再加上左右括号，并将其替换成“”，继而执行下一个右括号。
#如果word中有下划线以及空白空格的问题，继续讨论。

import sys
new_list = []

def is_valid(word, arity):
    str = word
    new_word = list(str)
    
    if arity == 0:
        if new_word.count("(") != 0:
            return False
        elif new_word.count(")") != 0:
            return False
        else:
            if word.isalpha():
                return True

    if arity > 0:                
        if word.count(')') > 0:
            while '(' not in word:
                #For  arity = 1, and word is f).
                return False
            temp_content = new_word[:new_word.index(")")]  
            copy_temp_content = temp_content[::-1]
            #This expression way has the same function as reverse.
            content = copy_temp_content[:copy_temp_content.index("(")]            
            content_copy=list(content)

            while ' ' in content:
                content.remove(' ')
            while '_' in content:
                content.remove('_')

            if content.count(',') == arity - 1:                
                content = content[::-1]
                content = "".join(content)
                content1 = content.split(",")
           
                for i in content1:
                    if i.isalpha() == False:
                        return False                
                content_copy=content_copy[::-1]
                content_copy = "".join(content_copy)
                content_copy = '(' + content_copy + ')'
                #Add left and right bracket to struct a stantdard symbol, then replace it.
                new_word = "".join(new_word)                
                new_word = new_word.replace(content_copy, "")                

                if "(" in new_word:                    
                    return is_valid(new_word, arity)
                else:
                    new_word = list(new_word)
                    while '_' in new_word:
                        new_word.remove("_")                
                    new_word = "".join(new_word)
                    if new_word.isalpha()==True:
                        return True
                    else:
                        return False
                                    
        else:
            return False

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')

