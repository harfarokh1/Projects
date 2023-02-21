import requests
import time
import numpy as np
from sklearn.linear_model import LogisticRegression

# Set the URL of the Bybit API endpoint
url = "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT"

userTimeInput = int(input("How long (in minutes) would you like the bot to perform for? "))

# Set up an empty list to hold the prices and labels
prices = []
labels = []

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

    # Check if the current price is within a trough or peak and append the corresponding label to the list
    if len(prices) >= 3:
        if prices[-2] < prices[-3] and prices[-2] < prices[-1]:
            labels.append(0)  # Trough
        elif prices[-2] > prices[-3] and prices[-2] > prices[-1]:
            labels.append(1)  # Peak
        else:
            labels.append(2)  # Not a peak or trough

    # Wait for a short time before sending the next request
    time.sleep(1)

# Convert the list of prices and labels to numpy arrays
pricesArray = np.array(prices[2:]).reshape(-1, 1)
labelsArray = np.array(labels)

# Convert continuous labels to categorical labels
labelsArray[labelsArray == 2] = 0  # Not a peak or trough
labelsArray[labelsArray == 1] = 1  # Peak
labelsArray[labelsArray == 0] = -1  # Trough

# Train a logistic regression model on the prices and labels data
model = LogisticRegression().fit(pricesArray, labelsArray)

# Use the trained model to predict the label of the next price value
nextPrice = prices[-1]
nextPriceArray = np.array(nextPrice).reshape(1, -1)
nextPriceLabel = model.predict(nextPriceArray)

# Output the predicted label to the console
if nextPriceLabel == -1:
    print("The next price is predicted to be within a trough")
elif nextPriceLabel == 0:
    print("The next price is not a peak or trough")
else:
    print("The next price is predicted to be within a peak")