

# def mostWater(h):
#   #pointers for beginning and end points
#   last_index = len(h) - 1
#   first_index = 0
#   max_area = 0
  
#   #now we need to calculate the max if these were our two points
#   while first_index is not last_index:
#     beginning_pointer_value = h[first_index]
#     end_pointer_value = h[last_index]
#     #difference between indices
#     difference = last_index - first_index
#     area = 0

#     if beginning_pointer_value > end_pointer_value:
#       area = difference * end_pointer_value
#       last_index -= 1

#     elif end_pointer_value > beginning_pointer_value:
#       area = difference * beginning_pointer_value
#       first_index += 1

#     if area > max_area:
#       max_area = area
    
#   print(max_area)

def mostWater(h):
    last_index = len(h) - 1
    first_index = 0
    max_area = 0
    
    #loop through until all numbers in list are covered
    while last_index != first_index:
        #difference between indices will be multiplied by the shorter of the two
        #values to determine the max water contained between the two points
        difference = last_index - first_index
        beginning_value = h[first_index]
        ending_value = h[last_index]
        area = 0

        if beginning_value > ending_value:
            area = difference * ending_value
            #since end value is smaller, we will decrement last index to get new value
            last_index -= 1
        elif ending_value > beginning_value:
            area = difference * beginning_value
            #since beginning value is smaller, we will increment first index to get new value
            first_index += 1
        elif ending_value == beginning_value:
            #we will move the one that is closer to the middle
            #compare difference of first index to 0 to
            #distance of last index to len(list) - 1
            area = difference * beginning_value
            distance_from_end = (len(h) - 1) - last_index
            if distance_from_end > first_index:
                last_index -= 1
            else:
                first_index += 1
        if area > max_area:
            max_area = area
            print(max_area)
    return max_area

      
    



  

height = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]
height3 = [4,3,2,1,4]
mostWater(height2)