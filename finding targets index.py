def searchInsert():
    nums = [1, 2, 4, 5, 6]
    target = int(input("Enter the target: "))
    
    for i in range(len(nums)):
        if nums[i] >= target :
            print(f"Target found at index no.{i}")
            return i
    return len(nums)

searchInsert()
