from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple dictionary for username and password validation.
# In real applications, this data should be stored in a secure database.
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['POST'])
def login():
    # Receive the JSON data sent.
    data = request.get_json()
    
    # Check the username and password.
    username = data.get('username')
    password = data.get('password')
    
    # Validate if the username and password are correct.
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid username or password", "status": "failure"}), 401

if __name__ == '__main__':
    app.run(debug=True)
