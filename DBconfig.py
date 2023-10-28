from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = '2399'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sumanth@99@localhost:3306/demo'
db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True)
