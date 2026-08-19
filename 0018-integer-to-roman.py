class Solution:

  def intToRoman(self, num: int) -> str:
    # Ordered mapping of values to their corresponding Roman symbols
    val_to_symbol = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    res = []
    for value, symbol in val_to_symbol:
      if num == 0:
        break
      # Determine how many times this symbol's value fits into num
      count = num // value
      # Append the symbol repeated 'count' times
      res.append(symbol * count)
      # Keep only the remaining remainder
      num %= value

    return ''.join(res)