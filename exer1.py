num1=[5,8,23,55,33,82]

# num1.pop(3)
# num1.pop(2)
# num1.pop(0)
# print(num1)

new_list=[j for i,j in enumerate(num1) if i not in [0,2,3]]
print(new_list)



