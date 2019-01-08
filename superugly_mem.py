import sys

count = 1
primes = []
file = open(sys.argv[1], 'r').read().split(",")
for numbers in file:
    primes.append(int(numbers))
size = len(primes)
ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def nth_super_ugly_number(n):
    global ugly, dp, index, ugly_nums, primes, count
    if count < n:
        for j in range(0, size):
            if ugly_nums[j] == ugly:
                ugly_nums[j] = dp[index[j]] * primes[j]
                index[j] += 1
        ugly = min(ugly_nums)
        dp.append(ugly)
        count = count + 1
        nth_super_ugly_number(n)
    return dp[-1]


def init(n):
    print("Super Ugly Numbers Memoization:", nth_super_ugly_number(n))
