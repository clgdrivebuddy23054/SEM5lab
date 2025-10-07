import string

# Step 1: Input text
text = "Hello! Welcome to Machine Learning, NLP & AI. Let's clean: this text."

# Step 2: Remove punctuation
cleaned_text = ''.join(char for char in text if char not in string.punctuation)

# Step 3: Output result
print("Original Text:")
print(text)
print("\nText without Punctuation:")
print(cleaned_text)
