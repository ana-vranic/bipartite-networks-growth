from mrjob.job import MRJob
import math as mt
import datetime as dt

class Count(MRJob):

    def mapper(self, _, line):

        reddit, key = line.split("\t")
        user, time = key.strip("[]").split(",")
        time = time.strip().strip("\"")
        reddit = reddit.strip().strip("\"")
        user = user.strip().strip("\"")
        time = int(time)
        day_time = dt.datetime.fromtimestamp(time)
        y = day_time.year
        m = day_time.month
        if int(y)<2012:
             yield(reddit, [user, time])

"""the below 2 lines are ensuring the execution of mrjob, the program will not
execute without them"""		
if __name__ == '__main__':  
    Count.run()
