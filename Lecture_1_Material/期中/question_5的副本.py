# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv
import string
def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    lines = []
    with open('cpiai.csv','r') as f :
        while True :
            line = f.readline()
            lineLst =  line.split(',')
            if line == '' :
                break
            if lineLst[0][:4] == str(year) :
                lines.append([int(lineLst[0][5:7])-1,float(lineLst[2][:-1])])
    f.close()
    lines.sort(key=lambda a:(a[1],a[0]),reverse=True)
    print(f'In {year}, maximum inflation was: {lines[0][1]}')
    i = 0
    month = [lines[0][0]]
    while lines[0][1] == lines[i+1][1] :
        i += 1
        month.append(lines[i][0])
    print('It was achieved in the following months:',end = ' ')
    for j in range(i,0,-1):
        print(months[month[j]],end=', ')
    print(months[month[0]])
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    f(2013)

