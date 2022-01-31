from mrjob.job import MRJob
from mrjob.step import MRStep
import math as mt
import datetime as dt

"""
 input is first_post_active17_filtered
"""
class NewGroups(MRJob):

    def get_subreddits(self, _, line):
       reddit, key = line.split("\t")
       user, time = key.strip("[]").split(",")
       time = time.strip().strip("\"")
       reddit = reddit.strip().strip("\"")
       yield(user, int(time))

    def get_creation_date(self, user, times):
        cr = min(times)
        day_time = dt.datetime.fromtimestamp(cr)
        
        y = day_time.year
        m = day_time.month
        
        yield((y,m), 1)

    def count(self, key, counts):
        yield(key, sum(counts))


    def steps(self):
        return [
            MRStep(mapper=self.get_subreddits,
                   reducer=self.get_creation_date),
            MRStep(reducer=self.count)  
        ]        
        
"""the below 2 lines are ensuring the execution of mrjob, the program will not
execute without them"""		
if __name__ == '__main__':  
    NewGroups.run()
