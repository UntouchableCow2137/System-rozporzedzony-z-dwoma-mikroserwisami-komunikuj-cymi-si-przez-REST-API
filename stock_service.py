from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)

# Dane stanów magazynowych przechowywane "na sztywno"
stocks = {
    1: {"productId": 1, "quantity": 15},
    2: {"productId": 2, "quantity": 0},
    3: {"productId": 3, "quantity": 5}
}

# Adres Serwisu Produktów
PRODUCT_SERVICE_URL = 'http://localhost:8001/products/'

@app.route('/stock/<int:product_id>', methods=['GET'])
def get_stock(product_id):
    # Sprawdzamy, czy produkt istnieje w Serwisie Produktów
    product_response = requests.get(PRODUCT_SERVICE_URL + str(product_id))
    if product_response.status_code == 404:
        abort(404, description="Product not found in product service")
    elif product_response.status_code != 200:
        abort(500, description="Error contacting product service")

    # Pobieramy stan magazynowy
    stock = stocks.get(product_id)
    if stock is None:
        # Jeżeli brak danych o stanie, zwracamy quantity=0
        return jsonify({"productId": product_id, "quantity": 0})
    return jsonify(stock)

if __name__ == '__main__':
    # Uruchamiamy serwer na porcie 8002
    app.run(port=8002)
