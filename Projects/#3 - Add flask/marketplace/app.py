from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    description = request.form.get('description')
    
    products.append({
        'name': name,
        'price': float(price),
        'quantity': int(quantity),
        'description': description
    })
    
    return redirect(url_for('index'))

@app.route('/remove/<string:name>')
def remove_product(name):
    global products
    products = [product for product in products if product['name'] != name]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
