def prime_sieve(maxnum = 1000000):
    # loosely based on sieve of aratosthenese
    # build the initial list
    t_list = [i for i in range(2, maxnum)]
    # define the first 2 primes to start the sieve
    retlist = [2, 3]
    for i in t_list:
        prime = True
        for j in retlist:
            if i % j == 0:
                prime = False
                break
        if prime:
            retlist.append(i)
    return retlist

def sumidx(vals, idxlow, idxhigh) -> int:
    return sum(vals[idxlow:idxhigh])
def sumnext3(vals, idx):
    return sumidx(vals, idx, idx + 3)
def sumnext9(vals, idx):
    return sumidx(vals, idx, idx + 9)

pmax = 10000
print(f"Computing primes up to: {pmax}")
# initial set of primes to test
plist = prime_sieve(pmax)
print("Making sums of 3 and 9 sequential primes")
# prebuild sums
sum3s = [sumnext3(plist, i) for i in range(len(plist) - 2)]
sum9s = [sumnext9(plist, i) for i in range(len(plist) - 8)]
print("Comparing lists of primes to find shared values")
shared = []
for i in sum3s:
    if i in sum9s:
        shared.append(i)

print(f"The 5th smallest prime that is the sum of both 3 and 9 sequential primes is:\n{shared[4]}")
