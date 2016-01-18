#!/usr/bin/python

#https://github.com/novel/py-urbandict
import urbandict
import time
import json
from string import ascii_lowercase

# Open a file
with open('foo2.txt', 'w') as outfile:    
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            #print a+b
            #fo.write(a+b);
            time.sleep(1)
            result = urbandict.define(a+b)
            #print result[0]        
            json.dump(result[0], outfile)

# Open a file
with open('foo3.txt', 'w') as outfile:    
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                #print a+b+c
                time.sleep(1)
                result = urbandict.define(a+b+c)
                #print result[0]        
                json.dump(result[0], outfile)
