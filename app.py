import os
from flask import Flask, render_template, send_from_directory, Response, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download-resume')
def download_resume():
    # Check if resume.pdf exists in the static directory
    resume_path = os.path.join(app.static_folder, 'resume.pdf')
    if os.path.exists(resume_path):
        return send_from_directory(app.static_folder, 'resume.pdf')
    else:
        # Return a message if the PDF is not found
        return Response(
            "Please place your resume.pdf file in the static directory to enable downloads.",
            mimetype='text/plain'
        )

# GitHub API mock endpoint (for demonstration purposes)
@app.route('/api/github-activity')
def github_activity():
    # This would typically fetch data from GitHub API
    # For now, we'll return mock data
    mock_data = {
        "stats": {
            "repositories": 20,
            "contributions": 300,
            "pullRequests": 15,
            "openSource": 10
        },
        "recent_commits": [
            {
                "repo": "MenuData.ai",
                "message": "Added RAG implementation with FAISS vector database",
                "type": "commit",
                "date": "2 days ago"
            },
            {
                "repo": "Human-vs-AI-Text-Detection",
                "message": "Improved model accuracy by 15% with feature engineering",
                "type": "commit",
                "date": "1 week ago"
            },
            {
                "repo": "Multi-label-Emotion-Detection",
                "message": "Merged transformer-based model improvements",
                "type": "pull_request",
                "date": "2 weeks ago"
            }
        ]
    }
    return jsonify(mock_data)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
