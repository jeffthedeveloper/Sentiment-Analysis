from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

# Exemplo de uso
text = ""I love Python!""
sentiment = analyze_sentiment(text)
print(sentiment)
