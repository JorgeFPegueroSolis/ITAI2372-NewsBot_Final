Data

This folder contains the datasets used to build and test NewsBot Intelligence System 

Training Dataset

Used to train and evaluate the classification model (preprocessing, TF-IDF, POS analysis, and the LinearSVC classifier). It contains labeled news articles across five categories: Business, Entertainment, Politics, Sport, and Tech.

Link: https://www.kaggle.com/competitions/learn-ai-bbc/data

File Descriptions
BBC News Train.csv — training set, 1,490 records, that I am going to use to train and evaluate the model.
BBC News Test.csv — test set, 736 records, used in the project just as a sample in the NewsBotAgent notebook.

Testing Dataset

Used as unseen data to run the final NewsBot 2.0 agent against, including category prediction, sentiment analysis, entity recognition, summarization, and translation. This dataset is not used during training, so it gives a realistic sense of how the system performs on articles it has never seen before.

Link: https://www.kaggle.com/datasets/gpreda/bbc-news?resource=download
