import json

# Sample data
data = [
    {"name": "Alice", "age": 28, "occupation": "Engineer"},
    {"name": "Bob", "age": 34, "occupation": "Designer"},
    {"name": "Charlie", "age": 25, "occupation": "Teacher"},
    {"name": "Diana", "age": 30, "occupation": "Doctor"},
]

# Output to a JSON file
with open('./ui/json/data.json', 'w') as f:
    json.dump(data, f)

print("JSON file created successfully.")
