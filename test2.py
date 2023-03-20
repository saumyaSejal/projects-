from tkinter import *
import voterid2
from PIL import ImageTk,Image
import smtplib
from tkinter import messagebox
import pymysql
import rsa
import re 
import hashlib 
class Login:

   def __init__(self,root):
         self.root=root
         self.root.title("Voter Registration ")
         self.root.geometry("1200x800+0+0") #for dimension3500x700 in middle
         self.root.config(bg="yellow")
         self.register()

   def loginform(self):

      Frame_login=Frame(self.root,bg="yellow")

      Frame_login.place(x=0,y=0,height=700,width=800)
      self.bg=ImageTk.PhotoImage(file="cybersec project/background.jpg") #self.bg object of imagetk
      bg=Label(self.root,image=self.bg).place(x=1000,y=0,relwidth=1,relheight=1)

      
      

      frame_input=Frame(self.root,bg='white')

      frame_input.place(x=320,y=130,height=450,width=350)



      label1=Label(frame_input,text="Login ",font=('Consolas',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=75,y=20)



      label2=Label(frame_input,text="ADHAR NO.",font=("Goudy old style",20,"bold"),

                   fg='red',bg='white')

      label2.place(x=30,y=95)

      self.adharverf=Entry(frame_input,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.adharverf.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input,text="voterId",font=("Goudy old style",20,"bold"),

                   fg='red',bg='white')

      label3.place(x=30,y=195)

      self.voteridverf=Entry(frame_input,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.voteridverf.place(x=30,y=245,width=270,height=35)

      label4=Label(frame_input,text="SECRET KEY.",font=("Goudy old style",20,"bold"),

                   fg='red',bg='white')

      label4.place(x=30,y=295)

      self.secretkey=Entry(frame_input,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.secretkey.place(x=30,y=345,width=270,height=35)

   




      btn2=Button(frame_input,text="Login",command=self.logincheck,cursor="hand2",

                  font=("times new roman",15),fg="white",bg="orangered",

                  bd=0,width=15,height=1)

      btn2.place(x=90,y=400)

        

      btn3=Button(frame_input,command=self.register,text="Not Registered?register"

                  ,cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)



   def logincheck(self):

      if self.adharverf.get()=="" or self.voteridverf.get()=="":

         messagebox.showerror("Error","enter all details",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='Saumyasejal1001',

                                database='pythongui2')

            cur=con.cursor()

            cur.execute('select * from register where adhar=%s'

                        ,(self.adharverf.get()))

            row=cur.fetchone()
            envid=row[4]
            skget=self.secretkey.get()
            pvtkparams=re.split('-',skget)
            pl=[]
            for i in pvtkparams:
               pl.append(int(i,16))
            print(pl)
            pvtk=rsa.PrivateKey(pl[0],pl[1],pl[2],pl[3],pl[4])
            encvidbytes=bytes.fromhex(envid)
            viddec=rsa.decrypt(encvidbytes,pvtk).decode()

         
            if(str(self.voteridverf.get()) != str(viddec)):

               messagebox.showerror('Error','Invalid Entry'

                                    ,parent=self.root)

               self.loginclear()

               self.adharverf.focus()

            else:

               self.ballotbox()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f"Error due to:{str(es)}"

                                 ,parent=self.root)
     

      
   

   def register(self):



      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=700,width=1366)
      

      

      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=320,y=130,height=450,width=630)



      label1=Label(frame_input2,text="Registeration",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=45,y=20)



      label2=Label(frame_input2,text="adhar number",font=("Goudy old style",20,"bold"),

                   fg='green',bg='white')

      label2.place(x=30,y=95)

      self.adhar=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.adhar.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Name",font=("Goudy old style",20,"bold"),

                   fg='green',bg='white')

      label3.place(x=30,y=195)

      self.name=Entry(frame_input2,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.name.place(x=30,y=245,width=270,height=35)



      label4=Label(frame_input2,text="age",font=("Goudy old style",20,"bold"),

                   fg='green',bg='white')

      label4.place(x=330,y=95)

      self.age=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.age.place(x=330,y=145,width=270,height=35)



      label5=Label(frame_input2,text="email",

                   font=("Goudy old style",20,"bold"),fg='green',bg='white')

      label5.place(x=330,y=195)

      self.email=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.email.place(x=330,y=245,width=270,height=35)



      btn2=Button(frame_input2,command=self.check,text="Submit"

                  ,cursor="hand2",font=("times new roman",15),fg="white",

                  bg="green",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

                  text="Already Registered?Login",cursor="hand2",

                  font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)





   def check(self):

      if self.adhar.get()==""or self.name.get()==""or self.age.get()==""or self.email.get()=="":

         messagebox.showerror("All Fields Are Required",parent=self.root)

      elif int(self.age.get())<18:

         messagebox.showerror("Error","Not eligible"

                              ,parent=self.root)

      else:

        try:

            con=pymysql.connect(host="localhost",user="root",password="Saumyasejal1001",

                                database="pythongui2")

            cur=con.cursor()

            cur.execute("select * from register where adhar=%s"

                        ,self.adhar.get())

            row=cur.fetchone()
            cur.execute("select * from register where email=%s"

                        ,self.email.get())

            row2=cur.fetchone()



            if (row!=None or row2 != None):

               messagebox.showerror("Error"

               ,"User already Exist,Please login"

                                    ,parent=self.root)

               self.regclear()

               self.adhar.focus()

            else:
                pubk , pvtk=rsa.newkeys(512)
                pvtmsg=str(hex(pvtk.n))+"-"+str(hex(pvtk.e))+"-"+str(hex(pvtk.d))+"-"+str(hex(pvtk.p))+"-"+str(hex(pvtk.q))

                vid=voterid2.sendvoterid(self.email.get(),pvtmsg)
                enc=rsa.encrypt(vid.encode(),pubk)
                encstore=enc.hex()
                




               


                cur.execute("insert into register values(%s,%s,%s,%s,%s)"

                           ,(self.adhar.get(),self.name.get(),

                           self.age.get(),

                           self.email.get(),str(encstore)))

                con.commit()

                con.close()

                messagebox.showinfo("Success","Registeration Succesfull"

                                   ,parent=self.root)

                self.regclear()

        except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}"

                                 ,parent=self.root)



   def ballotbox(self):
       Frame_login=Frame(self.root,bg="white")

       Frame_login.place(x=0,y=0,height=700,width=1366)

       label1=Label(Frame_login,text="cast your vote"

                   ,font=('times new roman',32,'bold'),

                   fg="black",bg='yellow')

       label1.place(x=375,y=100)

       label2=Label(Frame_login,text="group 11"

                   ,font=('times new roman',32,'bold'),

                   fg="black",bg='white')

       label2.place(x=235,y=160)
       
       self.vote=IntVar(Frame_login)
       op1=Radiobutton(Frame_login,text="party 1",value=3,var=self.vote,bg="blue",fg="black").place(x=100,y=300,width=150)
       op2=Radiobutton(Frame_login,text="party 2",value=5,var=self.vote,bg="blue",fg="black").place(x=300,y=300,width=150)
       op3=Radiobutton(Frame_login,text="party 3",value=6,var=self.vote,bg="blue",fg="black").place(x=100,y=400,width=150)
       op4=Radiobutton(Frame_login,text="party 4",value=8,var=self.vote,bg="blue",fg="black").place(x=300,y=400,width=150)
      #radio.validate(vote)      
       btn1=Button(Frame_login,text='submit',command=self.storevote,bg="green",fg="yellow").place(x=100,y=250,width=250,height=50)

     # btn3=Button(Frame_login,text='Save',command=self.save,bg="green",fg="yellow").place(x=300,y=250,width=250,height=50)
      


       btn2=Button(Frame_login,text="LEAVE",command=self.thankyou,

                  font=("times new roman",15),fg="white",bg="green",

                  bd=0,width=15,height=1)

       btn2.place(x=1000,y=10)


   def storevote(self):
         value=self.vote.get()
         if(value==3):
            self.code=351
         elif(value==5):
            self.code=769
         elif(value==6):
            self.code=67
         elif(value==8):
            self.code=25
         else:
            messagebox.showerror('ERROR','plz select an option')
         
         print(self.code)
         adharno = self.adharverf.get()
         to_be_hashed=str(adharno)[5:]+str(self.code)
         print("to be hashed string=",to_be_hashed)
         print("adharsegment=",str(adharno)[5:])
         hashed=hashlib.sha256(str(to_be_hashed).encode())
         hexhashed=hashed.hexdigest()
         print("hashed value=",str(hexhashed),"length=",len(str(hexhashed)))

         try:

            con=pymysql.connect(host='localhost',user='root',password='Saumyasejal1001',

                                database='pythongui2')

            cur=con.cursor()

            cur.execute('select * from votes where adharno=%s'

                        ,(self.adharverf.get()))

            row=cur.fetchone()
            if(row != None):
               messagebox.showerror('Error','already voted',parent=self.root)
            else:
               cur.execute("insert into votes values(%s,%s)"

                           ,(self.adharverf.get(),str(hexhashed)))

               con.commit()

               con.close()


         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}"

                                 ,parent=self.root) 


   def thankyou(self):
      Frame_thanks=Frame(self.root,bg="green").place(x=0,y=0,height=700,width=1366)


      
      labthank=Label(Frame_thanks,text="thank you for your vote"

                   ,font=('times new roman',36,'bold'),

                   fg="white",bg='yellow')

      labthank.place(x=375,y=100)
      retbtn=Button(Frame_thanks,text="login page",command=self.loginform,font=("consolas",24,"bold"),bg="black",fg="green").place(x=100,y=83,width=200,height=80)


   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)



   def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)



root=Tk()

ob=Login(root)

root.mainloop()



