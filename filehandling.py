from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the allowed file extensions and maximum file size
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Setting the upload folder location 
app.config['UPLOAD_FOLDER'] = '/Users/sumanthmittapally/Flask_intro/uploads'

# Ensure the uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check if a file has an allowed file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-form')
def serve_upload_form():
    # HTML content as a string
    html_content = """
    <!doctype html>
    <html>
    <head>
        <title>Upload Form</title>
    </head>
    <body>
        <h1>File Upload Form</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    """
    return html_content

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has a file part
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify(error='No selected file'), 400

    # Check if the file has an allowed file extension
    if not allowed_file(file.filename):
        return jsonify(error='Invalid file type'), 400

    # Check if the file size is within the limit
    if len(file.read()) > MAX_CONTENT_LENGTH:
        return jsonify(error='File size exceeds the limit'), 400

    # Secure the filename and save it to the upload folder
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify(message='File uploaded successfully')

if __name__ == '__main__':
    app.run(debug=True)
