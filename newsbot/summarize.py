
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')
nltk.download('punkt_tab')

def summarize(text): 
  
  summary = []

  parser = PlaintextParser.from_string(text, Tokenizer('english'))

  summarizer = LsaSummarizer()(parser.document, 3)

  for sentence in summarizer:
    summary.append(str(sentence))

  return summary

  
