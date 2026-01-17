import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# 1. Dataset load பண்ணறது
data = pd.read_csv("email-data.csv")

# 2. Features & Labels
X = data['text']
y = data['label']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Text Vectorization
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 5. Model Training
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 6. Model Testing
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Save Model & Vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ New model.pkl & vectorizer.pkl saved successfully!")