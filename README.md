# bipartite-networks-growth

This is a suporting repository for the paper [Universal growth of social groups: empirical analysis and modeling](https://arxiv.org/abs/2206.06732).

---

`./model`

We proposed the bipartite growth model for simulating the growth of online social groups. The model parameters are:
- time series of new users stored in the txt file
- probability that the user is active $p_a$
- the probability that the user makes a new group $p_g$
- probability that the user perform social linking $p_{aff}$
- random linking could be uniform $random$, or $preferential$ when a user has a preference toward larger groups

---

Our empirical analysis is based on Reddit and Meetup datasets. Here we do not give the raw datasets, only the final results of calculated group sizes distributions. The Meetup dataset could be downloaded with Meetup API. The Redddit data could be downloaded from https://pushshift.io/. 

Our processed datasets take the form [userid, timestamp], where the timestamp is the time when the user is for the first time active in the group. Also, the folder 
`./data_preparation_reddit` contains map-reduce scripts to process big Reddit data. 
