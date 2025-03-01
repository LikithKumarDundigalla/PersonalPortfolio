import os
from flask import Flask, render_template, send_from_directory, Response
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

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

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500