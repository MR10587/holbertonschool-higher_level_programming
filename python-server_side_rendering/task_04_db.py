from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    error = None  

    try:
        if source == 'json':
            with open('products.json', encoding='utf-8') as f:
                products = json.load(f)
        elif source == 'csv':
            with open('products.csv', encoding='utf-8') as f:
                products = list(csv.DictReader(f))
        elif source == 'sql':
            with sqlite3.connect('products.db') as conn:
                cursor = conn.cursor()P
                cursor.execute('SELECT name, category, price FROM Products')

                products = cursor.fetchall()
        else:
            error = "Wrong source"     
            products = []           
    except FileNotFoundError:
        error = "Data file not found"
        products = []
    except json.JSONDecodeError:
        error = "Invalid JSON format" 
        products = []

    # CHANGED: filter by actual product["id"]
    if error is None and product_id is not None:
        found = None
        for p in products:
            try:
                if int(p.get("id")) == product_id:
                    found = p
                    break
            except (TypeError, ValueError):
                continue

        if found:
            products = [found]
        else:
            error = "Product not found"
            products = []

    return render_template('product_display.html', products=products, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
