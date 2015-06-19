def count_evens(nums):
  """
  Return the number of even ints in the given array. Note: the % "mod" operator
  computes the remainder, e.g. 5 % 2 is 1. 
  """
  count = 0
  for n in nums:
    count -= n%2-1
  return count

def big_diff(nums):
  """
  Given an array length 1 or more of ints, return the difference between the 
  largest and smallest values in the array. Note: the built-in min(v1, v2) and 
  max(v1, v2) functions return the smaller or larger of two values. 
  """
  return max(nums) - min(nums)

def centered_average(nums):
  """
  Return the "centered" average of an array of ints, which we'll say is the 
  mean average of the values, except not counting the largest and smallest 
  values in the array. Use int division to produce the final average. You may
  assume that the array is length 3 or more. 
  """
  nums.sort()
  return sum(nums[1:-1]) / (len(nums) - 2)

def sum13(nums):
  """
  Return the sum of the numbers in the array, returning 0 for an empty array. 
  Except the number 13 is very unlucky, so it does not count and numbers that 
  come immediately after a 13 also do not count. 
  """
  while 13 in nums:
    if nums.index(13) < len(nums)-1:
      nums.pop(nums.index(13)+1)
    nums.pop(nums.index(13))
    
  return sum(nums)

def sum67(nums):
  """
  Return the sum of the numbers in the array, except ignore sections of numbers
  starting with a 6 and extending to the next 7 (every 6 will be followed by at
  least one 7). Return 0 for no numbers. 
  """
  count = 0
  blocked = False
  
  for n in nums:
    if n == 6:
      blocked = True
      continue
    if n == 7 and blocked:
      blocked = False
      continue
    if not blocked:  
      count += n
  
  return count

def has22(nums):
  """
  Given an array of ints, return True if the array contains 
  a 2 next to a 2 somewhere. 
  """
  for i,v in enumerate(nums[:-1]):
    if v == 2 and nums[i+1] == 2:
      return True
  return False
