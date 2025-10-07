import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Step 1: Download NLTK stopwords and tokenizer models
nltk.download('punkt')
nltk.download('stopwords')

# Step 2: Sample input text
text = "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data."

# Step 3: Preprocessing - Lowercase, remove punctuation
text = text.lower()
text = ''.join([char for char in text if char not in string.punctuation])

# Step 4: Tokenize text
words = word_tokenize(text)

# Step 5: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Step 6: Output
print("Original Text:")
print(text)
print("\nAfter Stopword Removal:")
print(filtered_words)
