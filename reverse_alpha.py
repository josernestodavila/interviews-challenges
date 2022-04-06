"""
# Reverse alpha

Reverse the alpha characters in a string and keep all the non alpha characters in the same place.
"""
def reverse_alpha(string):
  original = list(string)
  start = 0
  end = len(original) - 1

  while start < end:
    if original[start].isalpha() and original[end].isalpha():
      original[start], original[end] = original[end], original[start]
      start += 1
      end -= 1
      continue

    if original[start].isalpha():
      end -= 1
    else:
      start += 1

  print(original)
  return ''.join(original)

def test_reverse_alpha():
  assert reverse_alpha('a.b*d') == 'd.b*a'
  assert reverse_alpha('.ab') == '.ba'
  assert reverse_alpha('a...') == 'a...'
  assert reverse_alpha('a...b') == 'b...a'
  assert reverse_alpha('a*b,c@d#eaffeqw)2a*a#31&$*@abe') == 'e*b,a@a#awqeffa)2e*d#31&$*@cba'

test_reverse_alpha()
