import json
from flask import Flask, jsonify, request
from mysql.connector import Error
from db import get_db_connection, initialize_database

app = Flask(__name__)

initialize_database()

def addJSONtoDB():
    try:
        with open('products.json', mode='r') as json_file:
            jsonData = json.load(json_file)

        def insertDB(data):
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            try:
                values = (data['id'], data['name'], data['description'], float(data['price']), int(data['stock']))
                sql = '''
                    INSERT INTO products (id, name, description, price, stock)
                    VALUES (%s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        name = VALUES(name),
                        description = VALUES(description),
                        price = VALUES(price),
                        stock = VALUES(stock)
                '''
                cursor.execute(sql, values)
                connection.commit()
            except Error as e:
                print(f"error: {e}")
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        for row in jsonData:
            insertDB(row)

    except Error as e:
        print(f"MySQL error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")


@app.route('/products', methods=['GET'])
def getAllProducts():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        return jsonify({
            'products': products,
            'success' : True,
            'message' : 'All the products have been fetched',
        }), 200
    except Error as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/products/<int:id>', methods=['GET'])
def getProductByID(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products WHERE id = %s', (id,))
        product = cursor.fetchone()
        if product:
            return jsonify({
                'product': product,
                'success': True,
                'message': 'Product has been fetched',
            }), 200
        return jsonify({
            'success': False,
            'message': 'Product does not exist',
        })
    except Error as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/products', methods=['POST'])
def createProduct():
    try:
        required_fields = ['name', 'description', 'price', 'stock']
        data = request.get_json()
        if not data or not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        values = (data['name'], data['description'], data['price'],data['stock'])
        cursor.execute('INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s)', values)
        connection.commit()

        return jsonify({
            'success': True,
            'message': 'Product has been created'
        }), 201
    except Error as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/products/<int:id>', methods=['PUT'])
def updateProduct(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        required_fields = ['name', 'description', 'price', 'stock']
        data = request.get_json(silent=True)
        if not data or not any(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400


        if 'name' in data and data['name']:
            cursor.execute('UPDATE products SET name = %s WHERE id = %s', (data['name'], id))
        if 'description' in data and data['description']:
            cursor.execute('UPDATE products SET description = %s WHERE id = %s', (data['description'], id))
        if 'price' in data and data['price']:
            cursor.execute('UPDATE products SET price = %s WHERE id = %s', (data['price'], id))
        if 'quantity' in data and data['stock']:
            cursor.execute('UPDATE products SET stock = %s WHERE id = %s', (data['stock'], id))
        
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({
                'success': False,
                'message': 'Product does not exist',
            }), 404

        return jsonify({
            'success': True,
            'message': 'Product has been updated'
        }), 200
    except Error as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
    finally:
        if connection.is_connected():
            connection.close()

@app.route('/products/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('DELETE FROM products WHERE id = %s', (id,))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({
                'success': False,
                'message': 'Product does not exist',
            }), 404

        return jsonify({
            'success': True,
            'message': 'Product has been deleted',
        }), 200
    except Error as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    addJSONtoDB()
    app.run(debug=True)