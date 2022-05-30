def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]
print('List of strings:')
print(colors)
print("\nList of lists:")
print(strings_to_listOflists(colors))