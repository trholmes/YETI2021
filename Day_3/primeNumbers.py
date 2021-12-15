# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:31:03 2021

@author: harin
"""

from primesieve import *
primenums = n_primes(500)
#first 500 prime numbers
#primesieve uses C to generate list of primes, it works faster than the sieve I tried to code
sumPrimes = lambda idx, seqLen: sum(primenums[idx:idx+seqLen])
#idx is the index of the number to start summing from, seqLen is the 
#number of consecutive primes
sumsOfThree = [sumPrimes(i, 3) for i in range(497)]
sumsOfThreeAndNine = [sumPrimes(i,9) for i in range(492) if sumPrimes(i,9) in sumsOfThree]
#lists sums of nine consecutive primes only if they are a sum of three consecutive primes
print(sumsOfThreeAndNine[4])

