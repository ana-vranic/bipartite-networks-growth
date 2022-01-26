#!/bin/bash

# in folder data are stored submissions

mapred streaming -input data  -output results_sub -mapper map1/map.py -reducer map1/reduce.py -file map1/map.py -file map1/reduce.py

# there are a lot of comments so we run map-reduce sctipt separatly for each year 

for year in 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017

do
   mapred streaming -input "data_c/${year}"  -output "results_comments/${year}" -mapper map1/map.py -reducer map1/reduce.py -file map1/map.py -file map1/reduce.py
done

# then we store or subresults in the same location "results_all" and run secound pair of map-reduce scripts to get final result

mapred streaming -input results_all  -output first_post -mapper map2/map.py -reducer map2/reduce.py -file map2/map.py -file map2/reduce.py
