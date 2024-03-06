import requests
import matplotlib.pyplot as plt
import datetime

def get_funding_rates(market, start_date, end_date):
    params = {
        'market': market,
        'start_date': start_date,
        'end_date': end_date
    }

    try:
        response = requests.get("https://indexer-mainnet.levana.finance/funding-rates", params=params)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Example usage
market = "osmo1hd7r733w49wrqnxx3daz4gy7kvdhgwsjwn28wj7msjfk4tde89aqjqhu8x"
start_date = "2023-08-01"
end_date = "2023-08-31"

response_data = get_funding_rates(market, start_date, end_date)
timestamps = [datetime.datetime.fromisoformat(q['timestamp']) for q in response_data]
long_funding_rate = [100 * float(q['long_rate']) for q in response_data]
short_funding_rate = [100 * float(q['short_rate']) for q in response_data]

plt.plot(timestamps, long_funding_rate, label="Long Funding Rate")
plt.plot(timestamps, short_funding_rate, label="Short Funding Rate")
plt.legend()
plt.title("Funding Rates")
plt.show()