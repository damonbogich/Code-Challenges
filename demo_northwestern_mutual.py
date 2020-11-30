# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].



a = [1, 3, 6, 4, 1, -2, -4, 2]
n = 6

smallest_possible = 1

new_list = [i for i in a if i > 0]
new_list.sort()
print(new_list, 'new')
if len(new_list) == 0 or new_list[0] != 1:
    print(1, 'first if statement')
else:
    #while loop - compare each number in list to the number before it
    current = 0
    for i in range(len(new_list)):
        if (new_list[i] - 1) != current and new_list[i] != current:
            print(new_list[i] - 1, 'if statement return ') 
        else:
            current = new_list[i]
    









