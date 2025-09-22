from flask import Flask, jsonify, send_from_directory, request
from datetime import datetime
import os

class WebsiteServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.UPDATES = [
            {"User": "Owner", "date": "2025-09-08", "time": "14:30", "detail": "Added dark mode with persistent setting."},
            {"User": "Owner", "date": "2025-09-07", "time": "10:15", "detail": "Moved styles to style.css for better maintainability."},
            {"User": "Owner", "date": "2025-09-06", "time": "16:45", "detail": "Created sitemap.xml for SEO."},
            {"User": "Owner", "date": "2025-09-05", "time": "09:00", "detail": "Initial project setup and repository view."},
            {"User": "Owner", "date": "2025-09-04", "time": "11:00", "detail": "Committed to regular updates and transparency."},
            {"User": "Owner", "date": "2025-09-03", "time": "15:30", "detail": "Committed to improving accessibility features."},
            {"User": "Owner", "date": "2025-09-02", "time": "13:20", "detail": "Committed to open source contributions."}
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

        @self.app.route('/new-idea.html')
        def new_idea():
            return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'new-idea.html')

        @self.app.route('/updates', methods=['GET'])
        def get_updates():
            return jsonify(self.UPDATES)

        @self.app.route('/UpdateIdea', methods=['GET', 'POST'])
        def update_idea():
            if request.method == 'POST':
                idea = request.form.get('idea')
                if not hasattr(self, 'IDEAS'):
                    self.IDEAS = []
                if idea:
                    self.IDEAS.append(idea)
                return ('<script>window.location="/";</script>', 302)
            else:
                return ('<script>window.location="/new-idea.html";</script>', 302)

        # Add other routes as needed...

    def run(self):
        self.app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    server = WebsiteServer()
    server.run()