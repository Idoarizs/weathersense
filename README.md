# 🌦️ WeatherSense API

WeatherSense AI API utilizes a pre-trained machine learning model to classify weather conditions from uploaded images. With just an image, it predicts whether the weather is **cloudy**, **foggy**, **lightning**, **rainy**, **sandstorm**, **snowy**, or **sunny**. Perfect for integrating AI-powered weather predictions into your apps! 🌤️

---

## 🚀 Features

- 🖼️ **Image-Based Weather Classification**: Upload an image, and receive an accurate weather prediction.
- 🤖 **AI-Powered Predictions**: Uses a TensorFlow-trained deep learning model to predict weather conditions.
- 🌐 **Supported Image Formats**: Supports `.jpg`, `.jpeg`, `.png` image files.
- 📷 **Base64 Image Response**: The uploaded image is returned as Base64, making it easy to integrate into your application.

---

## 📡 API Endpoints

### `POST /predict`

- **Description**: Upload an image and get the weather prediction.
- **Request**:
  - **Type**: `multipart/form-data`
  - **Field**: `image` (image file to be analyzed)

- **Response**:
  - **Success**: Returns a JSON object with:
    - `"prediction"`: The predicted weather condition (e.g., `"Sunny"`).
    - `"uploaded_image"`: Base64-encoded image data.
  - **Error**: Returns an error message if the file type is unsupported or if the image is invalid.

---

## 💻 Example Request

**URL**: `POST http://<url>/predict`

**Body** (using `multipart/form-data`):
```json
{
  "image": "<image>.jpg"
}
