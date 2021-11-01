'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4'''

def sum67(nums):
  case = True
  total = 0
  
  for n in nums:
    if n == 6:
      case = False
  
    if case:
      total += n
      continue
    
    if n == 7:
      case = True
  
  return total  