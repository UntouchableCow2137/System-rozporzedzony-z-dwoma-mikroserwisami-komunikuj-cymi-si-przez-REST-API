from flask import Flask, jsonify, abort

app = Flask(__name__)


products = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Smartphone", "price": 2300.00},
    3: {"id": 3, "name": "Tablet", "price": 1500.00}
}

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product)

if __name__ == '__main__':
   
    app.run(port=8001)

