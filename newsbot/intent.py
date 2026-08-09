
from newsbot.preprocessing import clean_text, preprocess_text
from newsbot.extract_syntactic_features import extract_syntactic_features
from newsbot.pos import analyze_pos_patterns
from newsbot.sentiment_analysis import analyze_sentiment
from newsbot.ner import named_entity_recognition
from newsbot.translation import translate
from newsbot.language_detection import language_detection
from newsbot.summarize import summarize

def classify_intent(query):
    query = query.lower()
    intent = {"category": None, "action": "filter", "article_index": None, 'language' : 'english'}
    
    categories = ['business', 'entertainment', 'politics', 'sport', 'tech']
    languages = ['english', 'spanish', 'french', 'german', 'italian', 'japanese']

    for lang in languages:
        if lang in query:
            intent['language'] = lang
            
    for cat in categories:
        if cat in query:
            intent["category"] = cat

    if "translate" in query or "traduc" in query:
        intent["action"] = "translate"
    elif "summar" in query or "resum" in query:
        intent["action"] = "summarize"
    elif "entit" in query or "who" in query or "organization" in query:
        intent["action"] = "NER"
    elif "language" in query or "idiom" in query:
        intent["action"] = "detect"

    return intent


current_article = None

def process_query(df, intent):
    global current_article
    
    if intent['action'] == 'filter':
        pool = df if intent['category'] is None else df[df['Predicted_Category'] == intent['category']]
        
        if len(pool) == 0:
            return None
        
        row = pool.sample(1).iloc[0]
        current_article = {
            "text": row['description'],
            "predicted_category": row['Predicted_Category'],
            "pos_tags": analyze_pos_patterns(row['description']),
            "sentiment": analyze_sentiment(row['description'])
        }
        return current_article
    
    if current_article is None:
        return None
    
    text = current_article['text']
    
    if intent['action'] == 'translate':
        return translate(text, intent['language'])
    elif intent['action'] == 'summarize':
        return summarize(text)
    elif intent['action'] == 'NER':
        return named_entity_recognition(text)
    elif intent['action'] == 'detect':
        return language_detection(text)




def generate_response(result, intent):
    if result is None:
        if intent['action'] == 'filter':
            return "No articles found for that category."
        else:
            return "No article loaded yet. Try asking to see an article first."
    
    if intent['action'] == 'filter':
        return (f"Category: {result['predicted_category']}\n"
                f"Sentiment: {result['sentiment']}\n"
                f"POS tags: {result['pos_tags']}\n"
                f"Text: {result['text'][:200]}...")
    
    elif intent['action'] == 'translate':
        return f"Translation: {result[:300]}..."
    
    elif intent['action'] == 'summarize':
        return f"Summary: {result}"
    
    elif intent['action'] == 'NER':
        entities_txt = ", ".join([f"{ent} ({label})" for ent, label in result[:5]])
        return f"Entities found: {entities_txt}"
    
    elif intent['action'] == 'detect':
        return f"Detected language: {result}"
