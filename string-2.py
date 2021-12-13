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
  word="co"
  word1="e"
  count=0
  for i in str:
      word2=word+i+word1
      if word2 in str:
          count+=1
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
  if "xyz" in str and ".xyz" not in str:
      return True
  elif "xyz" in str and ".xyz" in str:
      if str.startswith(".xyz") or str.endswith(".xyz"):
          return False
      else:
          return True
  elif ".xyz" in str and "xyz" not in str:
      return False
  else:
    return False
