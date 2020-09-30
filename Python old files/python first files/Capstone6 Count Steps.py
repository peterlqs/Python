num = int(input("Enter a number: "))
count = 0
def odd():
    global num,count
    while num != 1:
        num /= 2
        if num % 2 !=0:
            even()
        count +=1
def even():
    global num,count
    while num!=1:
        num=num *3+1
        if num % 2 ==0:
            odd()
        count+=1
if num % 2 ==0:
    odd()
else:
    even()
if num==1:
    print(count)