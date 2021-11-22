# Temporal Topic Modeling Using LDA2Vec

Download these files before running

Link to cleaned NIPS papers (cleaned.txt): 

https://drive.google.com/file/d/19EoVcRdTdQ5Lr6262Qtnb5k1PaRXCuoK/view?usp=sharing

Link to pretrained word embeddings (glove.6B.300d.txt): 

https://drive.google.com/file/d/19_B-ip57uedacDN7SZN9DDVif29YD7vA/view?usp=sharing

Link to original NIPS papers (papers.csv): 

https://drive.google.com/file/d/1ZvwH8whuG8pd0asa1LM7eeMEX6Tey4wi/view?usp=sharing


## Preprocessing

Due to memory restrictions we sampled batches of the documents by year. Each pre-processing includes 10 non-overlapping documents each taken from 2008-2017. Thus we have 100 documents in each preprocessing folder.

lda2vec was run on each of these groups individually resulting in a unique set of embeddings that can be used to find a suitable set of hyperparameters or other experiments. The embeddings hold the output from the lda2vec for word, doc, and topic embeddings. The embeddings are clustered into 30 topics.
