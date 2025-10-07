import spacy

# Step 1: Load English model with word vectors
nlp = spacy.load("en_core_web_md")  # Or 'en_core_web_lg' for better vectors

# Step 2: Input sentence
sentence = "The doctor prescribed medicine to the patient."

# Step 3: Process the sentence
doc = nlp(sentence)

# Step 4: Semantic vector representation (sentence-level meaning)
print("Semantic Vector (first 10 dimensions):")
print(doc.vector[:10])  # Show first 10 numbers for simplicity

# Step 5: Dependency-based semantic structure
print("\nDependency Structure:")
for token in doc:
    print(f"{token.text:12} --> {token.dep_:10} --> {token.head.text}")

# Step 6: Named Entity Recognition (semantic units)
print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text:20} --> {ent.label_}")
