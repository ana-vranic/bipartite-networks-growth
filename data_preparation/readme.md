Data preparation

1) Reddit data are downloaded from https://redditsearch.io/.

2) For each user we selected time of the first post on each subreddit
results are collected in the firstpost file 
**[subreddit/user] timestamp_when_user_made_first_post_in_subreddit**

3) running **submit_statistics** we first select groups active in 2017, tend extract rates and sizes 
   ${loc}/reddit${year}_delta_sizes
   ${loc}/reddit${year}_size_rate_lograte
   
4) For detailed analasys of subrredits growth from groups active in 2017 we filtered those active untill 2012

   for this we use scripts in reddit_filtered_to2012
   
   we also calculate number of new users, number of active users and  new groups
   and calculate size_rate_lograte of subreddits during time
   

