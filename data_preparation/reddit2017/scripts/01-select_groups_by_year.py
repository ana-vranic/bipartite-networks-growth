from mrjob.job import MRJob
import math as mt
import datetime as dt

"""
 python select_groups_active17.py first_post > firstpost_2017active
"""
class Count(MRJob):

    def configure_args(self):
        super(Count, self).configure_args()
        self.add_passthru_arg("-m", "--maxYear", help="your argument description")

    def mapper(self, _, line):
        key = line.split('\t')[0].strip("\"[']")
        
        reddit = key.split("/")[0]
        user = key.split("/")[1]
        
        time = line.split('\t')[1]
        day_time = dt.datetime.fromtimestamp(int(time))
        
        yield(reddit, [day_time.year, user, time])
         
    def reducer(self, word, counts):
        data = []
        years = []
        times = []
        for i in counts:
            data.append(( int(i[0]), i[1], i[2])) #year, month, user, timestamp
            years.append( int(i[0]))
            times.append(int(i[2]))
        d1 = dt.datetime.fromtimestamp(min(times))
        d2 = dt.datetime.fromtimestamp(max(times))
        duration = (d2-d1).days 
        if int(self.options.maxYear) in years: #check if group is active in selected year
            if duration > 31:
            
                for y, u, t in data: # take only data less than that year
                    if y<=int(self.options.maxYear):
                        yield(word, [u, t])


"""the below 2 lines are ensuring the execution of mrjob, the program will not
execute without them"""		
if __name__ == '__main__':  
    Count.run()
