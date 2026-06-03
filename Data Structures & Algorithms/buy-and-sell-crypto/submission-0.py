class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0
        minimum=prices[0]
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum=prices[i]
            print(minimum,prices[i])
            maxprofit=max(maxprofit,prices[i]-minimum)

        return maxprofit


        