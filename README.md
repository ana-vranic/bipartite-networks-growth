# bipartite-networks-growth

This is suporting repository for paper [Universal growth of social groups: empirical analysis and modeling](https://arxiv.org/abs/2206.06732).

---

`./model`

We proposed the bipartite growth model for simulating the growth of online social groups. The model parameters are:
- time series of new users strored in the txt file
- probability that user is active $p_a$
- probability that user makes new group $p_g$
- probability that user perform social linking $p_{aff}$
- random linking could be uniform $random$, or $preferential$ when user has preference toward larger groups

---

Our empirical analasys is based on Reddit and Meetup datasets. Here we do not give the raw datasets, only the final results of calculated group sizes distributions. The Meetup dataset could be downloaded with Meetup API, while Redddit data could be downloaded on https://pushshift.io/. 

Our prepocessed datasets take form [userid, timestamp], where timestamp is the time when user is for the first time active in the group. Also, the folder 
`./data_preparation_reddit` contains map reduce scripts to process big reddit data. 
