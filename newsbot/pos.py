
import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

def analyze_pos_patterns(text):

  doc = nlp(text)

  pos_counts = Counter([token.tag_ for token in doc if not token.is_space])

  total_words = sum(pos_counts.values())

  if total_words == 0:
    return {}

  pos_proportions = {pos: count / total_words for pos, count in pos_counts.items()}

  return pos_proportions
