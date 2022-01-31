## Data preparation

1) Reddit data are downloaded from https://redditsearch.io/. Data have separated comments and post in the json files. Each file is collection of posts/comments for one moth. 

2) We use code from `hdfs_scripts/` to filter raw data. For each subreddit and user we select timestamp when user made first activity on given subreddit. The filtered data are saved in `first_post` file and have following structure

```
[subreddit/user] timestamp
```

3) running code in `reddit2017/` from file `first_post` we select group active in 2017 and extract month growth rates and sizes distributions, where subreddits are grouped per creation year
The outputs are:
- reddit2017_groups > filtered dataset  
- reddit2017_delta_sizes > subreddit, year-month, Nnew users
- reddit2017_rates > subreddit, year-month, growth rate

finaly obtained rates and sizes distributions are grouped per reddit creation year and saved into json files
  
  - `reddit2017_sizes_normed_per_year.json`
  - `reddit2017_logrates_normed_per_year.json`
   
4) For detailed analasys of subrredits growth from `reddit2017_groups` using code in `reddit_filtered_to2012` we filtered those active untill 2011-12, and removed subreddits active less than month and calculate distributions of sizes and rates. We also calculate time series of new users, active users, new_groups, cumulative number of users and groups. Those data are merged in file `reddit2012_ts.csv`, while merged distributions of sizes and rates are stored in files `reddit2012_logrates.txt`, `reddit2012_logrates.txt`, `reddit2012_sizes.txt` , `reddit2012_sizes_logrates.txt`

