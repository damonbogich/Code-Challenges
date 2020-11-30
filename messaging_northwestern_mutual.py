s = "bytdag"
a = [4,3,0,1,2,5]

#index of smallest number in person array
smallest_value_index = a.index(min(a))

current_sender = a[smallest_value_index]

current_reciever = a[current_sender]

current_letter = s[current_sender]

return_string_list = []

i = 0

running = True
while running:
    #add letter to string
    return_string_list.append(current_letter)
    if current_reciever == 0 and i > 0:
        break
    #change sender to recieve
    current_sender = current_reciever
    #Set new person to recieve 
    current_reciever = a[current_sender]

    current_letter = s[current_sender]

    if len(return_string_list) == len(s):
        running = False
    i += 1

new_string = ""

return_string = new_string.join(return_string_list)
print(return_string)









