def sort_n(nums_str):
    result = sorted(nums_str, key=lambda el: int(el))
    return result
nums_str = ['4','12','45','-12','-500']
print("Original list:")
print(nums_str)
print("\nSorted:")
print(sort_n(nums_str))