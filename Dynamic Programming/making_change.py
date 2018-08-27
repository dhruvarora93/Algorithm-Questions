def phone_permute_list(digits, mapping):
  if len(digits) == 0:
    return ['']
  else:
    result = []
    for x in phone_permute_list(digits[1:],mapping):
      for y in mapping[digits[0]]:
        result.append(y + x)
    return result



d = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L']}
index=0
print(phone_permute_list('23',d))