import yfinance as yf
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

startTime = dt.datetime(2011, 1, 1)
endTime = dt.datetime(2021, 1, 1)

user = input("What stock do you want to analyze?")
stockData = yf.download(user, startTime, endTime)



returns = stockData['Adj Close'].pct_change()
dailyVol = returns.std()


T = 252
count = 0
priceList = []
lastPrice = stockData['Adj Close'][-1]

price = lastPrice * (1 + np.random.normal(0, dailyVol))
priceList.append(price)

for y in range(T):
    if count == 251:
        break
    price = priceList[count]* (1 + np.random.normal(0, dailyVol))
    priceList.append(price)
    count += 1

plt.plot(priceList)
plt.show()


simulCount =  1000
df = pd.DataFrame()
lastPriceList = []
for x in range(simulCount):
    count = 0
    price_list = []
    price = lastPrice * (1 + np.random.normal(0, dailyVol))
    price_list.append(price)
    
    for y in range(T):
        if count == 251:
            break
        price = price_list[count]* (1 + np.random.normal(0, dailyVol))
        price_list.append(price)
        count += 1
        
    df[x] = price_list
    lastPriceList.append(price_list[-1])
        
fig = plt.figure()
fig.suptitle("Monte Carlo Simulation:" + user)
plt.plot(df)
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

print("Expected price: ", round(np.mean(lastPriceList),2))
print("Quantile (5%): ",np.percentile(lastPriceList,5))
print("Quantile (95%): ",np.percentile(lastPriceList,95))