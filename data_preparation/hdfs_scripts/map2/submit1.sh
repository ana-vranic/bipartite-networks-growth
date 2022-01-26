 mapred streaming -input results_all  -output results_sc -mapper map2/map.py -reducer map2/reduce.py -file map2/map.py -file map2/reduce.py
