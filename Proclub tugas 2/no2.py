def twoSum(arr, target):
    for i in arr:
        for j in arr:
            if i + j == target:
                return [arr.index(i), arr.index(j)]

print(twoSum([1, 2, 3, 4, 6], 6))
print(twoSum([2, 5, 9, 11], 11))