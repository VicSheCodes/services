"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold than one share
of the stock.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

Algorithm Solution:
    This solution calculates the maximum profit from stock prices by summing all positive price differences
    between consecutive days.
    For each day, if the next day's price is higher, the difference is added to the total profit.
    This greedy approach ensures all profit opportunities are captured efficiently.

    Steps:
    1. Initialize profit to 0.
    2. Loop through the prices from day 0 to day n-2.
    3. For each day, if the next day's price is higher than the current day's, add the difference to profit.
    4. Return the total profit after the loop.

    Time Complexity: O(n), where n is the number of days.
    Space Complexity: O(1).

"""
prices1 = [1,2,3,4,5]

def test_calculate_profit(prices):
    if not prices:
        return 0

    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]

    return profit

def test_test_calculate_profit():
    print(f"\n{test_calculate_profit(prices1)}")
