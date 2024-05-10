list1=[6,8,9,3,2,5,7,1]
new_list1=list1[:len(list1)//2]
new_list2=list1[len(list1)//2:]
print(new_list1)
print(new_list2)

list2=tuple(new_list1)
list3=tuple(new_list2)
print('tuple 1 is:',list2)
print('tuple 2 is:',list3)



