class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)): # 기존 nums 배열 사용, in-place 처리 공간 O(1)
            nums[i] += nums[i - 1]
        return nums


    # 기존 작성 코드. 문제는 1. 새 배열 만든것 2. 루프 문이 i+1 시작이라 불필요한 계산 시간 추가 
    # def runningSum(self, nums: List[int]) -> List[int]:
    #     # nums[0] nums[0]+nums[1] nums[0]+..+nums[2] 
    #     # ans[0] ans[1] ans[2]
    #     result = [0]*len(nums) # 새 배열 만들기 공간 O(n)
    #     result[0] = nums[0]
    #     for i in range(len(nums)-1):
    #         result[i+1] = result[i] + nums[i+1] # 이렇게 하면 인덱스 계산 시간이 미세하게 추가됨
    #         #print(result[i+1])
    #     return result
