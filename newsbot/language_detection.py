
from langdetect import detect

def language_detection(text):

  language = detect(text)

  return language
