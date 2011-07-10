def string_times(str, n):
  """
  Given a string and a non-negative int n, return a larger string that is 
  n copies of the original string. 
  """
  return str*n

def front_times(str, n):
  """
  Given a string and a non-negative int n, we'll say that the front of the 
  string is the first 3 chars, or whatever is there if the string is less than 
  length 3. Return n copies of the front.
  """ 
  return str[:(3 if len(str)>3 else len(str))]*n

def string_bits(str):
  """
  Given a string, return a new string made of every other char starting with 
  the first, so "Hello" yields "Hlo". 
  """
  return str[::2]

def string_splosion(str):
  """
  Given a non-empty string like "Code" return a string like "CCoCodCode".
  """
  result = ""
  for i in range(1,len(str)+1):
    result = result + str[:i]
  return result

def last2(str):
  """
  Given a string, return the count of the number of times that a substring 
  length 2 appears in the string and also as the last 2 chars of the string,
  so "hixxxhi" yields 1 (we won't count the end substring).
  """
  count = 0
  for i in range(0, len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count

def array_count9(nums):
  """Given an array of ints, return the number of 9's in the array."""
  return nums.count(9)

def array_front9(nums):
  """
  Given an array of ints, return True if one of the first 4 elements in the 
  array is a 9. The array length may be less than 4. 
  """
  return nums[:4].count(9) > 0

def array123(nums):
  """Given an array of ints, return True if .. 1, 2, 3, .. 
  appears in the array somewhere. 
  """
  for i in range(0,len(nums)-2):
    if [1,2,3] == nums[i:i+3]:
      return True
  return False

def string_match(a, b):
  def splitter(str,n):
    result = []
    for i in range(0,len(str)-n+1):
      result.append(str[i:i+n])
    return result
  count = 0
  b_splitted = splitter(b,2)
  
  for pair in splitter(a,2):
    if pair in splitter(b,2):
      count += 1
  return count

def string_match(a, b):
  """
  Given 2 strings, a and b, return the number of the positions where they 
  contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
  since the "xx", "aa", and "az" substrings appear in the same place in 
  both strings. 
  """
  def splitter(str,n):
  	"""Helper that returns every n-length substring"""
    result = []
    for i in range(0,len(str)-n+1):
      result.append(str[i:i+n])
    return result
    
  count = 0
  a_split = splitter(a,2)
  b_split = splitter(b,2)
  
  for i in range(0, len(a_split) if len(a_split)<=len(b_split) else len(b_split)):
    if a_split[i] == b_split[i]:
      count += 1
      
  return count