import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Step 1: Download tokenizer
nltk.download('punkt')

# Step 2: Initialize the stemmer
stemmer = PorterStemmer()

# Step 3: Input text
text = "The children were playing games, and they played very actively while running in the field."

# Step 4: Tokenize the text
tokens = word_tokenize(text)

# Step 5: Apply stemming
stemmed_words = [stemmer.stem(word) for word in tokens]

# Step 6: Output results
print("Original Words:")
print(tokens)

print("\nStemmed Words:")
print(stemmed_words)
