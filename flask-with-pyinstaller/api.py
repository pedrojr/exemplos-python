from flask import Flask, request, jsonify

app = Flask(__name__)
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' in data:
        item = {
            'id': len(items) + 1,
            'name': data['name'],
            'description': data.get('description', '')
        }
        items.append(item)
        return jsonify(item), 201
    else:
        return jsonify({'error': 'O campo "name" é obrigatório'}), 400

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item não encontrado'}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item['name'] = data.get('name', item['name'])
            item['description'] = data.get('description', item['description'])
            return jsonify(item)
    return jsonify({'error': 'Item não encontrado'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            return '', 204
    return jsonify({'error': 'Item não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
