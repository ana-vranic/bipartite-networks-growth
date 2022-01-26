#!/usr/bin/env python3

import sys

curr_user = None
times = []
    
for line in sys.stdin:
    try:
        key, ctime = line.split()[:-1], int(line.split()[-1]) 
        
        if key == curr_user:
            times.append(ctime)
        else:
            if curr_user:
                print('%s\t%s' % (curr_user, min(times)))
        
            curr_user = key
            times = [ctime]
    except:
        pass
if curr_user:
    print('%s\t%s'%(curr_user, min(times)))


#    if len(line.split())>1:
#        key , curr = " ".join(line.split()[:-1]), line.split()[-1]
#    
#        if key == curr_user:
#            times.append(int(curr))
#        else:
#            if curr_user:
#            
#                print('%s\t%s'% (key, min(times)))
#            curr_user = key
#            times = [int(curr)]
#    else:
#        pass

#if curr_user:
#    print('%s\t%s'% (key, min(times)))


