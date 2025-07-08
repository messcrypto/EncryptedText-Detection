import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

# قراءة البيانات من ملف CSV
df = pd.read_csv('data.csv')

# ميزات البيانات
X = df['text']
y = df['label']

# تحويل النصوص إلى متجهات
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# تدريب النموذج
model = BernoulliNB()
model.fit(X_vec, y)

# تجربة النموذج على جمل جديدة
test_sentences = [
    "Hello, how are you?",
    "kzjvnsdklvnsdlvnsd", 
    "Encrypted text example",
    "This is a regular message"
]

for sentence in test_sentences:
    sentence_vec = vectorizer.transform([sentence])
    prediction = model.predict(sentence_vec)[0]
    print(f"{sentence} => {'Encrypted' if prediction == 1 else 'Not Encrypted'}")
