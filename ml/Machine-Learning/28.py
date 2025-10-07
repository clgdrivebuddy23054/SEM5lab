from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Step 1: Sample documents
documents = [
    "Machine learning is fun and powerful.",
    "Python is great for machine learning.",
    "Statistics is an important part of data science.",
    "Data science includes machine learning and statistics."
]

# Step 2: Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Step 3: Fit and transform the documents
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Step 4: Convert to DataFrame for better readability
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Step 5: Output the TF-IDF matrix
print("TF-IDF Matrix:\n")
print(tfidf_df.round(3))
