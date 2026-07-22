import math
def piggy_bank(coins):
    coin_values={
        'pennies' : 0.01,
        'nickels' : 0.05,
        'dimes' : 0.10,
        'quarters' : 0.25 
    }
    result = 0
    for key,value in coins.items():
        key_name =key
        value=(coins[key])
        amount= (coin_values.get(key_name))
        result += (amount*value)