# This file of main.py is fo rcrearing the webapp to upload the file . This python file has been created using flask
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__)

# Replace this with your GCS bucket name
GCS_BUCKET_NAME = "dkprj"

# # Configure Google Cloud Storage credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-key.json"
# storage_client = storage.Client()


def upload_to_gcs(file):
    """Uploads a file to the specified GCS bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)
    return blob.public_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part in the request", 400
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    try:
        public_url = upload_to_gcs(file)
        return f"File uploaded successfully: <a href='{public_url}'>{public_url}</a>"
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
