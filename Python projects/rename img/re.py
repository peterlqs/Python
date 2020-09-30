import os
s=0
dir = input('Your directory : ').replace("\"","")
os.chdir(dir)
num = input('Number that took pic in order (with , between) : ').split(',')
hw = input('Number of hw in order (with , between) : ').split(',')
for i in hw:
    for f in num:
        file = os.listdir(dir)[s]
        os.rename(file,str(f)+"_"+str(i)+".jpg")
        s+=1
print('Done')
