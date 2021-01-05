
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#Goal: return the indices of the two values that add up to the target

def two_sum(arr, target):
    if len(arr) == 2:
        return [0, 1]
    #make a dictionary to store value, index, and difference
    num_dict = {}
    #loop through the array and add each number to the dictionary
    for i in range(len(arr)):
        value = arr[i]
        difference = target - value
        if value not in num_dict:
            num_dict[value] = (i, difference)
        elif value in num_dict and value == difference:
            return [i, num_dict[value][0]]
        #now check if the difference is also in the dictionary
        #But make sure that difference is not the same as value
        if difference in num_dict and difference != value:
            return [num_dict[difference][0], num_dict[value][0]]

nums = [3,2,3]
target = 6  
print(two_sum(nums, target))