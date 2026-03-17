def binary_search(arr: list, target: int) -> int:
    """This function will output the index of a target number from a given array"""

    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] <= target:
            left = mid + 1

        else:
            right = mid - 1
    

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8]
    target = 5
    print(binary_search(arr,target))