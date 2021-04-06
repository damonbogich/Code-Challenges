
#output: true
s1 = "mississippi"
p1 = "mis*is*ip*."
#output: false
s2 = 'aa' 
p2 = 'a'
#output: true
s3 = 'aa'
p3 = 'a*'
#output: true
s4 = 'ab'
p4 = '.*'
# output: true
s5 = 'aab'
p5 = 'c*a*b'

def isMatch(s,p):
    #Need pattern to contain match of string
    #'*' means you can repeat the previous character as many times as necessary
    #'.' can represent any character
    
    #Case 1: one or both are empty
    #Assumption: if one is empty then both must be in order to match
    if len(s) == 0:
        if len(p) == 0:
            return True
        else:
            return False
    #done and if this is wrong, maybe string can be empty but p must only contain a '*' at beginning
    #or maybe '.' can represent nothing, but I think the way I have it is correct

    #Case 2: neither empty and no symbols in the pattern
    #Check if pattern has either character
    #If pattern does not contain either
        #then the pattern must contain the substring of string
    special_characters = ['.', '*']
    matched_list = [characters in special_characters for characters in p]
    #If neither value is in matched found in pattern then substring must be found there
    if True not in matched_list:
        print(s, p)
        if s in p:
            return True
        else:
            return False

    #Loop through pattern
    current_string_index = 0
    last_string_index = len(s) - 1

    # #If i == last pattern index we are in last loop through pattern
    # last_pattern_index = len(p) - 1
    # #this variable will be set to the previous value in pattern when '*' is hit in loop
    # star_character = ''

    for i in range(len(p)):
        current_pattern_character = p[i]
        current_string_character = s[current_string_index]
        #how will we know we have a match?????????????
        #last index in string has its value matched

        #Case 1: Current pattern character matches current string character or is '.'
        if current_pattern_character == current_string_character or current_pattern_character == '.':
            if current_string_index == last_string_index:
                return True
            #increment current string index for next iteration
            else:
                current_string_index += 1
                continue
        #Case 2: '*' is hit in pattern
        elif current_pattern_character == '*':
            #If this is the first looop then the '*' is inconsequential
            if i == 0:
                continue
            else:
                #previous character in pattern
                repeat_character = p[i - 1]
                #If '.' repeats it is always True
                if repeat_character == '.':
                    return True

                looping = True
                #we will then want to compare the repeat character to the current string character
                while looping: 
                    current_string_character = s[current_string_index]
                    #if they match, we will want to continue checking if the repeat character matches
                    #The next character in string until it does not
                    if repeat_character == current_string_character:
                        if current_string_index == last_string_index:
                            return True
                        else:
                            current_string_index += 1
                    #If they do not match, we will not increment or reset current string index, but we
                    #will move on to next iteration of the loop through pattern
                    else:
                        looping = False
                continue
        #case 3: the current pattern character doesn't match the current string character
        else:
            current_string_index = 0



    return False


            
            # if i == 0:
            #     continue
            # else: 
            #     #previous character in pattern 
            #     repeat_character = p[i - 1]
            #     looping = True
            #     #If '.' repeats it is always True
            #     if repeat_character == '.':
            #             return True
            #     #we will then want to compare the repeat character to the current string character
            #     while looping:
            #         current_string_character = s[current_string_index]
                    
            #         if repeat_character == current_string_character:
            #             current_string_index += 1
            #         else:
            #             looping = False
            #     continue
                #if they match, we will want to continue checking if the repeat character matches
                    #The next character in string until it does not
                #If they do not match, we will not increment or reset current string index, but we
                    #will move on to next iteration of the loop through pattern

        #Case 2: '*' is hit in pattern
        #If '*' is first character in pattern:
            #disreguard the star and move to next iteration of pattern
        #If not, we want to stay in this loop and keep checking if next letter in string matches
        #the character that came before '*'
        #If the character before the '*' was a '.' then we return True

new_s = 'ab'
new_p = '.*c'

print(isMatch(s5, p5))

# Input: s='ab', p='.*'
# output: True
# expected: False


# Input: s = "ab", p = ".*c"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".