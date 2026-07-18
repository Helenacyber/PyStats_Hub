def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer."
    if n < 1:
        return "Argument must be greater than 1."
    
    sequence =''
    for num in range(1,n+1):
        if num == n:
            sequence += str(num) 
        else:
            sequence += str(num) + " "
    return sequence

print(number_pattern(6)) 
print(number_pattern(4)) 
print(number_pattern(5)) 
print(number_pattern(-2))
print(number_pattern("o"))  