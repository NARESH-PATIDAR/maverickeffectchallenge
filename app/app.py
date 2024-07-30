from flask import Flask, jsonify, request
import pandas as pd
from models.traffic_model import train_traffic_model
from models.toll_pricing import calculate_toll_price

app = Flask(__name__)

# Load and train the traffic model
traffic_model = train_traffic_model('../data/traffic_data.csv')

@app.route('/predict_traffic', methods=['GET'])
def predict_traffic():
    """
    Predicts traffic congestion based on input parameters.
    
    Query Parameters:
        hour (int): Hour of the day (0-23).
        day_of_week (int): Day of the week (0-6).
        weather (str): Weather condition (e.g., Clear, Rainy, Foggy).
    
    Returns:
        JSON: Predicted congestion level.
    """
    hour = int(request.args.get('hour'))
    day_of_week = int(request.args.get('day_of_week'))
    weather = request.args.get('weather')
    
    weather_mapping = {'Clear': 0, 'Rainy': 1, 'Foggy': 2}
    weather_encoded = weather_mapping.get(weather, 0)
    
    # Prepare input data for prediction
    data = pd.DataFrame([[hour, day_of_week, weather_encoded]], columns=['hour', 'day_of_week', 'weather'])
    data = pd.get_dummies(data, columns=['weather'])
    
    # Predict congestion level
    prediction = traffic_model.predict(data)[0]
    return jsonify({'congestion_level': prediction})

@app.route('/calculate_toll', methods=['GET'])
def calculate_toll():
    """
    Calculates the dynamic toll price based on congestion level.
    
    Query Parameters:
        base_price (float): Base toll price.
        congestion_level (float): Current congestion level.
    
    Returns:
        JSON: Calculated toll price.
    """
    base_price = float(request.args.get('base_price'))
    congestion_level = float(request.args.get('congestion_level'))
    price = calculate_toll_price(base_price, congestion_level)
    return jsonify({'dynamic_toll_price': price})

if __name__ == '__main__':
    app.run(debug=True)
