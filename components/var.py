import numpy as np
import requests
from datetime import datetime, timedelta

def get_historical_prices(symbol):
    
    # CoinGecko API endpoint for historical prices
    api_url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart'
    
    # Set up the request parameters
    params = {
        'vs_currency': 'usd',
        'days': '300'
    }
    
    # Make the API request
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        prices = data.get('prices', [])
        historical_data = [{'timestamp': timestamp, 'price': price} for timestamp, price in prices]
        return historical_data
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage:
historical_eth = get_historical_prices("eth")
historical_bnb = get_historical_prices("bnb")

if historical_eth is not None:
    for data_point in historical_prices:
        timestamp = datetime.utcfromtimestamp(data_point['timestamp'] / 1000).strftime('%Y-%m-%d')
        price = data_point['price']
        print(f"{timestamp}: {price} USD")
else:
    print("Failed to retrieve historical ETH/USD prices.")



def calculate_var(value, k, y, alpha):
    # Calculate daily yield from the second day to the 300th day.
    value0 = value[:-1]
    value1 = value[1:]
    rate0 = (value1 - value0) / value0
    
    # Calculate the mean and variance of daily yield.
    u = np.mean(rate0)
    vol = np.std(rate0)
    
    # 1000 times Monte Carlo simulations and 30 days each simulation.
    s0 = value[-1]
    np.random.seed(0)  # Setting seed for reproducibility
    k_simulations = 1000
    y_days = 30
    value2 = np.zeros(k_simulations)
    
    for i in range(k_simulations):
        s = s0
        for j in range(y - 1):
            # Build the variable wt of Random Walk based on the mean and variance.
            s = s + s * (u + vol * np.random.randn(1, 1))
        value2[i] = s
    
    # Calculate the daily yield of simulations.
    rate = (value2 - s0) / (s0 * y)
    rate1 = np.sort(rate)
    
    # Calculate the VaR with confidence 0.05.
    var = rate1[int(k * alpha)]
    return var

# Example usage:
# Replace 'your_eth_usd_data' with the actual array of ETH/USD price data.
# your_eth_usd_data = np.random.rand(300) * 1000  # Replace this with actual data
value_at_risk_eth = calculate_var(historical_eth, k=1000, y=30, alpha=0.05)
print("Value at Risk (VaR) for eth:", value_at_risk_eth)
value_at_risk_bnb = calculate_var(historical_bnb, k=1000, y=30, alpha=0.05)
print("Value at Risk (VaR) for bnb:", value_at_risk_bnb)
