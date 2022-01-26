#!/usr/bin/env python3

import sys
import json
    
for line in sys.stdin:
    try:
        print('%s\t%s'%(line.split('\t')[0][1:-1], line.split('\t')[1]))
    except:
        pass
        #print('z', 1)
