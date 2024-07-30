def calculate_toll_price(base_price, congestion_level):
    """
    Calculates dynamic toll price based on traffic congestion level.
    
    Args:
        base_price (float): Base toll price.
        congestion_level (int): Current traffic congestion level (0-10).
    
    Returns:
        float: Calculated dynamic toll price.
    """
    if congestion_level > 7:
        return base_price * 1.5
    elif congestion_level > 5:
        return base_price * 1.2
    else:
        return base_price

if __name__ == '__main__':
    base_price = 5
    congestion_level = 8
    price = calculate_toll_price(base_price, congestion_level)
    print(f"Dynamic Toll Price: ${price}")
