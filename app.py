from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('phishing_email_detector.pkl')

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Extract the data from the POST request
    data = request.get_json()

    # Ensure data contains the correct features
    try:
        sender = data['sender']
        subject = data['subject']
        body = data['body']
        urls = data['urls', '']

        # Here you need to implement feature extraction for sender, subject, body, and urls
        # You can follow the same steps for feature extraction that you did when training the model
        suspicious_sender = 1 if 'suspicious' in sender else 0  # Example: Check for suspicious keyword in sender
        subject_length = len(subject)
        body_length = len(body)
        subject_phishing_keywords = sum(keyword in subject for keyword in ["free", "urgent", "winner"])  # Example keywords
        body_phishing_keywords = sum(keyword in body for keyword in ["free", "urgent", "winner"])  # Example keywords
        url_length = len(urls) if urls else 0  # Example: Count the number of URLs
        suspicious_keywords = sum(keyword in urls for keyword in ["http", "www", "phishing"])  # Example URL check

    except KeyError:
        return jsonify({'error': 'Invalid input data'}), 400

    # Create feature vector (same order as the model was trained)
    features = np.array([suspicious_sender, subject_length, body_length,
                         subject_phishing_keywords, body_phishing_keywords,
                         url_length, suspicious_keywords]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Return prediction result
    return jsonify({'prediction': int(prediction[0])})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
