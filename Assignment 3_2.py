# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:04:09 2018  @author: krishna.i
Problem​ ​Statement
Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""
# output expected ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
samStr = "acadgild"
myLis1 = [i for i in samStr.upper()]
print(myLis1)

# output expected ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
samLis= ['x','y','z']

myLis2 = [i*j for i in samLis for j in range(1,5)]
print(myLis2)

# output expected  ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
myLis3= [i*j for i in range(1,5) for j in samLis]
print(myLis3)

# output expected [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
myLis4 = [[i+j] for i in range(1,4) for j in range(1,4)]
print(myLis4)

# output expected [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
myLis5 = [[i+j for i in range(1,5)] for j in range(1,5)]
print(myLis5)

# output expected [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
myLis6 = [(j,i) for i in range(1,4) for j in range(1,4)]
print(myLis6)