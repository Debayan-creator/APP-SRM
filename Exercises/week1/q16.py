def test_distinct(data):
    if len(data)==len(set(data)):
        return False
    else:
        return True
print(test_distinct([5,5,5]))
print(test_distinct([1,5,7,9]))
