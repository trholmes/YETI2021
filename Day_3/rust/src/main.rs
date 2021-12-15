fn prime_sieve(maxnum: u64) -> Vec<u64>
{
    let mut ret: Vec<u64> = Vec::<u64>::from([2, 3, 5]);
    for i in 6..maxnum
    {
        let mut prime = true;
        for j in 0..ret.len()
        {
            if i % ret[j] == 0
            {
                prime = false;
                break
            } 
        }
        if prime
        {
            ret.push(i)
        }
    }
    ret
}

fn sum_idx(vals: &Vec<u64>, idxlow: usize, idxhigh: usize) -> u64
{
    let mut ret = 0u64;
    for i in idxlow..idxhigh
    {
        ret += vals[i]
    }
    ret
}

fn intersect(v1: &Vec<u64>, v2: &Vec<u64>) -> Vec<u64>
{
    let mut ret: Vec<u64> = Vec::<u64>::new();
    for i in v1
    {
        if v2.contains(i)
        {
            ret.push(*i)
        }
    }
    ret
}

fn sum_xs(v1: &Vec<u64>, width: usize) -> Vec<u64>
{
    let mut ret: Vec<u64> = Vec::<u64>::new();
    let maxidx = v1.len() - width + 1 as usize;
    for i in 0..maxidx
    {
        ret.push(sum_idx(v1, i, i + width))
    }
    ret
}

fn main() {
    let plist = prime_sieve(100000);
    let sum3s = sum_xs(&plist, 3);
    let sum9s = sum_xs(&plist, 9);
    let shared = intersect(&sum3s, &sum9s);
    println!("The 5th smallest sum of both 3 and 9 consecutive primes is {}", shared[4]);
}
