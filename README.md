# Building a RESTful API with Flask - Error Handling, Authentication,and File Handling with Public and Admin Routes


Project Team Members :
Sumanth Mittapally(CWID : 885157511),
Rohit Chowdary Yadla (CWID : 885146852)

# Project Description 

This project is focused on developing a feature-rich RESTful API using the Flask framework. Key features include comprehensive error handling, robust JWT (JSON Web Token) authentication for secure user access, and secure file handling with validations on file types and sizes. It serves as a Python based template for creating Flask APIs with these essential features and includes a detailed readme for easy setup and deployment, making it a valuable resource for web and mobile application development.

#Drive Link For the Project Demonstration and Screenshots
https://drive.google.com/drive/folders/1SJhZYH80XomVbagyrl40h_x7m11TOvZX?usp=sharing
## Prerequisites

Before you begin, ensure that you have the following prerequisites:

- Python (3.6 or higher) installed on your system.

Create a Python virtual environment to isolate the application's dependencies:

python -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install the required packages using pip:

Like pip install Flask flask_sqlalchemy pymysql

Configuration
1.	Open the Flask application file (app.py) and make sure to configure the following settings:
•	SECRET_KEY: Set this to a secret key for your application.
•	SQLALCHEMY_DATABASE_URI: Set this to the correct URI for your MySQL database.

Running the Application
1.	In the terminal, navigate to the project directory where app.py is located.
2.	To start the Flask application, use the following command:

flask run 
The application will be accessible at http://localhost:5000 in your web browser.

Accessing the Application
Once the application is running, you can access it by opening your web browser and navigating to http://localhost:5000.

ERROR HANDLING :

Application Usage
•	The Flask application handles custom error handling for various HTTP error codes:
•	404 (Not Found)
•	401 (Unauthorized)
•	400 (Bad Request)
•	500 (Internal Server Error)
•	You can access different routes to test these error responses, such as:
•	/unauthorized to simulate a 401 error (Unauthorized)
•	/check_age to check if a provided age is valid (with potential 400 error)
•	/trigger_error to simulate a 500 error (Internal Server Error)
•	The application responds with appropriate error messages based on the route you access.

AUTHENTICATION :

Application Usage
•	The Flask application provides user authentication using JWT (JSON Web Tokens).
•	You can access the following routes:
1.	/login (POST) - Use this route to log in with a username and password. It will return a JWT access token if the credentials are valid.
2.	/protected (GET) - This route is protected and requires a valid JWT token. You need to include the JWT token in the request header to access it.
•	To test the application, you can use tools like Postman or cURL to send HTTP requests with JWT tokens.
Application Configuration
•	The secret key for JWT tokens is configured in the app.config['JWT_SECRET_KEY'] variable. You should replace it with your secret key in a production environment.
•	User authentication in this example is simplified, and you should replace the users dictionary with a proper user database in a real-world application.

FILEHANDLING :

Application Usage
•	The Flask application provides a file upload feature with the following endpoints:
1.	/upload-form (GET) - This route displays an HTML form for file uploads.
2.	/upload (POST) - Use this route to upload files. You can test the file upload functionality by submitting files through this route.
Application Configuration
•	The application is configured to accept files with specific extensions defined in the ALLOWED_EXTENSIONS set (e.g., txt, pdf, png, jpg, jpeg, gif).
•	The maximum file size allowed is set to 16MB (16 * 1024 * 1024 bytes), which you can modify in the MAX_CONTENT_LENGTH variable.
•	The default upload folder location is set to /Users/sumanthmittapally/Flask_intro/uploads. You should change this to your desired folder location.

PUBLIC ROUTE :

 Application Usage
•	The Flask application provides a simple route at /public/items (GET) to retrieve a list of public items. You can customize the items in the public_items list in the app.py file.
•	You can modify the list of public items and the application to serve more complex data if needed.

SERVICES :

Application Usage
•	The Flask application interacts with a MySQL database to manage items. It provides routes to create, retrieve, update, and delete items.
•	You can use tools like Postman or cURL to make API requests to these routes for testing and interacting with the application.
•	Customize the application as needed, and expand it to serve more complex data or functionality.


