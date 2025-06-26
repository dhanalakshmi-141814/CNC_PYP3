from pathlib import Path
import string

# Input and output file paths
input_path = Path("input.txt")
output_path = Path("word_count_output.txt")

# Ensure the input file exists
if not input_path.exists():
    print(f"Input file {input_path} not found.")
    exit()

# Read file content
with input_path.open("r", encoding="utf-8") as file:
    text = file.read()

# Normalize text: remove punctuation, convert to lowercase
translator = str.maketrans("", "", string.punctuation)
cleaned_text = text.translate(translator).lower()

# Count word frequencies
word_counts = {}
for word in cleaned_text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

# Write word counts to output file
with output_path.open("w", encoding="utf-8") as out_file:
    for word, count in sorted(word_counts.items()):
        out_file.write(f"{word}: {count}\n")

print(f"Word count written to {output_path}")