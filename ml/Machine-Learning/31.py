from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Sample dataset (text and labels)
texts = [
    "Free money now!!!",
    "Win big cash prizes",
    "Hi, how are you doing?",
    "Let's meet for lunch tomorrow.",
    "Congratulations, you've won a lottery!",
    "Reminder: your appointment is at 3 PM",
    "Click here to claim your reward",
    "Can we reschedule our meeting?",
    "Exclusive deal just for you",
    "See you at the conference"
]

labels = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = ham (non-spam)

# Step 2: Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Step 3: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Step 4: Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 5: Predict and evaluate
y_pred = model.predict(X_test)

print("Predicted labels:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
