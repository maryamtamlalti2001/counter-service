from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect
import os
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)

# Define the file's path to store the data
COUNTER_FILE = "./data/counter.txt"

# Function to read the counter from file
def read_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    else:
        return 0

# Function to update the counter in the file
def update_counter(counter):
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))

# Route to handle GET request for retrieving the counter
@app.route('/', methods=['GET'])
def get_counter():
    counter = read_counter()
    return f"Current POST requests count: {counter}"

# Route to handle POST request to increment the counter
@app.route('/', methods=['POST'])
def increment_counter():
    counter = read_counter()
    counter += 1
    update_counter(counter)
    return jsonify({"message": "POST requests counter updated", "new_counter": counter})

# Health check route
@app.route('/health', methods=["GET"])
def health_check():
    try:
        # Basic health check: Ensure the counter file is accessible
        read_counter()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
