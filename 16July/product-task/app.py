from flask import Flask, request, jsonify

products = [
    {"id": 1, "name": "Laptop", "price": 55000.0, "quantity": 10},
    {"id": 2, "name": "Mobile", "price": 15000.0, "quantity": 25},
    {"id": 3, "name": "Headphones", "price": 2000.0, "quantity": 50},
    {"id": 4, "name": "Smartwatch", "price": 5000.0, "quantity": 30},
    {"id": 5, "name": "Keyboard", "price": 700.0, "quantity": 40},
    {"id": 6, "name": "Mouse", "price": 400.0, "quantity": 45},
    {"id": 7, "name": "External Hard Drive", "price": 3500.0, "quantity": 15},
    {"id": 8, "name": "Pen Drive", "price": 500.0, "quantity": 100},
    {"id": 9, "name": "Monitor", "price": 12000.0, "quantity": 12},
    {"id": 10, "name": "Printer", "price": 8000.0, "quantity": 8},
    {"id": 11, "name": "Router", "price": 2200.0, "quantity": 20},
    {"id": 12, "name": "Speakers", "price": 2500.0, "quantity": 25},
    {"id": 13, "name": "Webcam", "price": 1800.0, "quantity": 18},
    {"id": 14, "name": "Projector", "price": 25000.0, "quantity": 5},
    {"id": 15, "name": "Graphic Tablet", "price": 6500.0, "quantity": 7}
]

app = Flask(__name__)


@app.route("/products", methods=["GET"])
def getAll():
    return jsonify(products), 200

@app.route("/product/<int:id>", methods=["GET"])
def getById(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    return jsonify({"error" : "product not found"}), 405

@app.route("/product", methods=["POST"])
def addProduct():
    data = request.get_json()
    products.append(data)
    return jsonify(data), 201

@app.route("/product/<int:id>", methods=["PUT"])
def updateProduct(id):
    data = request.get_json()
    for product in products:
        if product["id"] == id:
            product.update(data)
            return jsonify({
                "product" : product,
                "message" : "Product updated successfully"
            }), 200

    return jsonify({"error" : "product not found"}), 405

@app.route("/product/<int:id>", methods=["DELETE"])
def deleteProduct(id):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return jsonify({"message" : "Product deleted"}), 200
    return jsonify({"error" : "product not found"}), 405


if __name__ == '__main__':
    app.run(debug=True)