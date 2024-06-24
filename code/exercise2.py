# WRITE YOUR CODE HERE
def move_to_bottom(d, key):
    if key not in d:
      return 'The key is not in the dictionary'
    else:
      value = d.pop(key)
      d[key] = value
    return d

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 4)
  print(example_dict)