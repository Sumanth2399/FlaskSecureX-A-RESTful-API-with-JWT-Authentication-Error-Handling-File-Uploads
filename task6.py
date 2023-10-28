from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sumanth99@localhost:3306/demo'
db = SQLAlchemy(app)

# Create a model for your items
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Route to create a new item (POST request)
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' in data and 'description' in data:
        new_item = Item(name=data['name'], description=data['description'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify(message='Item created successfully'), 201
    else:
        return jsonify(error='Invalid data format'), 400

# Route to retrieve all items (GET request)
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    item_list = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
    return jsonify(items=item_list)

# implement GET, PUT, and DELETE routes for specific items by ID 
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    # Lookup the item by item_id and update it with data
    
    return jsonify(message='Item updated successfully')

# Route to delete a specific item by ID (DELETE request)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item is not None:
        db.session.delete(item)
        db.session.commit()
        return jsonify(message='Item deleted successfully')
    else:
        return jsonify(error='Item not found'), 404


if __name__ == '__main__':
    app.run(debug=True)
