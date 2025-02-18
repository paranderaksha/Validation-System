# Validation-System
This web application provides an AI-based solution for real-time validation of data quality by detecting anomalies and identifying missing values in uploaded datasets. The system uses an Isolation Forest model to detect outliers in numerical data and highlights missing values for further data cleaning.

## Features:
- **File Upload**: Allows users to upload a JSON file containing the dataset.
- **Anomaly Detection**: Identifies outliers in the dataset using the Isolation Forest algorithm.
- **Missing Value Detection**: Detects missing values in the dataset and displays a summary.

## Files:
1. **app.py**: The main Flask application that handles file uploads, processes the data, and renders results.
2. **index.html**: The front-end form for uploading a JSON file.
3. **results.html**: Displays the results, including anomalies and missing values detected in the uploaded data.

## How to Use:
1. Start the Flask application by running `app.py`.
2. Navigate to the home page (`/`), where you can upload a JSON file.
3. After uploading, the application will process the file and display the validation results, showing anomalies and missing values.

## Requirements:
- Flask
- pandas
- scikit-learn

## Running the Application:
```bash
pip install flask pandas scikit-learn
python app.py
