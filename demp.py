def recursion_binary_search(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            print("Element Found")
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1

arr=[1,2,3,4,5,6,7,8,9]
target=8
rishu= recursion_binary_search(arr,target)
print("index", rishu)
print("xyz")

