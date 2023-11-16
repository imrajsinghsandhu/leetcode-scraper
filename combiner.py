import os, json

combined_data = []

directory = './scraped_data'

# Loop through each JSON file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            data = json.load(file)
            combined_data.extend(data)

# Add unique IDs starting from 0
for i, question in enumerate(combined_data):
    question['id'] = i

# Write the combined data to a new JSON file
output_file = 'leetcode_questions.json'
with open(output_file, 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)

print(f"Combined data from {len(os.listdir(directory))} files into {len(combined_data)} questions.")
print(f"Saved the combined data to {output_file}.")