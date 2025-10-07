import nltk
from nltk.tokenize import sent_tokenize

# Step 1: Download required tokenizer data
nltk.download('punkt')

# Step 2: Input text (example paragraph)
text = "Machine Learning is a growing field. It allows systems to learn from data. This is an example of sentence tokenization."

# Step 3: Perform sentence tokenization
sentences = sent_tokenize(text)

# Step 4: Output the result
print("Original Text:")
print(text)
print("\nSentence Tokens:")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}. {sentence}")
