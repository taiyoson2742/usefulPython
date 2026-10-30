#written 10.30.26
def bubbleSort(items):
    for i in range(len(items)-1, 0, -1):
        for j in range(i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

nums = [1,8,4,6,5,9]
print(nums)
print(bubbleSort(nums))
