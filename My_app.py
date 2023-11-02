from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

VARIANT_NUMBER = 20

@app.route(f"/api/v1/hello-world-{VARIANT_NUMBER}")
def hello_world():
    """
    Hello World endpoint
    ---
    responses:
      200:
        description: A simple hello world
    """
    return jsonify(message=f"Hello World {VARIANT_NUMBER}"), 200

@app.route('/products', methods=['GET'])
@swag_from('ymls/products.yml')
def get_products():
    products = [
        {"id": 1, "name": "Product 1", "price": 10.0},
        {"id": 2, "name": "Product 2", "price": 20.0},

    ]
    return jsonify(products)

@app.route('/api/order', methods=['POST'])
@swag_from('ymls/create_order.yml')
def create_order():
     return jsonify(order_id=123), 201


@app.route('/order/<int:order_id>', methods=['DELETE'])
@swag_from('ymls/delete_order.yml')
def delete_order(order_id):
    return jsonify(message="Order deleted."), 200

if __name__ == "__main__":
    app.run()
