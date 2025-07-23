import csv
from flask import Flask, request, render_template
import json

app = Flask(__name__)

data = []

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        
        data.append({
            'product_id': len(data) + 1,
            'product_name': name,
            'category': category,
            'price': int(price)
        })
        
        writeInJSON()
        print(f'id : {len(data)}')
        print(f'Product name : {name}')
        print(f'Category : {category}')
        print(f'Price : {price}')

        return f'{name} added successfully to products!'
    
    return render_template('form.html')

@app.route('/products')
def getAllProducts():
    return render_template("products.html", products=data)

def read_csv():
    with open('products.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append({ 'product_id': int(row[0]), 'product_name': row[1], 'category': row[2], 'price': int(row[3]) })
            print(f'id : {row[0]}, Product name : {row[1]}, Category : {row[2]}, Price : {row[3]}')

def writeInJSON():
    with open('products.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    writeInCSV()

def writeInCSV():
    with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow({'product_id','product_name','category','price'})
            for row in data:
                writer.writerow([row['product_id'], row['product_name'], row['category'], row['price']])

if __name__ == '__main__':
    read_csv()
    writeInJSON()
    app.run(debug=True)