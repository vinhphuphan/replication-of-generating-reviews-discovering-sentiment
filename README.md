# Replication of Learning to Generate Reviews and Discovering Sentiment

## Summary

The authors train a character-RNN (using mLSTM units) over Amazon Product Reviews (82 million reviews) and use the char-RNN as the feature extractor for sentiment analysis. These unsupervised features beat state of the art results for the dataset while are outperformed by supervised approaches on other datasets. Most important observation is that the authors find a single neuron (called as the sentiment neuron) which alone achieves a test accuracy of 92.3% thus giving the impression that the sentiment concept has been captured in that single neuron. Switching this neuron on (or off) during the generative process produces positive (or negative) reviews.

## Original

* The paper aims to evaluate if the low level features captured by char-RNN can support learning of high-level representations.

* [Link to the paper](https://arxiv.org/abs/1704.01444)

* [Link to the Github repository]([https://blog.openai.com/unsupervised-sentiment-neuron/](https://github.com/openai/generating-reviews-discovering-sentiment))

