from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Define the path to the JSON file
DATA_FILE = '../ui/json/data.json'

# Function to load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Function to save data to JSON file
def save_data(new_data):
    data = load_data()
    data.append(new_data)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Route for the form entry page
@app.route('/')
def entry_page():
    return render_template('attending.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_data():
    # Get form data
    name = request.form['name']
    age = request.form['age']
    occupation = request.form['occupation']

    # Create a new data entry
    new_entry = {
        "name": name,
        "age": int(age),
        "occupation": occupation
    }

    # Save the new data entry to the JSON file
    save_data(new_entry)

    # Redirect back to the form or a success page
    return redirect(url_for('entry_page'))

# API to view all the data (optional)
@app.route('/data', methods=['GET'])
def view_data():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
