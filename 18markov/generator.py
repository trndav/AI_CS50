# python generator.py sample.txt

import markovify
import sys

# Read text from file
if len(sys.argv) != 2:
    sys.exit("Usage: python generator.py sample.txt")
with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

# Generate sentences that does not appear in text
print()
for i in range(5):
    print(text_model.make_sentence())
    print()
