import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_traffic_model(data_path):
    """
    Trains a Random Forest model to predict traffic congestion based on historical data.
    
    Args:
        data_path (str): Path to the CSV file containing traffic data.

    Returns:
        model (RandomForestRegressor): Trained Random Forest model.
    """
    # Load the data
    data = pd.read_csv(data_path)
    
    # Feature selection
    X = data[['hour', 'day_of_week', 'weather']]
    y = data['congestion_level']
    
    # One-hot encode the 'weather' column
    X = pd.get_dummies(X, columns=['weather'])
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Predict and evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    return model

if __name__ == '__main__':
    train_traffic_model('../data/traffic_data.csv')
