import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Step 1: Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Step 2: Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Step 3: Input text
text = "The children are playing in the gardens. They played well and were running fast."

# Step 4: Tokenize text
tokens = word_tokenize(text)

# Step 5: Lemmatize each word (default POS: noun)
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

# Step 6: Output result
print("Original Tokens:")
print(tokens)

print("\nLemmatized Tokens:")
print(lemmatized_words)
