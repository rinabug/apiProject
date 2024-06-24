# WRITE YOUR CODE HERE
def is_nested(d):
  for value in d.values():
    if isinstance(value, (list, tuple, dict)):
      return True
    return False

# test code below
