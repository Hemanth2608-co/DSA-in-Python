class Solution:
    def maxSubArray(self, nums):
        current_sum = best_sum = nums[0]

        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  
