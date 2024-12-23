import base64
import numpy as np

from io import BytesIO
from PIL import UnidentifiedImageError

from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Labels for classification
labels = {
    0: 'cloudy', 
    1: 'fogsmog', 
    2: 'lightning', 
    3: 'rain', 
    4: 'sandstorm', 
    5: 'snow', 
    6: 'sunny'
}

# Flask application
app = Flask(__name__)
allowed_extensions = ['.jpg', '.jpeg', '.png']
model = load_model('WeatherSense_Model.h5')

def preprocess_image(image):
    """Preprocess the image for model prediction."""
    image = img_to_array(image) / 255.0
    return np.expand_dims(image, axis=0)

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint for predicting the weather condition."""
    try:
        file = request.files['image']
        
        # Check file extension
        if not any(file.filename.lower().endswith(ext) for ext in allowed_extensions):
            return jsonify({
                "error": f"Only {', '.join(allowed_extensions)} files are allowed."
            }), 400
        
        # Read the image
        image_stream = BytesIO(file.read())
        try:
            # Load and preprocess the image
            image = load_img(image_stream, target_size=(224, 224))
            processed_image = preprocess_image(image)
            
            # Make prediction
            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction)
            
            # Convert uploaded image to base64
            image_stream.seek(0)
            img_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')
            
            return jsonify({
                "prediction": labels[predicted_class].capitalize(),
                "uploaded_image": img_base64
            }), 200
        except UnidentifiedImageError as e:
            return jsonify({
                "error": f"Unable to identify the image file. {e}"
            }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
