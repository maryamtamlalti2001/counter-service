from flask import Flask, jsonify, request
from flask_wtf.csrf import CSRFProtect, generate_csrf
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)

# Define the file's path to store the data
COUNTER_FILE = "./data/counter.txt"

def read_counter():
    """ Function to read the counter from file. """
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    else:
        return 0

def update_counter(counter):
    """ Function to update the counter in the file. """
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))

@app.route('/', methods=['GET'])
def get_counter():
    """ Route to handle GET request for retrieving the counter and CSRF token. """
    counter = read_counter()
    # Generate CSRF token and return it along with the counter value
    csrf_token = generate_csrf()
    return jsonify({
        "counter": counter,
        "csrf_token": csrf_token
    })

@app.route('/', methods=['POST'])
def increment_counter():
    """ Route to handle POST request to increment the counter. """
    counter = read_counter()
    counter += 1
    update_counter(counter)
    return jsonify({"message": "POST requests counter updated", "new_counter": counter})

@app.route('/health', methods=['GET'])
def health_check():
    """ Health check route to ensure the application is running properly. """
    try:
        # Basic health check: Ensure the counter file is accessible
        read_counter()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
