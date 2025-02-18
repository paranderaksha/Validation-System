from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    data = pd.read_json(file)
    results = process_data(data)
    return render_template('results.html', results=results)

def process_data(data):
    # Detect anomalies using Isolation Forest
    model = IsolationForest(contamination=0.1)
    data['anomaly'] = model.fit_predict(data.select_dtypes(include=[float, int]))
    anomalies = data[data['anomaly'] == -1]
    missing_values = data.isnull().sum()
    return {'anomalies': anomalies.to_dict(orient='records'), 'missing_values': missing_values.to_dict()}

if __name__ == '__main__':
    app.run(debug=True)