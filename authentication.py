from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configure JWT settings
app.config['JWT_SECRET_KEY'] = 'sumanth99'  
jwt = JWTManager(app)

# User model 
users = {
    'user1': generate_password_hash('password1'),  # Passwords should be hashed
    'user2': generate_password_hash('password2'),
}

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid username or password'), 401

# Protected endpoint (requires a valid JWT token)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f'Hello, {current_user}! This is a protected resource.')

if __name__ == '__main__':
    app.run(debug=True)
