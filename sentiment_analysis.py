import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Baixando pacotes necessários do NLTK
nltk.download('vader_lexicon')

# Carregando as frases
data = pd.read_csv('data/sentences.csv')

# Inicializando o analisador de sentimentos
sia = SentimentIntensityAnalyzer()

# Função para classificar o sentimento
def analyze_sentiment(sentence):
    score = sia.polarity_scores(sentence)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Analisando todas as frases
data['Sentiment'] = data['Sentence'].apply(analyze_sentiment)
data.to_csv('data/sentiment_analysis_result.csv', index=False)

print(""Sentiment analysis completed!"")
