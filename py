import re

# Load your text into this variable
text = file 1.rtf

# Split the entries by their original markers (e.g., "#1:", "#2:", etc.)
entries = re.split(r'#\d{1,3}:\s?', text)

# Remove any empty strings
entries = [entry.strip().replace('<br><br>', ' ') for entry in entries if entry.strip()]

# Remove duplicates while preserving order
seen = set()
unique_entries = []
for entry in entries:
    if entry not in seen:
        unique_entries.append(entry)
        seen.add(entry)

# Re-number and format the cleaned entries
formatted_entries = [f"#{i+1}: {entry}" for i, entry in enumerate(unique_entries)]

# Output result
cleaned_text = '\n\n'.join(formatted_entries)
print(cleaned_text)
