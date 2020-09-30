import random
flip_time=int(input("Number of flips : "))
list =0
list1 =0
list3 =1,2
for i in range(flip_time):
    dunphy =random.choice(list3)
    if dunphy ==1:
        list +=1
    else:
        list1 +=1
print("Tail :",list)
print('Head :', list1)