# Replication of Learning to Generate Reviews and Discovering Sentiment

In today's world of abundant research papers, reproducing and confirming the findings in these papers is getting harder. This repository is aimed to reproduce the results of the paper titled ”Learning to Generate Reviews and Discovering Sentiment”.  Our main goal is to show the initial claim of paper holds and we further replicate the findings on unseen data sets to show that the results are consistent.

## Original Paper

* "Learning to Generate Reviews and Discovering Sentiment"(2017) is a research paper authored by Alec Radford, Rafal Jozefowicz, and Ilya Sutskever.

* The paper presents a novel approach to generating text reviews and discovering sentiment in an unsupervised manner.

* Unlike traditional sentiment analysis, which relies on labeled data, this work leverages a large dataset to train a character-level recurrent neural network (char-RNN) model.

* [Link to the paper](https://arxiv.org/abs/1704.01444)

* [Link to the original github repository](https://github.com/openai/generating-reviews-discoering-sentiment)

## Replication of Original Work
To successfully replicate the source work

* **Data Collection** : Original work was built using Amazon Product Reviews (82 million reviews) from May 1996 to July 2014. We test the model on new datasets : Yelp, IMDB, SST, Hotel, Reddit.

* **Methodology** :
  * Researchers will replicate the model training and sentiment analysis process described in the paper. 
  * Ensure that the code is in the same state as when the experiments were conducted.
  * Ensure that the model architecture, hyperparameters, and training procedures are faithfully reproduced.
  * Implement the same performance evaluation metrics as used in the paper: Test Accuracy, Precision, AUC-ROC curves.

## Result
