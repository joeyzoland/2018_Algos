#Note: This algorithm was taken from an online source besides HackerRank.  You are given an array of stock prices from yesterday, and you have to determine where you could have gotten the biggest profit (viz., buying at the minimum price and selling at the maximum price).  Note: In this code, we're assuming that the array of stock_prices_yesterday has at least two values.

def get_max_profit(stock_prices_yesterday):
    #You initialize the current minimum price at the smallest price in the first two indices.  You set the maxProfit that can be gained as the difference between these two values.
    if (stock_prices_yesterday[0] < stock_prices_yesterday[1]):
        currentMinPosition = 0
        currentMinValue = stock_prices_yesterday[0]
    else:
        currentMinPosition = 1
        currentMinValue = stock_prices_yesterday[1]
    maxProfit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    #At each iteration, you check whether the minimum price subtracted from the current price would result in a greater gain and, if so, you save it in maxProfit.  You also check whether the current price is smaller than the minimum price and, if it is, you update it here for future iterations.
    if (len(stock_prices_yesterday) >= 3):
        for i in range(2, len(stock_prices_yesterday)):
            if (stock_prices_yesterday[i] - currentMinValue > maxProfit):
                maxProfit = stock_prices_yesterday[i] - currentMinValue
            if (stock_prices_yesterday[i] < currentMinValue):
                currentMinPosition = i
                currentMinValue = stock_prices_yesterday[i]
    return maxProfit



sample_stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(sample_stock_prices_yesterday)
