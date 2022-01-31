from mrjob.job import MRJob
import math as mt
import datetime as dt

"""
 python select_groups_active17.py first_post > firstpost_2017active
"""
class Count(MRJob):

    def mapper(self, _, line):

        reddit, key = line.split("\t")
        user, time = key.strip("[]").split(",")
        time=time.strip().strip("\"")
        reddit = reddit.strip().strip("\"")
        user = user.strip().strip("\"")        
        yield(reddit, [user,time])
         
    def reducer(self, word, counts):
        data = []
        times = []
        for i in counts:
            data.append( (i[0], int(i[1])))
            times.append(int(i[1]))
        d1 = dt.datetime.fromtimestamp(min(times))
        d2 = dt.datetime.fromtimestamp(max(times))
        duration = (d2-d1).days + 1
        if duration > 31:
            for u, t in data:
                yield(word, [u, t])


"""the below 2 lines are ensuring the execution of mrjob, the program will not
execute without them"""		
if __name__ == '__main__':  
    Count.run()
