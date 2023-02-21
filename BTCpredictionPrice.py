import requests
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# Set the URL of the Bybit API endpoint
url = "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT"

# Set up an empty list to hold the prices
prices = []

userTimeInput = int(input("How long (in minutes) would you like the bot to perform for? "))

# Get the current time and end time
startTime = time.time()
endTime = startTime + userTimeInput * 60

# Loop until the end time is reached, sending a GET request and adding the last price to the list after every request
while time.time() < endTime:
    # Send the GET request and read the response JSON
    response = requests.get(url)
    jsonResponse = response.json()

    # Extract the last price of BTCUSDT futures from the response and add it to the list
    lastPrice = float(jsonResponse["result"][0]["last_price"])
    prices.append(lastPrice)

    # Wait for a short time before sending the next request
    time.sleep(0.5)

# Convert the list of prices to a numpy array
pricesArray = np.array(prices).reshape(-1, 1)

# Fit a linear regression model to the prices
regressionModel = LinearRegression()
regressionModel.fit(pricesArray[:-1], pricesArray[1:])

# Predict the next price using the linear regression model
nextPrice = regressionModel.predict(pricesArray[-1:])[0][0]

# Output the next predicted price
print("Next predicted price:", nextPrice)