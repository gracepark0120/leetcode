class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)
        # wealth = [0]*len(accounts)
        # for i in range(len(accounts)):
        #     wealth[i] = sum(accounts[i])
        # #print(wealth)
        # return max(wealth)