from datetime import date
from itertools import count
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Free API for exchange rates (exchangerate-api.com)
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json(force=True)  # expects { "from": "USD", "to": "INR", "amount": 10 }
    from_currency = data.get('from')
    to_currency = data.get('to')
    amount = float(data.get('amount'))

    if not from_currency or not to_currency or not amount: 
        return jsonify({"error": "Missing required fields"}), 400

    # Fetch rates from API
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    if response.status_code != 200:
        return jsonify({"error": "API request failed"}), 500

    rates = response.json().get("rates")
    if not rates or to_currency not in rates:
        return jsonify({"error": "Invalid currency"}), 400

    converted_amount = float(amount) * rates[to_currency]
    return jsonify({"result": converted_amount})


if __name__ == '__main__':
    app.run(debug=True)
