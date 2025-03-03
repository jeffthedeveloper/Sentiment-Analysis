from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Exemplo simples de spam detection
def train_spam_classifier(data, labels):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data)
    clf = MultinomialNB()
    clf.fit(X, labels)
    return clf, vectorizer

# Exemplo de uso
data = ['Win money now', 'Hello, how are you?', 'Free lottery', 'Good morning']
labels = [1, 0, 1, 0]  # 1 = spam, 0 = not spam
model, vectorizer = train_spam_classifier(data, labels)

test_data = ['Free money']
test_vector = vectorizer.transform(test_data)
prediction = model.predict(test_vector)
print(prediction)  # 1 for spam
