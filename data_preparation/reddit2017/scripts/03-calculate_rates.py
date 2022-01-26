from mrjob.job import MRJob
import math as mt
"""
python 01-map_reduce.py reddit2017/reddit2017_delta_sizes > reddit_2017_size_rate_lograte

output file:

[reddit, start_year, current_year, current_month] [size, rate, lograte]
"""
class Count(MRJob):

    def mapper(self, _, line): 
        key, count = line.strip().split("\t")
        key = key.strip("[]").split(",")
        
        reddit = key[0].strip().strip("\"")

        
        year = key[1].strip()
        month = key[2].strip()
        if int(year)<2018:
            yield(reddit, [int(year), int(month), int(count)])
    def reducer(self, word, counts):
    #this reduce program calculates size of subreddit at each month, montly growth rate Si/Si-1 and montly lograte
        sizes = []
        for i in counts:
            sizes.append(( int(i[0]), int(i[1]), int(i[2])))
        sorted_sizes = sorted(sizes, key=lambda element: (element[0], element[1]))
        yield([word, sorted_sizes[0][0], sorted_sizes[0][0], sorted_sizes[0][1]], [sorted_sizes[0][2], 1, 0])
        start_year = sorted_sizes[0][0]
        s = [sorted_sizes[0][2]]
      
        for i in range(1, len(sorted_sizes)):
           s.append(s[i-1] + sorted_sizes[i][2])
           yield([word, start_year, sorted_sizes[i][0], sorted_sizes[i][1]], [s[i], s[i]/s[i-1], mt.log(s[i]/s[i-1]) ])


"""the below 2 lines are ensuring the execution of mrjob, the program will not
execute without them"""		
if __name__ == '__main__':
    #input is reddit_montly_users
	Count.run()