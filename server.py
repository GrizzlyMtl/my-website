from flask import Flask, jsonify, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

# Example updates data
UPDATES = [
    {"date": "2025-09-08", "detail": "Added dark mode with persistent setting."},
    {"date": "2025-09-07", "detail": "Moved styles to style.css for better maintainability."},
    {"date": "2025-09-06", "detail": "Created sitemap.xml for SEO."},
    {"date": "2025-09-05", "detail": "Initial project setup and repository view."}
]

@app.route('/')
def home():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/updates', methods=['GET'])
def get_updates():
    return jsonify(UPDATES)

if __name__ == '__main__':
    app.run(debug=True)
