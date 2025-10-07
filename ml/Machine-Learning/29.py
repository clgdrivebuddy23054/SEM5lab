import spacy

# Step 1: Load the English language model
nlp = spacy.load("en_core_web_sm")  # Make sure this model is installed

# Step 2: Input text
text = "Barack Obama was born in Hawaii. He was elected president of the United States in 2008."

# Step 3: Process the text
doc = nlp(text)

# Step 4: Extract and print named entities
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text:30} --> {ent.label_}")
