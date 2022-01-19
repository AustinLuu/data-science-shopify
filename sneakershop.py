import pandas as pd
import numpy as np
import csv
import collections
from collections import defaultdict

# Import CSV for month of march
data= pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
# Determine the total month spending, number of orders, and the average order value
sum = np.sum(data.order_amount)
orders = np.shape(data.order_amount)[0]
average = np.around(sum/orders, decimals = 2)
print("Average Order Value w/Anomalies: $",average)

# Obiously AOV of 3145 isnt reasonable. This is likely cause by anomly purchases by bots/scalpers
# A better way to represent the data would be to:

# A) Present the data as AOV without anomalies. i.e, puchases exceeding a threshold of items
# We notice user_id == 607 is purchasing from the same seller in bulk amounts.
# I have set a threshold of 20 items for this example as likely stores would limit their customers purchases per transaction
# Note: The dataset used for solutions B, C, and D use the filtered dataset.
data = data[data['total_items'] < 20]
sumA = np.sum(data.order_amount)
ordersA = np.shape(data.order_amount)[0]
averageA = np.around(sumA/ordersA, decimals = 2)
print("Average Order Value w/Out Anomalies: $",averageA)

# B) Present the data as an Average Monthly Revenue per Shop. Displayed as a key value pair shop_id:monthly_revenue
# Representing it by shop would be beneficial in identifying shop based anomalies 
sumB = defaultdict(int)
for i, k in zip(data['shop_id'], data['order_amount']):
    sumB[i] += k 
sumB = collections.OrderedDict(sorted(sumB.items()))
print(sumB)

# C) Present the data as an Average Monthly Revenue by user. Displayed as a key value pair user_id:monthly_revenue
# Representing it by user would be beneficial in identifying user based anomalies 
sumC = defaultdict(int)
for i, k in zip(data['user_id'], data['order_amount']):
    sumC[i] += k 
sumC = collections.OrderedDict(sorted(sumC.items()))
print(sumC)

# D) Present the data as a Distribution by Payment Method
sumD = defaultdict(int)
for i, k in zip(data['payment_method'], data['order_amount']):
    sumD[i] += k 
sumD = collections.OrderedDict(sorted(sumD.items()))
print(sumD)

#To expand on the question in regards to anomly detction
# A), we could also take into consideration the time of purchases and reject purchases made sequentially over a short period of time.
# Furthermore if returns are accepted by our sneaker shops. We should reflect these transactions as rows with negative order_amount and total_items in our dataset