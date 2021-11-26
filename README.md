# Temporal Topic Modeling Using LDA2Vec

Download these files before running

Link to cleaned NIPS papers (cleaned.txt): 

https://drive.google.com/file/d/19EoVcRdTdQ5Lr6262Qtnb5k1PaRXCuoK/view?usp=sharing

Link to pretrained word embeddings (glove.6B.300d.txt): 

https://drive.google.com/file/d/19_B-ip57uedacDN7SZN9DDVif29YD7vA/view?usp=sharing

Link to original NIPS papers (papers.csv): 

https://drive.google.com/file/d/1ZvwH8whuG8pd0asa1LM7eeMEX6Tey4wi/view?usp=sharing


## Preprocessing

Due to memory restrictions we sampled batches of the documents by year. Each pre-processing includes 300 non-overlapping documents taken from 2008-2017 in which every 3 documents are aggregated into 1 single document. Thus, there are essentially 100 aggregate documents in each aggregate folder.

lda2vec was run on each of these groups individually resulting in a unique set of embeddings that can be used to find a suitable set of hyperparameters or other experiments. The embeddings hold the output from the lda2vec for word, doc, and topic embeddings. The embeddings are clustered into 40 topics.

## LDA2Vec

Here are the following coherence scores:

Aggregate 1

Coherence scores for each number of topic clusters
20 topics: 0.3107490686037474
30 topics: 0.34992583735742505
40 topics: 0.39195844545443026
50 topics: 0.3827791294533138

Aggregate 2

Coherence scores for each number of topic clusters
40 topics: 0.3817637460859906

Aggregate 3

Coherence scores for each number of topic clusters
40 topics: 0.38678243150003255

Aggregate 4

Coherence scores for each number of topic clusters
40 topics: 0.3831858639488928
