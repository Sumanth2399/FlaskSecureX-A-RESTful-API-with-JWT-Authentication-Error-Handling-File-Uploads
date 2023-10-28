from flask import Flask, jsonify

app = Flask(__name__)

# Define a list of public items 
public_items = ['item1', 'item2', 'item3']

# Public route to retrieve the list of public items
@app.route('/public/items', methods=['GET'])
def get_public_items():
    return jsonify(items=public_items)

if __name__ == '__main__':
    app.run(debug=True)
