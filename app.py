from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audioFile' not in request.files:
        return 'No file part', 400

    file = request.files['audioFile']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        # Placeholder for processing logic
        return f"File {file.filename} uploaded successfully!", 200

if __name__ == '__main__':
    app.run(debug=True)
