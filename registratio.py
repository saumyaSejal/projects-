import PIL 
from PIL import ImageTk,Image #imagetk module helps in dealing with jpg
from tkinter import *
from tkinter import messagebox
import pymysql

class register:
    
    def __init__(self,root):
        self.root=root

        self.root.title("Login and registration system for Apps")

        self.root.geometry("1366x700+0+0")

        self.root.resizable(False,False)

        self.registerform()
    

    def registerform(self):
        self.root=root
        self.root.title("Voter Registration ")
        self.root.geometry("1200x800+0+0") #for dimension3500x700 in middle
        self.root.config(bg="yellow")
        #decorations
        self.bg=ImageTk.PhotoImage(file="cybersec project/background.jpg") #self.bg object of imagetk
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        frame1=Frame(self.root,bg="white")
        frame1.place(x=0,y=100,width=500,height=500)
        title=Label(frame1,text="REGISTER",font=("times new roman",32,"underline"),bg="green",fg="black").place(x=20,y=30)
        adhar=Label(frame1,text="Adhar no.",font=("times new roman",18,"underline"),bg="white",fg="black").place(x=50,y=130)
        self.txt_adhar=Entry(frame1,font=("times new roman",12),bg="light grey").place(x=150,y=130,width=250)

        name=Label(frame1,text="name",font=("times new roman",18,"underline"),bg="white",fg="black").place(x=50,y=180)
        self.txt_name=Entry(frame1,font=("times new roman",12),bg="light grey").place(x=150,y=180,width=250)
        
        age=Label(frame1,text="Age",font=("times new roman",18,"underline"),bg="white",fg="black").place(x=50,y=260)
        self.txt_age=Entry(frame1,font=("times new roman",12),bg="light grey").place(x=150,y=260,width=50)

        email=Label(frame1,text="Email",font=("times new roman",18,"underline"),bg="white",fg="black").place(x=50,y=340)
        self.txt_email=Entry(frame1,font=("times new roman",12),bg="light grey").place(x=150,y=340,width=350)
        
        #submit button
        submit=Button(frame1,text="SUBMIT",command=self.check,bg="black",fg="green").place(x=80,y=400,width=80,height=50)
    
    
    def check(self):

      if self.txt_adhar.get()==""or self.txt_name.get()==""or self.txt_age.get()==""or self.txt_email.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.txt_age.get()<18:

         messagebox.showerror("Not eligible to vote"

                              ,parent=self.root)

      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="Saumyasejal1001",

                                database="pythongui")

            cur=con.cursor()

            cur.execute("select * from register where Adhar=%s"

                        ,self.txt_adhar.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error"

               ,"User already Exist,Please try with another Email"

                                    ,parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"

                           ,(self.txt_adhar.get(),self.txt_name.get(),

                           self.txt_age.get(),

                           self.txt_email.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull"

                                   ,parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}"

                                 ,parent=self.root)
    #clear func
    def regclear(self):

      self.txt_adhar.delete(0,END)

      self.txt_name.delete(0,END)

      self.txt_age.delete(0,END)

      self.txt_email.delete(0,END)    

root=Tk()
obj=register(root)
root.mainloop()