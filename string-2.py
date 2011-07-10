def double_char(str):
  """
  Given a string, return a string where for every char in the original, 
  there are two chars. 
  """
  #new_str = "".join([i+j for i,j in zip(list(str),list(str))])
  new_str = ""
  for char in str:
    new_str += char*2
  return new_str

def count_hi(str):
  """
  Return the number of times that the string "hi" appears anywhere 
  in the given string. 
  """
  return str.count("hi")

def cat_dog(str):
  """
  Return True if the string "cat" and "dog" appear the same number of 
  times in the given string. 
  """
  return str.count("cat") == str.count("dog")

def count_code(str):
  """
  Return the number of times that the string "code" appears anywhere in the 
  given string, except we'll accept any letter for the 'd', so "cope"  and 
  "cooe" count.
  """
  count = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count

def end_other(a, b):
  """
  Given two strings, return True if either of the strings appears at the very 
  end of the other string, ignoring upper/lower case differences (in other 
  words, the computation should not be "case sensitive").
  """
  long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
  return long_s.lower().endswith(short_s.lower())

  def xyz_there(str):
  """
  Return True if the given string contains an appearance of "xyz" where 
  the xyz is not directly preceeded by a period (.). So "xxyz" counts but
  "x.xyz" does not. 
  """
  i=0
  while "xyz" in str[i:]:
    if str[i-1+str[i:].index("xyz")] != ".":
      return True
    i += str[i:].index("xyz")+2
  return False