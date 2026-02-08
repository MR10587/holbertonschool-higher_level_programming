# Importing necessary modules and functions
from flask import Flask, render_template, request
import json
import csv

# Creating flask app
app = Flask(__name__)

# Route to products
@app.route('/products')
# Function to show in right route
def products():
    # Get source and ID
    source = request.args.get('source')
    id = request.args.get('id',type=int)

    # Validate source
    try:
        if source == 'json':
            with open('products.json') as f:
                products = json.load(f)
        elif source == 'csv':
            with open('products.csv') as f:
                products = list(csv.DictReader(f))
        else:
            return "Wrong source"
    except FileNotFoundError:
        return "Data file not found"
    except json.JSONDecodeError:
        return "Invalid JSON format"
    
    # Validate ID
    if id is not None:
        if 1 <= id <= len(products):
            products = [products[id - 1]]
        else:
            return "Product not found"

    # Render HTML file
    return render_template('product_display.html', products = products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
