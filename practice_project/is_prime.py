def is_prime(number: int) -> bool:
    if (number <= 1):
        return False
    elif (number <= 3):
        return True
    
    i = 2
    while (i * i <= number): 
        if (number % i == 0):
            return False
        i += 1
    return True

print (is_prime(1)) # False
print (is_prime(3)) # True
print (is_prime(7)) # true