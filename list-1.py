def first_last6(nums):
  """
  Given an array of ints, return True if 6 appears as either the first or last
  element in the array. The array will be length 1 or more.
  """
  return 6 in [nums[0],nums[-1]]


def same_first_last(nums):
  """
  Given an array of ints, return True if the array is length 1 or more, and the
  first element and the last element are the same.
  """
  return len(nums) > 0 and nums[0] == nums[-1]


def make_pi():
  """
  Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
  """
  return [3,1,4]


def common_end(a, b):
  """
  Given 2 arrays of ints, a and b, return True if they have the same first
  element or they have the same last element. Both arrays will be length 1
  or more.
  """
  return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
  """Given an array of ints length 3, return the sum of all the elements."""
  return sum(nums)


def rotate_left3(nums):
  """
  Given an array of ints length 3, return an array with the elements "rotated
  left" so {1, 2, 3} yields {2, 3, 1}.
  """
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  """
  Given an array of ints length 3, return a new array with the elements in
  reverse order, so {1, 2, 3} becomes {3, 2, 1}.
  """
  return [nums[2],nums[1],nums[0]]

def max_end3(nums):
  """
  Given an array of ints length 3, figure out which is larger between the
  first and last elements in the array, and set all the other elements to be
  that value. Return the changed array.
  """
  return [nums[0]]*3 if nums[0] >= nums[-1] else [nums[-1]]*3

def sum2(nums):
  """
  Given an array of ints, return the sum of the first 2 elements in the array.
  If the array length is less than 2, just sum up the elements that exist,
  returning 0 if the array is length 0.
  """
   return sum(nums[:2])

def middle_way(a, b):
  """
  Given 2 int arrays, a and b, each length 3, return a new array length 2
  containing their middle elements.
  """
  return [ a[1] , b[1] ]

def make_ends(nums):
  """
  Given an array of ints, return a new array length 2 containing the first
  and last elements from the original array. The original array will be
  length 1 or more.
  """
  return [ nums[0] , nums[-1] ]

def has23(nums):
  """Given an int array length 2, return True if it contains a 2 or a 3."""
  return 2 in nums or 3 in nums
