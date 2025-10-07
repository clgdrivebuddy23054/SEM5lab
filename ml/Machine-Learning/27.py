from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Step 1: Sample documents
documents = [
    "Machine learning is super fun.",
    "Python is super, super cool.",
    "Statistics is cool, too.",
    "Data science is fun.",
]

# Step 2: Initialize the vectorizer
vectorizer = CountVectorizer()

# Step 3: Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Step 4: Convert to DataFrame for better visualization
dtm = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Step 5: Output the Document-Term Matrix
print("Document-Term Matrix:\n")
print(dtm)
