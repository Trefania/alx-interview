#!/usr/bin/python3
""""
Main file for testing
"""

def makeChange(coins, total):
    """ If the total is 0 or less, return 0 """
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    # The minimum number of coins needed to make 0 is 0
    min_coins[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Iterate over each amount from the coin value to the total
        for amount in range(coin, total + 1):
            # Update the minimum number of coins needed for the current amount
            # by taking the minimum of the current minimum and the minimum for the
            # remaining amount after subtracting the current coin value plus 1
            min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    # If the minimum number of coins for the total is still infinity, it means
    # the total cannot be met by any combination of coins
    if min_coins[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed for the total
    return min_coins[total]
