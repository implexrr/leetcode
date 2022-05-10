class Solution:

    """
    Solution via DP/memoization.

    This is pretty much just the fibonacci sequence. We take the
    last value of the fibo(n) sequence, and that is our desired value.

    Time complexity: O(n)
    Space complexity:O(n)

    """

    def climbStairs(self, n: int) -> int:
        distinct_ways = [1] * (n + 1)
        for i in range(2, n + 1):
            distinct_ways[i] = distinct_ways[i - 1] + distinct_ways[i - 2]
        return(distinct_ways[-1])
