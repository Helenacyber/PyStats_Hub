#This program helps to calculate the sum of squares of a number starting from 1 upto the number itself.
def sum_of_squares(n):
    num_ranges = range(1,n+1)
    result = 0
    for num in num_ranges:
        value = num **2
        result += value
    return result




