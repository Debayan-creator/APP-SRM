def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = "Debayan" 
result = map(change_cases, chrars)
print("\nAfter eliminating duplicate letters:")
print(set(result))