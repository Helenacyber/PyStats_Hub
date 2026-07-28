#This program defines a function that takes a number and check it wherether the number is a pronic or not \n A pronic A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6.
def is_pronic (num):
    num_range= range(0,num+1)
    for a ,b in enumerate(num_range,1):
        if abs(a-b) == 1:
           if a*b == num:
              return True
    return False
print (is_pronic(0))
print (is_pronic(6))
print (is_pronic(15))
print (is_pronic(132))
print (is_pronic(80))


