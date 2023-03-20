import random
import pymysql
import smtplib


def voterid():
    vid=""
    for i in range(4):
        d=random.randint(0,9)
        vid=vid+str(d)
    return vid

a=voterid()

# trying to connect to the mail 

server=smtplib.SMTP('smtp.gmail.com',587 ) #the 587 is port for only gmail server
#the prev step is basically opening gmail on xerver

'''server.starttls() #tls is a protocol for secure mailing
server.login('saumyasejal1001@gmail.com','vsoquauzfjvnzwrp')
msg="thank you for registering. Your voter id is- "+str(a)+"plz do not share it with anyone"
server.sendmail('saumyasejal1001@gmail.com','saumyasejal10010@gmail.com',msg)
server.quit()'''

def sendvoterid(email):
    newvid=voterid()
    server=smtplib.SMTP('smtp.gmail.com',587 ) #the 587 is port for only gmail server
    #the prev step is basically opening gmail on xerver
    server.starttls() #tls is a protocol for secure mailing
    server.login('saumyasejal1001@gmail.com','vsoquauzfjvnzwrp')
    msg="thank you for registering. Your voter id is- "+str(newvid)+"plz do not share it with anyone"
    server.sendmail('saumyasejal1001@gmail.com',email,msg)
    server.quit()
    return newvid


