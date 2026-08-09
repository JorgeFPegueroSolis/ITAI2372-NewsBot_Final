# ITAI2372-NewsBot_Final

This is the final project for the Natural Language Processing (NLP) course (ITAI 2373).

What NewsBot 2.0 Can Do

✅ Preprocess news articles using advanced text cleaning techniques

✅ Classify articles into categories (Business, Entertainment, Politics, Sport, Tech)

✅ Analyze sentiment and emotional tone of news content

✅ Identify grammatical and syntactic patterns using POS tagging and dependency parsing

✅ Extract named entities (people, organizations, locations) from any article

✅ Generate short, automatic summaries of full articles

✅ Detect the language of a text and translate it into another language

✅ Hold a simple conversation: request articles by category, ask follow-up questions, and get direct answers, without writing any code

Technologies Used
spaCy and NLTK — text processing, POS tagging, syntax parsing, and named entity recognition
scikit-learn — TF-IDF feature extraction and the LinearSVC classification model
NLTK VADER — sentiment analysis
sumy — extractive text summarization (LSA)
langdetect — language detection
deep-translator — translation (Google Translate)
pandas / joblib — data handling and model persistence
BBC News dataset — public dataset of 2,225 news articles used to train and evaluate the classifier
Google Colab — development environment

How It Works

nce the notebook is running, it asks what you want to do, and you just type your request in plain English:

Ask for an article — for example, show me a tech article. NewsBot picks one, tells you its category, sentiment, and grammatical pattern breakdown.
Ask a follow-up question about that same article — for example, translate it, summarize it, or who is mentioned in this article. NewsBot remembers which article you're currently looking at, so you don't need to repeat or resend the text.
Ask for a different article whenever you want — NewsBot picks a new one and it becomes the current article for any follow-up questions.
Type goodbye whenever you're done, and the conversation ends.



