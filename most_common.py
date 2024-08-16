#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

# create a set of the input string 
# take the input string and char for each character
# loop through the set string checking each character  
# if the char in set string matches the character in input string 
# increase count by 1 
# the append the char and count to 
set_s = set(s)
empty = []
for char in set_s: 
    count = 0
    for chara in s: 
        if char == chara: 
            count += 1
    empty.append([char, count])        

empty = sorted(empty)
for item in empty:
    print(item)
    
