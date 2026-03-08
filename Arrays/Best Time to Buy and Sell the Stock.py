def buyAndSellStock(nums):
  price = nums[0]
  curr_profit = 0
  max_profit = 0
  for i in range(1, len(nums)):
    if nums[i]<price:
      price = nums[i]
    else:
      curr_profit = nums[i]-price
      profit = max(curr_profit, max_profit)
  return profit
nums = list(int, input().split())
print(buyAndSellStock(nums))
