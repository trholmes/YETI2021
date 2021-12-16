class MyNumber:
    def __init__(self):
        self.primes_cache = [] #Is sorted and contains first prime numbers

    def is_prime(self, x):
        for p in self.primes_cache:
            if x % p == 0:
                return False
        return True

    def precalculate_next_n_primes(self, n):
        original_length = len(self.primes_cache)
        if not n: 
            return
        if not self.primes_cache:
            self.primes_cache = [2]
            if n == 1:
                return
        test_number = self.primes_cache[-1] + 1
        while True:
            if self.is_prime(test_number):
                self.primes_cache.append(test_number)
            if(len(self.primes_cache) - original_length) >= n:
                return 
            test_number += 1

    def get_number(self):
        n, nine_primes_ptr = 0, 0

        #The three primes cannot be less than or all be among the nine primes for the equality to hold
        #Atleast one of the three primes has to be greater than the nine_primes. So we start by making our 
        #pointer for three primes point at the second last of the nine primes
        three_primes_ptr  = nine_primes_ptr + 9 - 2 
        self.precalculate_next_n_primes(10)
        while n < 5: 
            while True:
                if nine_primes_ptr + 9 > len(self.primes_cache) or three_primes_ptr+3 > len(self.primes_cache):
                    self.precalculate_next_n_primes(10)

                sum_nine = sum(self.primes_cache[nine_primes_ptr: nine_primes_ptr+9]) 
                sum_three = sum(self.primes_cache[three_primes_ptr: three_primes_ptr+3]) 

                if sum_nine > sum_three:
                    three_primes_ptr += 1
                elif sum_three > sum_nine:
                    nine_primes_ptr += 1
                elif sum_nine == sum_three:
                    n += 1
                    nine_primes_ptr += 1
                    if n == 5 :
                        return sum_nine


def main():
    my_number = MyNumber()
    print(my_number.get_number())

if __name__ == '__main__':
    main()
