from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from React frontend

# Load example data (assume you have a CSV file for demonstration)
data = pd.read_csv('data/featured_oil_price_data.csv') 
@app.route('/api/price-trends', methods=['GET'])
def get_price_trends():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Example data filtering
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)].copy()
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/api/model-metrics', methods=['GET'])
def get_model_metrics():
    # Dummy metrics (replace with your actual calculation logic)
    metrics = {
        "RMSE": 0.02,
        "MAE": 0.015,
        "Volatility": 0.03
    }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
