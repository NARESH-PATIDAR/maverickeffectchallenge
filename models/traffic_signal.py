import time
import random

def simulate_traffic_data():
    """
    Simulates real-time traffic density data.
    
    Returns:
        int: Simulated traffic density between 0 and 100.
    """
    return random.randint(0, 100)  # Random traffic density

def adjust_signal(traffic_density):
    """
    Adjusts traffic signal timing based on traffic density.
    
    Args:
        traffic_density (int): Current traffic density (0-100).
    
    Returns:
        tuple: Adjustment recommendation and green light duration in seconds.
    """
    if traffic_density > 80:
        return 'Reduce Green Time', 30  # Reduce green time to 30 seconds
    elif traffic_density > 50:
        return 'Normal Green Time', 60  # Normal green time
    else:
        return 'Increase Green Time', 90  # Increase green time to 90 seconds

def main():
    """
    Continuously adjusts traffic signals based on simulated traffic data.
    """
    while True:
        traffic_density = simulate_traffic_data()
        adjustment, green_time = adjust_signal(traffic_density)
        print(f"Traffic Density: {traffic_density}")
        print(f"Signal Adjustment: {adjustment} - Green Time: {green_time} seconds")
        
        # Simulate waiting for the green light duration
        time.sleep(green_time)

if __name__ == '__main__':
    main()
