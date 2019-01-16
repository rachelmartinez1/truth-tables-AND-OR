#Program 1
#Rachel Martinez

from array import *

x = 0

#Building 2D Array/Table
#x is the answer variable - should be able to be accessed/filled with an index
table = [['p','q',x], ['T','T',x], ['T','F',x], ['F','T',x], ['F','F',x]]

for r in table:
    for c in r:
        print(c,end = " ")
    print()