class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=new=diff=0
        for sell in range(1,len(prices)):
          if prices[buy]>prices[sell]:
              buy=sell
          elif prices[buy]<prices[sell]:
              diff=prices[sell]-prices[buy]
              new=max(new,diff)
        return new
        