
import pandas as pd

import spacy
from collections import Counter
nlp = spacy.load('en_core_web_sm')


def extract_syntactic_features(text):

  if not text or pd.isna(text):
    return {}


  doc = nlp(text)

  features = {
        'num_sentences': len(list(doc.sents)),
        'num_tokens': len(doc),
        'dependency_relations': [],
        'noun_phrases': [],
        'verb_phrases': [],
        'subjects': [],
        'objects': []
    }

  dependency_relations = []


  for token in doc:
      if token.is_space or token.is_punct:
          continue

      dependency_relations.append(token.dep_)

      if token.dep_ in ['nsubj', 'nsubjpass']:
          features['subjects'].append(token.text.lower())

      elif token.dep_ in ['dobj', 'iobj', 'pobj']:
          features['objects'].append(token.text.lower())

  for chunk in doc.noun_chunks:
      features['noun_phrases'].append(chunk.text.lower())

  features['dependency_counts'] = dict(Counter(dependency_relations))

  result = f'Sentences: {features['num_sentences']}, Subjects: {features['subjects']}, Objects: {features['objects']}, Noun phrases: {features['noun_phrases']}'
  return result
