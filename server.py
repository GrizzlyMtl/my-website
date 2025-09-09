from flask import Flask, jsonify, send_from_directory, request
from datetime import datetime
import os

class WebsiteServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.UPDATES = [
            {"user": "Owner", "date": "2025-09-08", "time": "14:30", "detail": "Added dark mode with persistent setting."},
            {"user": "Owner", "date": "2025-09-07", "time": "10:15", "detail": "Moved styles to style.css for better maintainability."},
            {"user": "Owner", "date": "2025-09-06", "time": "16:45", "detail": "Created sitemap.xml for SEO."},
            {"user": "Owner", "date": "2025-09-05", "time": "09:00", "detail": "Initial project setup and repository view."},
            {"user": "Owner", "date": "2025-09-04", "time": "11:00", "detail": "Committed to regular updates and transparency."},
            {"user": "Owner", "date": "2025-09-03", "time": "15:30", "detail": "Committed to improving accessibility features."},
            {"user": "Owner", "date": "2025-09-02", "time": "13:20", "detail": "Committed to open source contributions."}
        ]
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

        @self.app.route('/style.css')
        def style():
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'style.css')

        @self.app.route('/sitemap.xml')
        def sitemap():
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'sitemap.xml')

        @self.app.route('/README.md')
        def readme():
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'README.md')

        @self.app.route('/updates', methods=['GET'])
        def get_updates():
            return jsonify(self.UPDATES)

        # Add other routes as needed...

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    server = WebsiteServer()
    server.run()