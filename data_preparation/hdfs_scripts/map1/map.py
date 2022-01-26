#!/usr/bin/env python3

import sys
import json
    
for line in sys.stdin:
    try:
        p = json.loads(line)
        if ('subreddit' in p) & ('author' in p) & ('created_utc' in p):
         
              print(p['subreddit']+'/'+p['author'],  p['created_utc'])
    except:
        pass
        #print('z', 1)
