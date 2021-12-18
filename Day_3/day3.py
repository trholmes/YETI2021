import math

def getPrimes(limit=300):
    # returns a list of primes lower than limit
    primes = []
    
    for number in range(limit):
        if number > 1:
            for i in range(2, int(math.sqrt(number)+1)):
                if number%i == 0:
                    break
            else:
                primes.append(number)
                
    return primes


found = 0
primes = getPrimes()

# maximum lenghts of i and j variables
i_max = len(primes) - 9
j_max = len(primes) - 3

for i in range(i_max + 1):

    # until the 5th result is found
    if found < 5:
        sum9 = sum(primes[i:i+9])   # sum of 9 consecutive primes
            
        for j in range(j_max + 1):
            sum3 = sum(primes[j:j+3])   # sum of 3 consecutive primes
                
            if sum3 == sum9:
                found = found + 1
                break
                
            if sum3 > sum9:
                break   # move on to the next sum of 9 primes
    else:
        print(f"{found}th result = {sum9}")
        break