import getpass # i think this is a jupyter module only
#the get pass suppposed to be be : password = getpass.getpass("Password : ) it worked on jupyter tho
import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587)#587 all email is encrypted
smtp_object.ehlo()
smtp_object.starttls()
email = input("Email : ")
password = input("Password : ")
smtp_object.login(email,password)
froms = email
to = email
subject =input('enter subject : ')
message = input('enter message : ')
msg = "Subject: "+ subject + '\n' + message
smtp_object.sendmail(froms,to,msg)
smtp_object.quit()