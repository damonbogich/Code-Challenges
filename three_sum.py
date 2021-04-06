def threeSum(nums):
  res = []
  current = 0
  compare = current + 1
  last_index = len(nums) - 1

  if len(nums) < 3:
    return res

  while current < last_index - 1:
    sum_list = []
    #always after current
    
    #number being compared to the rest
    pointer = nums[current]
    pointer2 = nums[compare]
    #sum of pointer values
    total = pointer + pointer2

    #check if the opposite of the sum is in list
    if (-total) in nums[compare + 1:last_index + 1]:
        sum_list = [-total, pointer, pointer2]
        sum_list.sort()
        if sum_list not in res:
            res.append(sum_list)
    if compare + 1 != last_index:
        compare += 1
    else:
        current += 1
        compare = current + 1
  return res  
ex1 = [0,-1,1,2,-1,-4]

print(threeSum(ex1))