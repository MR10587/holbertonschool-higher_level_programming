from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    try:
        if source == 'json':
            with open('products.json', encoding='utf-8') as f:
                products = json.load(f)
        elif source == 'csv':
            with open('products.csv', encoding='utf-8') as f:
                products = list(csv.DictReader(f))
        else:
            return "Wrong source"
    except FileNotFoundError:
        return "Data file not found"
    except json.JSONDecodeError:
        return "Invalid JSON format"

    if product_id is not None:
        if 1 <= product_id <= len(products):
            products = [products[product_id - 1]]
        else:
            return "Product not found"

    return render_template('product_display.html', products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
