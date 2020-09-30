import random
length = int(input('Input the lenght of ur password: '))
numberofletter = int(input('Input the number of letter in ur password: '))
numberofnumber = int(input('Input the number of number in ur password: '))
counts = 0
count1 = 0
count2 = 0
count3 = 0
password1 = ""
password2 = ""
password3 = ""
password =""
listnumber = '0123456789'
listlowerletter = 'abcdefghijklmnopqrstuvwxyz'
listupperletter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
listsymbol = '!"#$%&'
if length < (numberofletter + numberofnumber):
    print("You typed more letter/number than ur lenght")
if length == (numberofletter + numberofnumber):
    while length >= counts:
        if numberofnumber > count1:
            result1 = random.choice(listnumber)
            count1 += 1
            password1 += result1
            counts += 1
        elif numberofletter > count2:
            result2 = random.choice(listlowerletter+listupperletter)
            count2 += 1
            password2 += result2
            counts += 1
        else:
            password = password1 + password2
            print(password)
            listpassword= list(password)
            random.shuffle(listpassword)
            print("".join(listpassword))
            break
if length > (numberofletter + numberofnumber):
    while length >= counts:
        if numberofnumber > count1:
            result1 = random.choice(listnumber)
            count1 += 1
            password1 += result1
            counts += 1
        elif numberofletter > count2:
            result2 = random.choice(listlowerletter+listupperletter)
            count2 += 1
            password2 += result2
            counts += 1
        elif count3 < (length - (numberofletter + numberofnumber)):
            result3 = random.choice(listsymbol)
            count3 += 1
            password3 += result3
        else:
            password = password1 + password2 + password3
            listpassword= list(password)
            random.shuffle(listpassword)
            print("".join(listpassword))
            break







