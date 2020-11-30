
# def reverse(x):
# #maybe add boolean to represent if input is negative or positive

#     if x < 0:
#         y = -x
#         # convert integer into list 
#         int_list = [int(n) for n in str(y)]
#         # reverse the list
#         int_list.reverse()
#         # convert back to integer
#         string_list = [str(n) for n in int_list]
#         single_string = "".join(string_list)
#         num_conversion = int(single_string)
#         if -(num_conversion) <= 2147483647 and -(num_conversion) >= -2147483648:
#             return -(num_conversion)
#         else:
#             return 0
#     else:
#         int_list = [int(n) for n in str(x)]
#         # reverse the list
#         int_list.reverse()
#         # convert back to integer
#         string_list = [str(n) for n in int_list]
#         single_string = "".join(string_list)
#         num_conversion = int(single_string)
#         if num_conversion >= -2147483648 and num_conversion <= 2147483647:
#             return num_conversion
#         else:
#             return 0

def reverse(x):
    negative = False 
    if x < 0:
        negative = True
        x = -x
    int_list = [int(n) for n in str(x)]
    int_list.reverse()
    string_list = [str(n) for n in int_list]
    single_string = "".join(string_list)
    num_conversion = int(single_string)
    if negative == True:
        num_conversion = -(num_conversion)
    if num_conversion >= -2147483648 and num_conversion <= 2147483647:
        return num_conversion
    else:
        return 0
#knnd
    
    



print(reverse(-2147483648))