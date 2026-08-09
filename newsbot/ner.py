
import spacy

nlp = spacy.load('en_core_web_sm')

def named_entity_recognition(text):

    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities
