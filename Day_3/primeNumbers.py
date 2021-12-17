# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:31:03 2021

@author: harin
"""

from primesieve import *
primenums = n_primes(500)
#primesieve uses C to generate list of primes, it works faster than the sieve I tried to code
def sumPrimes(ind,seqLen): return sum(primenums[ind:ind+seqLen])
#index is the element to start summing from, primes is the list of primes, seqLen is the 
#number of consecutive primes
sumsOfThree = [sumPrimes(i, 3) for i in range(497)]
sumsOfThreeAndNine = [sumPrimes(i,9) for i in range(492) if sumPrimes(i,9) in sumsOfThree]
#lists sums of nine consecutive primes only if they are a sum of three consecutive primes
print(sumsOfThreeAndNine[4])

