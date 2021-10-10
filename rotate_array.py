def reverse23(digits, num_rotate):
  # get the length of digits
  length_array = len(digits)


  num_not_touched = digits[0:(length_array - num_rotate)]
  num_moved_upfront = digits[(length_array - num_rotate):length_array]
  new_output = num_moved_upfront + num_not_touched
  return new_output


n = [3, 8, 9, 7, 6]
cycles = 7
output = reverse23(n, cycles)
print(n)
print(output)


