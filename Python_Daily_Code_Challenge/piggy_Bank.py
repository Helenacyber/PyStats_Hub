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

    return f"${result:.2f}"

print(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}))

print(piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}))

print(piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}))

print(piggy_bank({}))

print(piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}))