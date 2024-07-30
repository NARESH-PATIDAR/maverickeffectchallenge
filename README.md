# Smart Traffic Management System

This project demonstrates a basic AI-driven traffic management system using Python. It includes predictive analytics, dynamic toll pricing, a traffic signal adjustment system, and a Flask-based API for integration.

## Project Structure

- data: Contains sample datasets for traffic and weather data.
- models: Contains Python scripts for training traffic prediction models, calculating dynamic toll pricing, and adjusting traffic signals.
- app: Contains the Flask application for providing API endpoints.
- README.md: This file.
 
## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart_traffic_management.git
   cd smart_traffic_management

2. Install the required packages:
   pip install -r app/requirements.txt

3. Train the traffic model:
   python models/traffic_model.py

4. Run the traffic signal adjustment system:
   python models/traffic_signal.py

5. Run the Flask application:
   python app/app.py

6. Use the API endpoints:
  Predict Traffic Congestion:
  GET /predict_traffic?hour=<hour>&day_of_week=<day_of_week>&weather=<weather>

  Calculate Dynamic Toll Price
  GET /calculate_toll?base_price=<base_price>&congestion_level=<congestion_level>
