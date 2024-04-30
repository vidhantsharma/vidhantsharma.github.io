from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return 'No image uploaded'

    image_file = request.files['image']

    # Your image processing code here
    # Example: You can use a library like OpenCV or PIL to process the image
    
    # For demonstration, let's just return the file name
    return f'Uploaded image: {image_file.filename}'

if __name__ == '__main__':
    app.run(debug=True)