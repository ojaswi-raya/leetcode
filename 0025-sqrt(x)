class Solution:

  def mySqrt(self, x: int) -> int:
    if x < 2:
      return x

    left, right = 1, x // 2
    ans = 0

    while left <= right:
      mid = left + (right - left) // 2
      if mid * mid <= x:
        ans = mid
        left = mid + 1  # Try to find a larger integer
      else:
        right = mid - 1  # mid squared is too large

    return ans