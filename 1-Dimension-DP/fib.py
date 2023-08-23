#Memoization AKA "Top down dynamic programming"
#This is the recursive solution

def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]

print("memoization approach: ", memoization(10, {}))


#Bottom up or "true dynamic programming" solution
#iterative solution

def dp(n):
    if n < 2:
        return n
    
    dp = [0, 1]
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1
    return dp[1]

print("Bottom up approach: ", dp(10))