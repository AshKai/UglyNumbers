next_multiple_of_2, next_multiple_of_3, next_multiple_of_5, i2, i3, i5 = 2, 3, 5, 0, 0, 0
ugly = [0]
ugly[0] = 1
count = 1


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def calculate_list(number):
    global next_multiple_of_2, next_multiple_of_3, next_multiple_of_5, i2, i3, i5, count
    if count < number:
        ugly.append(min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5))
        if ugly[-1] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[-1] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[-1] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
        count = count + 1
        calculate_list(number)


def init(n):
    calculate_list(n)
    print("Ugly Numbers Memoization:", ugly[-1])
