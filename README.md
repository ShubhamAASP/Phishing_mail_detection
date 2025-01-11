# Phishing Email Detection System

This project implements a **Phishing Email Detection System** using **Machine Learning** to classify emails as phishing or legitimate. The system leverages email features like sender, subject, body, and URLs for accurate predictions.

## Features
- **Real-time predictions**: Classifies emails as phishing or legitimate.
- **User-friendly interface**: Simple, responsive UI built with **HTML**, **CSS**, and **JavaScript**.
- **Machine Learning model**: Uses **scikit-learn** for classification and **Natural Language Processing (NLP)** for feature extraction.
- **Flask backend**: API built using **Flask** for easy integration with the frontend.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, NLP

## Installation
1. Clone this repository.
   ```bash
   git clone https://github.com/ShubhamAASP/Phishing_mail_detection.git
2. Install Dependencies
   Navigate to the project directory and install the required dependencies:

   '''bash
   cd Phishing_mail_detection
   pip install -r requirements.txt
   Ensure you have Python 3.x and pip installed on your machine. The requirements.txt file includes all necessary libraries like Flask, scikit-learn, pandas, numpy, and joblib.

3. Run the Flask Application
   Once the dependencies are installed, start the Flask app by running:

   '''bash
   python app.py
   The Flask app will run on http://127.0.0.1:5000/.

4. Open the Web Application
   To use the phishing email detection system, open a web browser and visit http://127.0.0.1:5000/.

   Usage
   Enter the Email Details: Provide the email sender, subject, body, and optional URLs in the input fields.
   Submit the Form: After submitting, the system will return a prediction of whether the email is phishing or legitimate.
   The prediction result will display:

   "This email is phishing!"
   "This email is not phishing."
