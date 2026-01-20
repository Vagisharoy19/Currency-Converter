# Currency-Converter
A Flask-based currency converter web app that uses live exchange rates via a free API. Users can enter an amount, choose source and target currencies, and instantly see results. Built with Python, Flask, HTML, CSS, and JavaScript, it features real‑time data, supports popular currencies, and includes error handling for invalid inputs.


# Currency Converter

A simple full-stack currency converter built with Python and Flask.

## Features

- Convert between multiple currencies
- Real-time exchange rates from exchangerate-api.com
- Clean, responsive web interface
- Beginner-friendly code structure

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`

3. Enter the amount, select currencies, and click "Convert"

## Project Structure

- `app.py`: Main Flask application with API endpoints
- `templates/index.html`: Frontend HTML template
- `requirements.txt`: Python dependencies
- `README.md`: This file

## API Endpoint

- `GET /`: Serves the main page
- `POST /convert`: Converts currency (expects JSON with amount, from_currency, to_currency)

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **API**: exchangerate-api.com (free tier)

## Learning Objectives

This project demonstrates:
- Setting up a Flask web application
- Making API requests with Python
- Handling form submissions with JavaScript
- Basic currency conversion logic
- Structuring a simple full-stack application

## Customization

Feel free to:
- Add more currencies to the dropdown
- Implement user authentication
- Add historical exchange rate charts
- Improve the UI with a framework like Bootstrap

## License

This project is open source and available under the MIT License.
