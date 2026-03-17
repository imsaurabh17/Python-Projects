def binary_search(arr: list, target: int) -> int:
    """This function will output the index of a target number from a given array"""

    for index, num in enumerate(arr):
        if num == target:
            return index
        
    else:
        return f"Target isn't in the provided array"
    

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8]
    target = 10
    print(binary_search(arr,target))