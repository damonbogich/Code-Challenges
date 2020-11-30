#Leetcode - Add two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#example: 

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(ListNode_1, ListNode_2):
    #create empty lists for each node_list to put its values in
    node_value_list_1 = []
    node_value_list_2 = []

    #Loop through linked lists and put their its values in empty node_value_list in the correct order
    while ListNode_1 is not None:
        node_value_list_1.insert(0, ListNode_1.val)
        ListNode_1 = ListNode_1.next
        
    while ListNode_2 is not None:
        node_value_list_2.insert(0, ListNode_2.val)
        ListNode_2 = ListNode_2.next
        
    #Converts each list of numbers to a single number
    strings = [str(item) for item in node_value_list_1]
    single_string = "".join(strings)
    single_integer = int(single_string)
        
    strings_2 = [str(item) for item in node_value_list_2]
    single_string_2 = "".join(strings_2)
    single_integer_2 = int(single_string_2)
    
    #Add both numbers
    list_sum = single_integer + single_integer_2
    #Turn that single number back to a list of numbers
    list_of_nums = [int(x) for x in str(list_sum)]
    #Reverse that List of numbers 
    list_of_nums.reverse()
    
    node_list = []
    #Make every number in list_of_nums a node value
    for i in list_of_nums:
        node_list.append(ListNode(i))
    #Link all of the nodes together
    for i in range(len(node_list) - 1):
        node_list[i].next = node_list[i + 1]
    
    #return the head of the node list
    return node_list[0]

#node list 1
node1_1 = ListNode(2)
node2_1 = ListNode(4)
node3_1 = ListNode(3)

node1_1.next = node2_1
node2_1.next = node3_1

#node list 2
node1_2 = ListNode(5)
node2_2 = ListNode(6)
node3_2 = ListNode(4)

node1_2.next = node2_2
node2_2.next = node3_2



print(addTwoNumbers(node1_1, node1_2))