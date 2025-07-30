import re
from striprtf.striprtf import rtf_to_text

# Read and convert RTF to plain text
with open('file 1.rtf', 'r', encoding='utf-8') as f:
    rtf_content = f.read()

text = rtf_to_text(rtf_content)

# Split the entries by their markers
entries = re.split(r'#\s*\d{1,3}:\s*', text)

# Clean and filter entries
entries = [entry.strip().replace('<br><br>', ' ') for entry in entries if entry.strip()]

# Remove duplicates
seen = set()
unique_entries = []
for entry in entries:
    if entry not in seen:
        unique_entries.append(entry)
        seen.add(entry)

# Reformat and output
formatted_entries = [f"#{i+1}: {entry}" for i, entry in enumerate(unique_entries)]

cleaned_text = '\n\n'.join(formatted_entries)
print(cleaned_text)
