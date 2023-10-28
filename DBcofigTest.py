from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text  # Import the text function

app = Flask(__name__)
app.config['SECRET_KEY'] = '2399'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sumanth99@localhost:3306/demo'


db = SQLAlchemy(app)

@app.route('/')
def test_db_connection():
    try:
        # Explicitly declare the SQL expression as a text object
        result = db.session.execute(text('SELECT 1'))
        # If the query was successful, the connection is working
        return 'Database connection is successful'
    except Exception as e:
        # If there's an exception, the connection may not be working
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
