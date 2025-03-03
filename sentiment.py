from textblob import TextBlob

# Analisando o sentimento

text = ""I love programming in Python!""
blob = TextBlob(text)
print(f""Sentimento: {blob.sentiment}"")
