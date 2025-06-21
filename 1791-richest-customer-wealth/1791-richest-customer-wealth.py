class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


        # map 사용해서 메모리 아끼는 게 관건.
        # map(function, iterable)
        
        # wealth = [0]*len(accounts)
        # for i in range(len(accounts)):
        #     wealth[i] = sum(accounts[i])
        # #print(wealth)
        # return max(wealth)