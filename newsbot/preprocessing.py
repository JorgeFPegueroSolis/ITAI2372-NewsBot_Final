
import pandas as pd
import re

def clean_text(text):

  if pd.isna(text):
    return ""

  text = str(text).lower()

  text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
  text = re.sub(r'<[^>]+>', '', text)
  text = re.sub(r'\S+@\S+', '', text)
  text = re.sub(r'[^a-zA-Z\s]', '', text)
  text = re.sub(r'\s+', ' ', text).strip()

  return text


import spacy
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):

  if not text:
    return ""

  doc = nlp(text)

  lemmas = []
  for token in doc:
      if not token.is_stop and not token.is_punct and token.lemma_.strip() != "":
          lemmas.append(token.lemma_)

  return " ".join(lemmas)
