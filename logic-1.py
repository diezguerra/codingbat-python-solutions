def cigar_party(cigars, is_weekend):
  """
  When squirrels get together for a party, they like to have cigars. A squirrel
  party is successful when the number of cigars is between 40 and 60, inclusive.
  Unless it is the weekend, in which case there is no upper bound on the number
  of cigars. Return True if the party with the given values is successful, or
  False otherwise. 
  """
  return cigars >= 40 if is_weekend else cigars in range(40,61)

def date_fashion(you, date):
  """
  You and your date are trying to get a table at a restaurant. The parameter 
  "you" is the stylishness of your clothes, in the range 0..10, and "date" is 
  the stylishness of your date's clothes. The result getting the table is 
  encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very 
  stylish, 8 or more, then the result is 2 (yes). With the exception that if 
  either of you has style of 2 or less, then the result is 0 (no). Otherwise 
  the result is 1 (maybe). 
  """
  if you <= 2 or date <=2:
    return 0
  elif you >=8 or date >=8:
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  """
  The squirrels in Palo Alto spend most of the day playing. In particular, 
  they play if the temperature is between 60 and 90 (inclusive). Unless it is 
  summer, then the upper limit is 100 instead of 90. Given an int temperature 
  and a boolean is_summer, return True if the squirrels play and False 
  otherwise. 
  """
  return temp in range(60, 101 if is_summer else 91)

def caught_speeding(speed, is_birthday):
  """
  You are driving a little too fast, and a police officer stops you. Write code
  to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 
  2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 
  and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. 
  Unless it is your birthday -- on that day, your speed can be 5 higher in all 
  cases. 
  """
  speeding = speed - (65 if is_birthday else 60)
  if speeding > 20:
    return 2
  elif speeding > 0:
    return 1
  else:
    return 0

def sorta_sum(a, b):
  """
  Given 2 ints, a and b, return their sum. However, sums in the range 10..19 
  inclusive, are forbidden, so in that case just return 20. 
  """
  return 20 if a+b in range(10,20) else a+b

def alarm_clock(day, vacation):
  pronto = "7:00" if not vacation else "10:00"
  tarde = "10:00" if not vacation else "off"
  return pronto if day not in [6,0] else tarde

def alarm_clock(day, vacation):
  """
  Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a 
  boolean indicating if we are on vacation, return a string of the form "7:00" 
  indicating when the alarm clock should ring. Weekdays, the alarm should be 
  "7:00" and on the weekend it should be "10:00". Unless we are on vacation --
  then on weekdays it should be "10:00" and weekends it should be "off". 
  """
  week_preset = "7:00" if not vacation else "10:00"
  weekend_preset = "10:00" if not vacation else "off"
  return week_preset if day not in [6,0] else weekend_preset

def love6(a, b):
  """
  The number 6 is a truly great number. Given two int values, a and b, 
  return True if either one is 6. Or if their sum or difference is 6. 
  """
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
  """
  Given a number n, return True if n is in the range 1..10, inclusive. 
  Unless "outsideMode" is True, in which case return True if the number is 
  less or equal to 1, or greater or equal to 10. 
  """
  if n == 1 or n == 10:
    return True
  return (n in range(1,11)) ^ outside_mode

def near_ten(num):
  """
  Given a non-negative number "num", return True if num is within 2 of a 
  multiple of 10. Note: (a % b) is the remainder of dividing a by b, 
  so (7 % 5) is 2. 
  """
  #within = num - (num+2)/10*10
  #return within in range(-2,3)
  within = num%((num/10)*10) if num >= 10 else num
  return within in [8,9,0,1,2]