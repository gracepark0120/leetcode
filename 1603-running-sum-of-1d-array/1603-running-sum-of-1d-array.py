class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = (sum(nums[:i+1]))
        return output


# 위 방법은 O(n^2), 매번 합을 다시 계산함. 이것보다 누적합을 계산하는 게 더 효율적임. O(n)
