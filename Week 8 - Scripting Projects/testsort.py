def isSorted(list):
    for L in range(len(list) - 1):
        if list[L] > list[L + 1]:
            return False
    return True

testLists = [
    [], 
    [1],
    [1, 2, 3],
    [4, 6, 5],
    [2, 2, 2, 2, 4],
    ]

for list in testLists:
    if isSorted(list):
        print([list], "This list is sorted")
    else:
        print([list], "This list is not sorted")
