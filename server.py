from flask import Flask, jsonify, send_from_directory, request
from datetime import datetime
import os

app = Flask(__name__)

# Example updates data
UPDATES = [
    {"user": "Owner", "date": "2025-09-08", "time": "14:30", "detail": "Added dark mode with persistent setting."},
    {"user": "Owner", "date": "2025-09-07", "time": "10:15", "detail": "Moved styles to style.css for better maintainability."},
    {"user": "Owner", "date": "2025-09-06", "time": "16:45", "detail": "Created sitemap.xml for SEO."},
    {"user": "Owner", "date": "2025-09-05", "time": "09:00", "detail": "Initial project setup and repository view."}
]

@app.route('/')
def home():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'style.css')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'sitemap.xml')

@app.route('/README.md')
def readme():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'README.md')

@app.route('/updates', methods=['GET'])
def get_updates():
    return jsonify(UPDATES)

@app.route('/update/<int:update_id>', methods=['POST'])
def update_message(update_id):
    data = request.get_json()
    if 0 <= update_id < len(UPDATES):
        UPDATES[update_id]['detail'] = data.get('detail', UPDATES[update_id]['detail'])
        return jsonify({'status': 'success', 'message': 'Update modified.'})
    return jsonify({'status': 'error', 'message': 'Update not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
