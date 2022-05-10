class Solution:
    """
    Solution via memoization.

    For any array index, the product of an array except itself will
    equal to the product of all the elements in the left of the array
    times the product of all the elements in the right
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_prod = [1] * (n)
        left_prod = [1] * (n)
        answer = [1] * n

        # For any given array element, calculate it's product from the left and it's product from the right via the previous products
        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
            right_prod[n - 1 - i] = right_prod[n - i] * nums[n - i]

        # Each element in the answer array is the product of the left product and right product.
        for i in range(n):
            answer[i] = right_prod[i] * left_prod[i]

        return answer
