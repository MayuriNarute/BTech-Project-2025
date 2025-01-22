from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'templates'  # Folder to store uploaded files
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Routes
@app.route('/')
def home():
    # Render the main upload page (index.html)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Placeholder for authentication logic
        if username == "admin" and password == "admin":  # Example logic
            return jsonify({'message': 'Login successful!'})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    # Render the login page
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST']) 
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Placeholder for user registration logic
        return jsonify({'message': f'User {username} registered successfully!'})
    # Render the signup page
    return render_template('signup.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Placeholder for analysis logic
    return jsonify({'message': f'File {filename} uploaded successfully for analysis!'})

if __name__ == '__main__':
    app.run(debug=True)
