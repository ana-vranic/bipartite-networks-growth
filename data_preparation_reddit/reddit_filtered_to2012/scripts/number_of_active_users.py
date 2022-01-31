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
       time = int(time)
       day_time = dt.datetime.fromtimestamp(time)
       y = day_time.year
       m = day_time.month
       yield((y,m), user)

    def count(self, key, users):
        ul = []
        for u in users:
            ul.append(u)
        yield(key, len(set(ul)))


    def steps(self):
        return [
            MRStep(mapper=self.get_subreddits,
                   reducer=self.count),
        ]        

"""the below 2 lines are ensuring the execution of mrjob, the program will not
execute without them"""		
if __name__ == '__main__':  
    NewGroups.run()
