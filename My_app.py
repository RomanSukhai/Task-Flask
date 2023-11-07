from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Припустимо, що у нас є певний набір продуктів в пам'яті для прикладу
products = [
    {"id": "1", "name": "Product 1", "price": 10.0, "stock": 100},
    # Додати інші продукти за потреби
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def create_product():
    if not request.json or not 'name' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'name': request.json['name'],
        'price': request.json.get('price', 0),
        'stock': request.json.get('stock', 0)
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/api/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product is None:
        abort(404)
    return jsonify(product)

@app.route('/api/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product is None:
        abort(404)
    if not request.json:
        abort(400)
    product['name'] = request.json.get('name', product['name'])
    product['price'] = request.json.get('price', product['price'])
    product['stock'] = request.json.get('stock', product['stock'])
    return jsonify(product)

@app.route('/api/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [prod for prod in products if prod['id'] != product_id]
    return jsonify({'result': True})

@app.route('/api/orders', methods=['POST'])
def create_order():
    if not request.json or not 'productId' in request.json:
        abort(400)
    # Тут має бути логіка для створення замовлення
    return jsonify({'result': 'Order placed'}), 201

if __name__ == '__main__':
    app.run(debug=True)
