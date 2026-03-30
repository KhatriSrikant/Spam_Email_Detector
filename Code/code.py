import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("spam.csv")

df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# Features and target
X = df['text']
y = df['label_num']

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

print("Spam Email Detector")
print("Type 'exit' to stop\n")

while True:
    exit = input("Enter your message: ")

    if exit.lower() == 'exit':
        print("Loading...")
        break

    input_data = vectorizer.transform([exit])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        print("Spam Message\n")
    else:
        print("Not Spam\n")
