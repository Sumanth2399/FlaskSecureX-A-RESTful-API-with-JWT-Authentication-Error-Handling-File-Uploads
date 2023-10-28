from flask import Flask, jsonify, abort,request
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# generate a function for consistent error format
def error_response(message, status_code):
    response = jsonify(error=message)
    response.status_code = status_code
    return response

# Custom error handler for 404 (Not Found) error
@app.errorhandler(404)
def handle_not_found_error(e):
    return error_response('Resource not found', 404)

# Custom error handler for 401 (Unauthorized) error
@app.errorhandler(401)
def handle_unauthorized_error(e):
    return error_response('Unauthorized', 401)

# Custom error handler for 400 (Bad Request) error
@app.errorhandler(400)
def handle_bad_request_error(e):
    return error_response('Bad Request', 400)

# Custom error handler for 500 (Internal Server Error) error
@app.errorhandler(500)
def handle_internal_server_error(e):
    return error_response('Internal Server Error', 500)

# Route for testing a 401 error
@app.route('/unauthorized')
def unauthorized_route():
    # Simulate an unauthorized access
    abort(401)
    # New endpoint for testing 400 error
@app.route('/check_age', methods=['GET'])
def check_age():
    age = request.args.get('age')
    if not age or not age.isdigit() or int(age) < 18:
        return error_response('Invalid age or age less than 18', 400)
    return jsonify(message='Age is valid')
@app.route('/trigger_error', methods=['GET'])
def trigger_error():
    # Simulate a 500 internal server error
    raise Exception('This is a 500 error')

if __name__ == '__main__':
    app.run(debug=True)
