import nltk
from nltk.tokenize import word_tokenize
import string

# Step 1: Download required NLTK resources
nltk.download('punkt')

# Step 2: Input text (example)
text = "Machine Learning enables computers to learn from data and make predictions."

# Step 3: Preprocessing - Convert to lowercase
text = text.lower()

# Step 4: Remove punctuation
text = ''.join(char for char in text if char not in string.punctuation)

# Step 5: Tokenize the text into words
tokens = word_tokenize(text)

# Step 6: Output the tokens
print("Original Text:")
print(text)
print("\nWord Tokens:")
print(tokens)
