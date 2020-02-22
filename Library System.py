from tkinter import *
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry
from PIL import ImageTk,Image
from tkinter import filedialog
mainWidth=1000
mainHeight=640
main = Tk()
main.geometry(str(mainWidth)+"x"+str(mainHeight))
main.resizable(0,0)
main.title("Library Book Manager")

#Create Library DB

connectionInstance = pymysql.connect(host = "127.0.0.1", user = "root", password = "",charset = "utf8mb4", cursorclass = pymysql.cursors.DictCursor)

try:
    cursorInsatnce        = connectionInstance.cursor()                                    

    sqlStatement            = "CREATE DATABASE " + "LibraryDB"  

    cursorInsatnce.execute(sqlStatement)
    
except Exception as e:

    print("Exeception occured:{}".format(e))

finally:
    connectionInstance.close()
    
try:
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()

    sql=""" create table users(
    Id int primary key auto_increment,
    Username char(100) not null,
    password char(20) not null,
    accountType char(20) not null)"""
    
    cursor.execute(sql)

    db.close()
except Exception as e:
    print(format(e))

try:
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()

    sql2=""" create table books(
    Id int primary key auto_increment,
    title char(100) not null,
    author char(100) not null,
    isbn char(100) not null,
    subject char(100) not null,
    type char(100) not null,
    numberOfCopies int not null,
    usageAccountType char(100) not null,
    price int not null,
    publisher char(100) not null,
    pubDate char(10) not null,
    imageName char(255) default 'default.jpg' not null,
    Note char(255) not null  )"""

    cursor.execute(sql2)

    db.close()
except Exception as e:
    print(format(e))

try:
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()

    sql2=""" create table booksBorrowed(
    Id int primary key auto_increment,
    studentID int not null references users(id) ,
    bookID int not null references books(id),
    borroweddate timestamp default current_timestamp)"""

    cursor.execute(sql2)

    db.close()
except Exception as e:
    print(format(e))

#Login & Signup Frame

root = LabelFrame(main)
root.pack(expand='yes',fill='both')

loginFrame = LabelFrame(root ,text="Login",font=('Ubuntu Mono',20),padx=50,pady=100)
signupFrame = LabelFrame(root,text="Signup",font=('Ubuntu Mono',20),padx=50,pady=50)
loginFrame.pack(side="right",expand='yes')
signupFrame.pack(side="left",expand='yes')

#Books frame for Staff Members and Users

ussMain = LabelFrame(main)
bookMain = LabelFrame(main)

def enter2(event):
    canvas2.bind_all("<MouseWheel>",mouse_wheel2)
def leave2(event):
    canvas2.unbind_all("<MouseWheel>")

def myfunction2(event):
    canvas2.configure(scrollregion=canvas2.bbox("all"),width=mainWidth-30,height=mainHeight-100)

def mouse_wheel2(event):
    if event.num==5 or event.delta==-120:
        canvas2.yview_scroll(1,"units" )
    if event.num==4 or event.delta ==120:
        canvas2.yview_scroll(-1,"units" )
                        
myframe2=Frame(ussMain,relief=GROOVE,width=mainWidth,height=mainHeight,bd=0)
myframe2.place(x=0,y=90)


canvas2=Canvas(myframe2)



frame2=Frame(canvas2)
myscrollbar2=Scrollbar(myframe2,orient="vertical",command=canvas2.yview)
canvas2.configure(yscrollcommand=myscrollbar2.set)

myscrollbar2.pack(side="right",fill="y")
canvas2.pack(side="left")
canvas2.create_window((0,0),window=frame2,anchor='nw')
frame2.bind("<Configure>",myfunction2)

canvas2.bind('<Enter>', enter2)
canvas2.bind('<Leave>', leave2)


def bookDetails(result):
    ussMain.pack_forget()
    bookMain.lift()
    bookMain.pack(fill=BOTH ,expand=TRUE, side=LEFT)

    global image3
    global pic3

    global  bookDetailsLabel1 
    global  bookDetailsLabel2 
    global  bookDetailsLabel3 
    global  bookDetailsLabel4 
    global  bookDetailsLabel5 
    global  bookDetailsLabel6 
    global  bookDetailsLabel7 
    global  bookDetailsLabel8 
    global  bookDetailsLabel9 
    global  bookDetailsLabel10
    global  bookDetailsLabel11

    bookDetailsLabel1 =Label(bookMain,text=result[1],wraplength=250)
    bookDetailsLabel2 =Label(bookMain,text=result[2],wraplength=250)
    bookDetailsLabel3 =Label(bookMain,text=result[3],wraplength=250)
    bookDetailsLabel4 =Label(bookMain,text=result[4],wraplength=250)
    bookDetailsLabel5 =Label(bookMain,text=result[5],wraplength=250)
    bookDetailsLabel6 =Label(bookMain,text=result[6],wraplength=250)
    bookDetailsLabel7 =Label(bookMain,text=result[7],wraplength=250)
    bookDetailsLabel8 =Label(bookMain,text=result[8],wraplength=250)
    bookDetailsLabel9 =Label(bookMain,text=result[9],wraplength=250)
    bookDetailsLabel10 =Label(bookMain,text=result[10],wraplength=250)
    bookDetailsLabel11 =Label(noteFrame,text=result[12],font=('ubuntu mono',18),wraplength=700)
    bookDetailsLabel1.grid(row=1, column=1,sticky=W) 
    bookDetailsLabel2.grid(row=2, column=1,sticky=W)
    bookDetailsLabel3.grid(row=3, column=1,sticky=W)
    bookDetailsLabel4.grid(row=4, column=1,sticky=W)
    bookDetailsLabel5.grid(row=5, column=1,sticky=W)
    bookDetailsLabel6.grid(row=6, column=1,sticky=W)
    bookDetailsLabel7.grid(row=7, column=1,sticky=W)
    bookDetailsLabel8.grid(row=8, column=1,sticky=W)
    bookDetailsLabel9.grid(row=9, column=1,sticky=W)
    bookDetailsLabel10.grid(row=10, column=1,sticky=W)
    bookDetailsLabel11.grid(row=12, column=1,padx=30,pady=40)
    path="images\\"+str(result[11])
    
    image3 = Image.open(path)
    pic3 = ImageTk.PhotoImage(image3)
    imageLabel=Label(bookMain)
    imageLabel.configure(image=pic3)
    imageLabel.grid(row=2, column=3,sticky=W,rowspan=10,padx=(100,0))

def getExistingBooksUsers(userType):
    global bookCol11
    global bookCol22
    global bookCol33
    
    try:
        bookCol11.destroy()
        bookCol22.destroy()
        bookCol33.destroy()
        
    except Exception as e:
        print(format(e))

    bookCol11=Frame(frame2)
   
    bookCol22=Frame(frame2)
   
    bookCol33=Frame(frame2)
    
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()

    if not str(searchEntryUsers.get()):
        sql="select * from books where usageAccountType = 'All' or usageAccountType = '"+userType+"'"
    else:
        sql= "select * from books where title like '%"+str(searchEntryUsers.get())+"%'"
      
    try:
        cursor.execute(sql)
        global image2
        global pic2
        results = cursor.fetchall()
        i=0
        length = len(results)
        for result in results:
            if i%3==0:
                global image2
                global pic2
                itemFrame = LabelFrame(bookCol11)
                itemFrame.pack()
                NameLabel = Label(itemFrame, text=result[1], font=("TIMES NEW ROMAN",12),wraplength=250)
                NameLabel.pack()
                path="images\\"+str(result[11])
                image2 = Image.open(path)
                
                pic2 = ImageTk.PhotoImage(image2)
                imageLabel21=Label(itemFrame)
                imageLabel21.configure(image=pic2)
                imageLabel21.image=pic2
                imageLabel21.pack()
               
                labelBookAuthor=Label(itemFrame,text=result[2],wraplength=250)
                labelBookAuthor.pack()
                
                NameLabel.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                imageLabel21.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                itemFrame.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                labelBookAuthor.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                
                itemFrame.pack()
                #itemFrame.grid(row=i//3+1,column=0)
                
            elif i%3==1:
                global image22
                global pic22
                itemFrame = LabelFrame(bookCol22)
                itemFrame.pack()
                NameLabel = Label(itemFrame, text=result[1], font=("TIMES NEW ROMAN",12),wraplength=250)
                NameLabel.pack()
                path="images\\"+str(result[11])
                image22 = Image.open(path)
                pic22 = ImageTk.PhotoImage(image22)
                imageLabel21=Label(itemFrame)
                imageLabel21.configure(image=pic22)
                imageLabel21.image=pic22
                imageLabel21.pack()
                labelBookAuthor=Label(itemFrame,text=result[2],wraplength=250)
                labelBookAuthor.pack()
                
                NameLabel.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                imageLabel21.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                itemFrame.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                labelBookAuthor.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                itemFrame.pack()
                #itemFrame.grid(row=i//3+1,column=0)
            else:
                global image23
                global pic23
                
                itemFrame = LabelFrame(bookCol33)
                itemFrame.pack()
                NameLabel = Label(itemFrame, text=result[1], font=("TIMES NEW ROMAN",12),wraplength=250)
                NameLabel.pack()
                path="images\\"+str(result[11])
                image23 = Image.open(path)
                pic23 = ImageTk.PhotoImage(image23)
                imageLabel21=Label(itemFrame)
                imageLabel21.configure(image=pic23)
                imageLabel21.image=pic23
                imageLabel21.pack()

                
                labelBookAuthor=Label(itemFrame,text=result[2],wraplength=250)
                labelBookAuthor.pack()
                
                NameLabel.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                imageLabel21.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                itemFrame.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                labelBookAuthor.bind("<Button-1>", lambda e,result=result:bookDetails(result))
                itemFrame.pack()
                #itemFrame.grid(row=i//3+1,column=0)
            i=i+1
        
        #bookCol11.place(x=100,y=100,width=300)
        #bookCol22.place(x=350,y=200,width=300)
        #bookCol33.place(x=650,y=300,width=300)
        #bookCol11.pack(side='left',padx=20)
        #bookCol22.pack(side='left',padx=20)
        #bookCol33.pack(side='left',padx=20)
        bookCol11.grid(row=3,column=0,padx=30,sticky=N)
        bookCol22.grid(row=3,column=1,padx=30,sticky=N)
        bookCol33.grid(row=3,column=2,padx=30,sticky=N)
       
    except Exception as e:
        print(format(e))
        
    db.close()



#login frame
lsmMain = LabelFrame(main)


def login():
    username = loginUserName.get()
    password = loginPassword.get()
    if username and password:
        db= pymysql.connect("localhost","root","","LibraryDB")
        cursor = db.cursor()
        sql="select * from users where username= '"+username+"'"
        
        try:
           cursor.execute(sql)
           
           global pass1
           pass1=0
           results = cursor.fetchall()
           for result in results:
               
               if result[2]== password:
                   if result[3]== "Library Staff Member":
                       lsmMain.pack(fill=BOTH ,expand=TRUE, side=LEFT)
                       lsmMain.lift()
                       root.pack_forget()
                   else:
                       ussMain.pack(fill=BOTH ,expand=TRUE, side=LEFT)
                       ussMain.lift()
                       getExistingBooksUsers(result[3])
                       root.pack_forget()
                   pass1=1
           if  len(result)==0:
               messagebox.showerror("Error","Invalid User Account")
               pass1==1
               
           if pass1==0:     
               messagebox.showerror("Error","Invalid Password")    
               
           
              
          
           
        except Exception as e:
            print(format(e))
            messagebox.showerror( title="Error", message="Invalid User Account")

        db.close()
    elif not username:
        messagebox.showerror( title="Error", message="User Name is Empty")
    elif not password:
        messagebox.showerror( title="Error", message="Password is Empty")

def loginClear():
    loginUserName.delete(0,END)
    loginPassword.delete(0,END)

    

Label(loginFrame,text="UserName",padx=10).grid(row=0,column=0,sticky=W,pady=10)
Label(loginFrame,text="Password",padx=10).grid(row=1,column=0,sticky=W,pady=(0,10))

emptyCol = Label(loginFrame,text ="  ").grid(row=0,column=1)


loginUserName = Entry(loginFrame,)
loginUserName.grid(row=0,column=2,pady=10)
loginPassword = Entry(loginFrame, show="**")
loginPassword.grid(row=1,column=2,pady=(0,10))

loginClearButton = Button(loginFrame, text = "Clear", command=loginClear).grid(row=2,column=0,sticky=W+E)
loginButton = Button(loginFrame, text="Login", command= login).grid(row=2,column=2,sticky=W+E)






#Signup Form

def signup():
    username = str(signupUserName.get())
    password = str(signupPassword.get())
    confirm = str(signupConfirmPassword.get())
    acType = str(accountTypeSignUp.get())
    if username and password and confirm and acType:
        if password == confirm:
            db= pymysql.connect("localhost","root","","LibraryDB")
            cursor = db.cursor()
            sql = "INSERT INTO users(username,password,accountType  ) VALUES ('"+username+"','"+password+"','"+acType+"' )"
            
            try:
               cursor.execute(sql)
               db.commit()
               signupClear()
            except Exception as e:
               db.rollback()
               print(format(e))
               messagebox.showerror( title="Error", message="Account not Added")

            db.close()
            loginUserName.delete(0,END)
            loginUserName.insert(0,username)
            loginPassword.delete(0,END)
            loginPassword.insert(0,password)
        else:
            messagebox.showerror( title="Error", message="Password Mismatch")
            signupPassword.delete(0,END)
            signupConfirmPassword.delete(0,END)
    elif not username:
        messagebox.showerror( title="Error", message="Username is Empty")
    elif not password:
        messagebox.showerror( title="Error", message="Password is Empty")
    elif not confirm:
        messagebox.showerror( title="Error", message="Password Confirmation is Empty")
            


def signupClear():
    signupUserName.delete(0,END)
    signupPassword.delete(0,END)
    signupConfirmPassword.delete(0,END)
    accountType.set("Student")

Label(signupFrame,text="UserName").grid(row=0,column=0,sticky=W,pady=10)
Label(signupFrame,text="Password").grid(row=1,column=0,sticky=W,pady=(0,10))
Label(signupFrame,text="Confirm-Password").grid(row=2,column=0,sticky=W,pady=(0,10))
Label(signupFrame,text="Account Type").grid(row=3,column=0, rowspan=3,sticky=W,pady=(0,10))

emptyCol = Label(signupFrame,text ="  ").grid(row=0,column=1,pady=(0,10))

signupUserName = Entry(signupFrame)
signupUserName.grid(row=0,column=2,pady=(0,10))
signupPassword = Entry(signupFrame, show="**")
signupPassword.grid(row=1,column=2,pady=(0,10))
signupConfirmPassword = Entry(signupFrame, show="**")
signupConfirmPassword.grid(row=2,column=2,pady=(0,10))

accountTypeSignUp = StringVar()
accountTypeSignUp.set("Student")

Radiobutton(signupFrame,text="Student",variable = accountTypeSignUp , value = "Student",anchor=W).grid(row = 3, column=2,sticky=W)
Radiobutton(signupFrame,text="Staff Member",variable = accountTypeSignUp , value = "Staff Member").grid(row = 4, column=2,sticky=W)
Radiobutton(signupFrame,text="Library Staff Member",variable = accountTypeSignUp , value = "Library Staff Member").grid(row = 5, column=2,sticky=W,pady=(0,10))


signupButton = Button(signupFrame, text="Signup", command= signup).grid(row=6, column=2, sticky=W+E,pady=(0,10))
signupClearButton = Button(signupFrame, text = "Clear", command=signupClear).grid(row=6, column=0, sticky=W+E,pady=(0,10))

#Library Staff Member

#lsmMain UI



bookAddUI = LabelFrame(main)

def newBook():
    
    bookAddUI.pack(fill=BOTH ,expand=TRUE)
    bookAddUI.lift()
    lsmMain.pack_forget()





#Book adding Frame


global fileName


def addBookClear():
    titleEntry.delete(0,END)
    authorEntry.delete(0,END)
    isbnEntry.delete(0,END)
    subjectEntry.delete(0,END)
    typeEntry.delete(0,END)
    numberCopiesEntry.delete(0,END)
    accountType.set("All")
    priceEntry.delete(0,END)
    publisherEntry.delete(0,END)
    noteEntry.delete(0,END)

    global imageLabel
    global image
    global pic
    image = Image.open(r"images\default.jpg")
    image = image.resize((250, 250), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    imageLabel=Label(bookAddUI,image=pic)
    imageLabel.grid(row=2,column=3,columnspan=2,rowspan=10)

def back():
    addBookClear()
    try:
        
        updateButton.destroy()
        deleteButton.destroy()
    except Exception as e:
        print(format(e))

    try:
        submitButton= Button(bookAddUI,text="Add New Book",command=submit)
        submitButton.grid(row=12, column=1, columnspan=4,sticky=W+E,pady=(20,0))
        #submitButton= Button(bookAddUI,text="Add New Book",command=submit)
        #submitButton.grid(row=12, column=1, columnspan=4,sticky=W+E,pady=(20,0))
    except Exception as e:
        print(format(e))

        
    booksUI.pack_forget()
    bookAddUI.pack_forget()
    usersUI.pack_forget()
    lsmMain.pack(fill=BOTH ,expand=TRUE, side=LEFT)
    

def image():
    global image
    global pic
    fileName = filedialog.askopenfilename(initialdir="/",title="Set Image", filetypes=(("jpg files","*jpg"),("png files","*.png"),("all files","*.*")))
    image = Image.open(fileName)
    image = image.resize((250, 250), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    imageLabel=Label(bookAddUI,image=pic)
    imageLabel.grid(row=2,column=3,columnspan=2,rowspan=10)
    
def submit():
    try:
        title= str(titleEntry.get())
        author= str(authorEntry.get())
        isbn= int(isbnEntry.get())
        subject= str(subjectEntry.get())
        btype= str(typeEntry.get())
        numberOfCopies= int(numberCopiesEntry.get())
        acType= str(accountType.get())
        price= int(priceEntry.get())
        publisher= str(publisherEntry.get())
        publishDate= str(publishDateEntry.get())
        note = str(noteEntry.get())
    except Exception as e:
        print(format(e))
        messagebox.showerror("Error","Check the Input Fields")
    

   
    if title and author and isbn and subject and btype and numberOfCopies and acType and price and publisher and publishDate and note:
        imageName= str(title+" "+str(isbn))+".jpg"
        image.save("Images\\"+imageName,format='jpeg')

        db= pymysql.connect("localhost","root","","LibraryDB")
        cursor = db.cursor()
        sql = "INSERT INTO books(title,author, isbn,subject,type,numberOfCopies,usageAccountType,price,publisher,pubDate,imageName, Note ) VALUES ('"+title+"','"+author+"','"+str(isbn)+"','"+subject+"','"+btype+"','"+str(numberOfCopies)+"','"+acType+"','"+str(price)+"','"+publisher+"','"+publishDate+"','"+ imageName+"','"+note+"')"
        
        try:
            cursor.execute(sql)
            db.commit()
            addBookClear()
        except Exception as e:
            print(format(e))
            db.rollback()
            messagebox.showerror("Error","Book not Added")

        db.close()
    else:
        messagebox.showerror("Error","Check the Input Fields")
 
        

        
        

Button(bookAddUI, text="Back",command = back).grid(row=0,column=0)
topicLabel = Label(bookAddUI, text="Add New Book", font=("TIMES NEW ROMAN",30)).grid(row=0,column=1,columnspan=10,sticky=W+E)

Label(bookAddUI,text="Title").grid(row=1, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Author").grid(row=2, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="ISBN").grid(row=3, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Subject").grid(row=4, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Type").grid(row=5, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Number of Copies").grid(row=6, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Usage Account Type").grid(row=7, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Price").grid(row=8, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Publisher").grid(row=9, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Publication Date").grid(row=10, column=0,sticky=W,padx=(100,30),pady=(20,0))
Label(bookAddUI,text="Image",width=20).grid(row=1, column=3,sticky=W,padx=(0,30),pady=(20,0))
Label(bookAddUI,text="Note").grid(row=11, column=0,sticky=W,padx=(100,30),pady=(20,0))
titleEntry=Entry(bookAddUI,width=40)
titleEntry.grid(row=1, column=1,sticky=W,pady=(20,0))
authorEntry=Entry(bookAddUI,width=40)
authorEntry.grid(row=2, column=1,sticky=W,pady=(20,0))
isbnEntry=Entry(bookAddUI,width=40)
isbnEntry.grid(row=3, column=1,sticky=W,pady=(20,0))
subjectEntry=Entry(bookAddUI,width=40)
subjectEntry.grid(row=4, column=1,sticky=W,pady=(20,0))
typeEntry=Entry(bookAddUI,width=40)
typeEntry.grid(row=5, column=1,sticky=W,pady=(20,0))
numberCopiesEntry=Entry(bookAddUI,width=40)
numberCopiesEntry.grid(row=6, column=1,sticky=W,pady=(20,0))


accountType=StringVar()
accountType.set("All")
accountTypeValues=[ "Student","Staff Member","All"]
accountTypeMenu = OptionMenu(bookAddUI, accountType,*accountTypeValues)
accountTypeMenu.config(width=30)
accountTypeMenu.grid(row=7,column=1,sticky=W+E,pady=(20,0))

priceEntry=Entry(bookAddUI,width=40)
priceEntry.grid(row=8, column=1,sticky=W,pady=(20,0))

publisherEntry=Entry(bookAddUI,width=40)
publisherEntry.grid(row=9, column=1,sticky=W,pady=(20,0))

publishDateEntry = DateEntry(bookAddUI, width=35)
publishDateEntry.grid(row=10,column=1,sticky=W+E,pady=(20,0))

imageOpenButton = Button(bookAddUI, text="Set Image", command=image,width=30)
imageOpenButton.grid(row=1, column=4,sticky=W+E,pady=(20,0))

image = Image.open(r"images\default.jpg")
image = image.resize((250, 250), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(image)
imageLabel=Label(bookAddUI,image=pic)
imageLabel.grid(row=1,column=3,columnspan=2,rowspan=10)

noteEntry=Entry(bookAddUI,width=40)
noteEntry.grid(row=11, column=1,sticky=W,pady=(20,0))

clearButton = Button(bookAddUI, text="Clear", command= addBookClear)
clearButton.grid(row=12, column=0,sticky=W+E,pady=(20,0),padx=(100,5))

submitButton= Button(bookAddUI,text="Add New Book",command=submit)
submitButton.grid(row=12, column=1, columnspan=4,sticky=W+E,pady=(20,0))


booksUI = LabelFrame(main)

def enter(event):
    canvas.bind_all("<MouseWheel>",mouse_wheel)
def leave(event):
    canvas.unbind_all("<MouseWheel>")

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=mainWidth-30,height=mainHeight-100)

def mouse_wheel(event):
    if event.num==5 or event.delta==-120:
        canvas.yview_scroll(1,"units" )
    if event.num==4 or event.delta ==120:
        canvas.yview_scroll(-1,"units" )
                        
myframe=Frame(booksUI,relief=GROOVE,width=mainWidth,height=mainHeight,bd=0)
myframe.place(x=0,y=90)

canvas=Canvas(myframe)



frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

canvas.bind('<Enter>', enter)
canvas.bind('<Leave>', leave)

def update(result):
    try:
        title= str(titleEntry.get())
        author= str(authorEntry.get())
        isbn= int(isbnEntry.get())
        subject= str(subjectEntry.get())
        btype= str(typeEntry.get())
        numberOfCopies= int(numberCopiesEntry.get())
        acType= str(accountType.get())
        price= int(priceEntry.get())
        publisher= str(publisherEntry.get())
        publishDate= str(publishDateEntry.get())
        note = str(noteEntry.get())
        if title and author and isbn and subject and btype and numberOfCopies and acType and price and publisher and publishDate and note:
            imageName= str(title+" "+str(isbn))+".jpg"
            image.save("Images\\"+imageName,format='jpeg')
        
            db= pymysql.connect("localhost","root","","LibraryDB")
            cursor = db.cursor()
            sql2="update books set  title ='"+title+"', author ='"+author+"' , isbn ='"+str(isbn)+"', subject ='"+subject+"', type ='"+btype+"', numberOfCopies ='"+str(numberOfCopies)+"' ,usageAccountType ='"+acType+"', price ='"+str(price)+"' , publisher ='"+publisher+"', pubdate ='"+str(publishDate)+"', imageName ='"+imageName+"',note='"+note+"' where id='"+str(result[0])+"'"

            try:
                cursor.execute(sql2)
                db.commit()
                addBookClear()
                back()
            except Exception as e:
                print(format(e))
                db.rollback()
                messagebox.showerror("Error","Book not Updated")

            db.close()
        else:
            messagebox.showerror("Error","Check the Input Fields")

    except Exception as e:
        print(format(e))
        messagebox.showerror("Error","Check the Input Fields")
    

   
   

def deleteBook(result):
    
    con = messagebox.askyesnocancel("CONFIRM","Do you want to delete this book?")
    if con:
        try:
            db= pymysql.connect("localhost","root","","libraryDB")
            cursor=db.cursor()
            sql3="delete from books where id = "+str(result[0])

            try:
                cursor.execute(sql3)
                db.commit()
                addBookClear()
            except Exception as e:
                print(format(e))
                db.rollback()
                messagebox.showerror("Error","Book not deleted")
        except Exception as e:
            print(format(e))
            messagebox.showerror("Error","Book not deleted")
    

def bookEdit(result):
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()
    sql="select * from books"
        
            
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        length = len(results)
        for AllResult in results:
            if result==AllResult:
                break

        
        titleEntry.insert(0,result[1])
        
        authorEntry.insert(0,result[2])
        
        isbnEntry.insert(0,result[3])
        
        subjectEntry.insert(0,result[4])
        
        typeEntry.insert(0,result[5])
        
        numberCopiesEntry.insert(0,result[6])

        
        accountType.set(result[7])
    
        priceEntry.insert(0,result[8])

        
        publisherEntry.insert(0,result[9])

        publishDateEntry.delete(0,END)
        publishDateEntry.insert(0,result[10])

        noteEntry.insert(0,result[12])

        global image
        global pic
        image = Image.open(r"images\\"+result[11])
        image = image.resize((250, 250), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(image)
        imageLabel=Label(bookAddUI,image=pic)
        imageLabel.grid(row=2,column=3,columnspan=2,rowspan=10)

        bookAddUI.pack(fill=BOTH ,expand=TRUE)
        bookAddUI.lift()
        booksUI.pack_forget()

        submitButton.destroy()
        updateButton= Button(bookAddUI,text="Update",command=lambda:update(result))
        updateButton.grid(row=12, column=1, columnspan=3,sticky=W+E,pady=(20,0))
        deleteButton= Button(bookAddUI, text="Delete",command=lambda:deleteBook(result))
        deleteButton.grid(row=12, column=4,sticky=W+E,pady=(20,0),padx=(5,0))
           
    except Exception as e:
        print(format(e))
        
    db.close()
    

def getExistingBooks():
    global bookCol1
    global bookCol2
    global bookCol3
    
    try:
        bookCol1.destroy()
        bookCol2.destroy()
        bookCol3.destroy()
        
    except Exception as e:
        print(format(e))

    bookCol1=Frame(frame)
   
    bookCol2=Frame(frame)
   
    bookCol3=Frame(frame)
    
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()

    if not str(searchEntry.get()):
        sql="select * from books"
    else:
        sql= "select * from books where title like '%"+str(searchEntry.get())+"%'"
      
    try:
        cursor.execute(sql)
        global image2
        global pic2
        results = cursor.fetchall()
        i=0
        length = len(results)
        for result in results:
            if i%3==0:
                global image2
                global pic2
                itemFrame = LabelFrame(bookCol1)
                itemFrame.pack()
                NameLabel = Label(itemFrame, text=result[1], font=("TIMES NEW ROMAN",12),wraplength=250)
                NameLabel.pack()
                path="images\\"+str(result[11])
                image2 = Image.open(path)
                
                pic2 = ImageTk.PhotoImage(image2)
                imageLabel21=Label(itemFrame)
                imageLabel21.configure(image=pic2)
                imageLabel21.image=pic2
                imageLabel21.pack()
               
                labelBookAuthor=Label(itemFrame,text=result[2],wraplength=250)
                labelBookAuthor.pack()
                
                NameLabel.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                imageLabel21.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                itemFrame.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                labelBookAuthor.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                
                itemFrame.pack()
                #itemFrame.grid(row=i//3+1,column=0)
                
            elif i%3==1:
                global image22
                global pic22
                itemFrame = LabelFrame(bookCol2)
                itemFrame.pack()
                NameLabel = Label(itemFrame, text=result[1], font=("TIMES NEW ROMAN",12),wraplength=250)
                NameLabel.pack()
                path="images\\"+str(result[11])
                image22 = Image.open(path)
                pic22 = ImageTk.PhotoImage(image22)
                imageLabel21=Label(itemFrame)
                imageLabel21.configure(image=pic22)
                imageLabel21.image=pic22
                imageLabel21.pack()
                labelBookAuthor=Label(itemFrame,text=result[2],wraplength=250)
                labelBookAuthor.pack()
                
                NameLabel.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                imageLabel21.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                itemFrame.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                labelBookAuthor.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                itemFrame.pack()
                #itemFrame.grid(row=i//3+1,column=0)
            else:
                global image23
                global pic23
                
                itemFrame = LabelFrame(bookCol3)
                itemFrame.pack()
                NameLabel = Label(itemFrame, text=result[1], font=("TIMES NEW ROMAN",12),wraplength=250)
                NameLabel.pack()
                path="images\\"+str(result[11])
                image23 = Image.open(path)
                pic23 = ImageTk.PhotoImage(image23)
                imageLabel21=Label(itemFrame)
                imageLabel21.configure(image=pic23)
                imageLabel21.image=pic23
                imageLabel21.pack()

                
                labelBookAuthor=Label(itemFrame,text=result[2],wraplength=250)
                labelBookAuthor.pack()
                
                NameLabel.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                imageLabel21.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                itemFrame.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                labelBookAuthor.bind("<Button-1>", lambda e,result=result:bookEdit(result))
                itemFrame.pack()
                #itemFrame.grid(row=i//3+1,column=0)
            i=i+1
        #bookCol1.pack(side="left")
        #bookCol2.pack(side="left")
        #bookCol3.pack(side="left")
        bookCol1.grid(row=3,column=0,padx=30,sticky=N)
        bookCol2.grid(row=3,column=1,padx=30,sticky=N)
        bookCol3.grid(row=3,column=2,padx=30,sticky=N)
       
    except Exception as e:
        print(format(e))
        
    db.close()

def searchBook():
    getExistingBooks()
    searchEntry.delete(0,END)
def searchBook1(event):
    getExistingBooks()
    searchEntry.delete(0,END)

#books UI LMS
Button(booksUI, text="Back",command = back).place(x=50, y=30)
searchEntry = Entry(booksUI)
topicLabel = Label(booksUI, text="Existing Books", font=("TIMES NEW ROMAN",30)).place(x=375, y=10)
searchEntry = Entry(booksUI)
searchEntry.place( x=325, y=60,width=300)
searchButton = Button(booksUI, text="Search", width=10,command=searchBook)
searchEntry.bind('<Return>',searchBook1)
searchButton.place(x=645, y=57)






def existingBooks():
    booksUI.pack(fill='both',expand='yes')
    booksUI.lift()
    getExistingBooks()
    lsmMain.pack_forget()

usersUI = LabelFrame(main)

def enter1(event):
    canvas1.bind_all("<MouseWheel>",mouse_wheel1)
def leave1(event):
    canvas1.unbind_all("<MouseWheel>")

def myfunction1(event):
    canvas1.configure(scrollregion=canvas1.bbox("all"),width=mainWidth-30,height=mainHeight-100)

def mouse_wheel1(event):
    if event.num==5 or event.delta==-120:
        canvas1.yview_scroll(1,"units" )
    if event.num==4 or event.delta ==120:
        canvas1.yview_scroll(-1,"units" )
                        
myframe1=Frame(usersUI,relief=GROOVE,width=mainWidth,height=mainHeight,bd=0)
myframe1.place(x=0,y=90)

canvas1=Canvas(myframe1)



frame1=Frame(canvas1)
myscrollbar1=Scrollbar(myframe1,orient="vertical",command=canvas1.yview)
canvas1.configure(yscrollcommand=myscrollbar1.set)

myscrollbar1.pack(side="right",fill="y")
canvas1.pack(side="left")
canvas1.create_window((0,0),window=frame1,anchor='nw')
frame1.bind("<Configure>",myfunction1)

canvas1.bind('<Enter>', enter1)
canvas1.bind('<Leave>', leave1)

global searchUsersEntry

def getExistingUsersList():
    global frameCol1
    global frameCol2
    global frameCol3
    
    try:
        frameCol1.destroy()
        frameCol2.destroy()
        frameCol3.destroy()
        
    except Exception as e:
        print(format(e))

    frameCol1=Frame(frame1)
    Label(frameCol1, text="ID", font=("TIMES NEW ROMAN",12)).grid(row=0,column=0)
    Label(frameCol1, text="User Name", font=("TIMES NEW ROMAN",12)).grid(row=0,column=1)
    Label(frameCol1, text="Action", font=("TIMES NEW ROMAN",12)).grid(row=0,column=2,columnspan=2)
   
    frameCol2=Frame(frame1)
    Label(frameCol2, text="ID", font=("TIMES NEW ROMAN",12)).grid(row=0,column=0)
    Label(frameCol2, text="User Name", font=("TIMES NEW ROMAN",12)).grid(row=0,column=1)
    Label(frameCol2, text="Action", font=("TIMES NEW ROMAN",12)).grid(row=0,column=2,columnspan=2)
    
    frameCol3=Frame(frame1)
    Label(frameCol3, text="ID", font=("TIMES NEW ROMAN",12)).grid(row=0,column=0)
    Label(frameCol3, text="User Name", font=("TIMES NEW ROMAN",12)).grid(row=0,column=1)
    Label(frameCol3, text="Action", font=("TIMES NEW ROMAN",12)).grid(row=0,column=2,columnspan=2)
        
    db= pymysql.connect("localhost","root","","LibraryDB")
    cursor = db.cursor()

    
    if not str(searchUsersEntry.get()):
        sql="select * from users"
    else:
        sql="select * from users where username like '%"+str(searchUsersEntry.get())+"%'"
        
            
    try:
        cursor.execute(sql)
               
        results = cursor.fetchall()
        i=0
        length = len(results)
        for result in results:
            if i%3==0:
                
                labelID=Label(frameCol1,text=result[0])
                labelName = Label(frameCol1,text=result[1],wraplength=250)
                labelPassword = Label(frameCol1, text="Change",fg="blue")
                labelDelete = Label(frameCol1, text="Delete",fg="red")
                labelPassword.bind("<Button-1>", lambda e,result=result:click(result))
                labelDelete.bind("<Button-1>", lambda e,result=result:delete(result))
                labelID.grid(row=i//3+1,column=0)
                labelName.grid(row=i//3+1,column=1)
                labelPassword.grid(row=i//3+1,column=2)
                labelDelete.grid(row=i//3+1,column=3)
            elif i%3==1:
                labelID=Label(frameCol2,text=result[0])
                labelName = Label(frameCol2,text=result[1],wraplength=250)
                labelPassword = Label(frameCol2, text="Change",fg="blue")
                labelDelete = Label(frameCol2, text="Delete",fg="red")
                labelPassword.bind("<Button-1>", lambda e,result=result:click(result))
                labelDelete.bind("<Button-1>", lambda e,result=result:delete(result))
                labelID.grid(row=i//3+1,column=0)
                labelName.grid(row=i//3+1,column=1)
                labelPassword.grid(row=i//3+1,column=2)
                labelDelete.grid(row=i//3+1,column=3)
            else:
                labelID=Label(frameCol3,text=result[0])
                labelName = Label(frameCol3,text=result[1],wraplength=250)
                labelPassword = Label(frameCol3, text="Change",fg="blue")
                labelDelete = Label(frameCol3, text="Delete",fg="red")
                labelPassword.bind("<Button-1>", lambda e,result=result:click(result))
                labelDelete.bind("<Button-1>", lambda e,result=result:delete(result))
                labelID.grid(row=i//3+1,column=0)
                labelName.grid(row=i//3+1,column=1)
                labelPassword.grid(row=i//3+1,column=2)
                labelDelete.grid(row=i//3+1,column=3)
            i=i+1
        frameCol1.grid(row=3,column=0,padx=60,sticky=N)
        frameCol2.grid(row=3,column=1,padx=60,sticky=N)
        frameCol3.grid(row=3,column=2,padx=60,sticky=N)
    except Exception as e:
        print(format(e))
        print("error")

    db.close()

def users():
    usersUI.pack(fill=BOTH ,expand=TRUE)
    usersUI.lift()
    getExistingUsersList()
    lsmMain.pack_forget()


addNewBookButton = Button(lsmMain, text="Add New Book",font=('ubuntu mono',10),width=35,height=15, command=newBook)
existingBooksButton = Button(lsmMain, text="Existing Books",font=('ubuntu mono',10),width=35,height=15, command=existingBooks)
existingUsersButton = Button(lsmMain, text="Users",width=35,font=('ubuntu mono',10),height=15, command = users)

addNewBookButton.place(x=120,rely=0.3)
existingBooksButton.place(x=385,rely=0.3)
existingUsersButton.place(x=650,rely=0.3)





#Existing Users Info LSM Panel

Button(usersUI, text="Back",command = back).place(x=50, y=30)
topicLabel = Label(usersUI, text="Existing Users", font=("TIMES NEW ROMAN",30)). place(x=375, y=10)

def searchUser():
    getExistingUsersList()
    searchUsersEntry.delete(0,END)
def searchUser1(event):
    getExistingUsersList()
    searchUsersEntry.delete(0,END)

searchUsersEntry = Entry(usersUI)
searchUsersEntry.place( x=325, y=60,width=300)
searchUsersButton = Button(usersUI, text="Search", width=10,command=searchUser)
searchUsersEntry.bind('<Return>',searchUser1)
searchUsersButton.place(x=645, y=57)



def click(result):
    global passwordChange
    passwordChange = Toplevel()
    passwordChange.title("Chnage Password")
    passwordChange.geometry("250x100")
    passwordChange.resizable(0,0)

    welcome = Label(passwordChange,text="Change Password of "+result[1],font=('TIMES NEW ROMAN',15)).grid(row=0,column=0,columnspan=2)
    labelChange = Label(passwordChange,text="New Password").grid(row=1,column=0,sticky=W)
    labelConfirm = Label(passwordChange,text="Confirm Password").grid(row=2,column=0,sticky=W)

    global passwordEntry
    global confirmPassword

    passwordEntry = Entry(passwordChange,show="*")
    passwordEntry.grid(row=1,column=1,sticky=W+E)
    confirmPassword = Entry(passwordChange,show="*")
    confirmPassword.grid(row=2,column=1,sticky=W+E)

    buttonConfrim = Button(passwordChange,text="Confirm",command=lambda:changePassword(result)).grid(row=3,column=1,sticky=W+E)
    buttonCancel = Button(passwordChange,text="Cancel",command=passwordChange.destroy).grid(row=3,column=0,sticky=W+E)

def changePassword(result):
    password = passwordEntry.get()
    confirm =confirmPassword.get()
    if password and confirm:
        if password==confirm:
            
            db= pymysql.connect("localhost","root","","LibraryDB")
            cursor = db.cursor()
            sql2="update users set password='"+password+"' where id='"+str(result[0])+"'"

            try:
                cursor.execute(sql2)
                db.commit()
            except Exception as e:
                print(format(e))
                messagebox.showerror("Error","Password Not Changed")
                db.rollback()
            passwordChange.destroy()
            db.close()
        else:
            passwordChange.destroy()
            messagebox.showerror("ERROR","Password Mismatch")
            
    else:
        passwordChange.destroy()
        messagebox.showerror("ERROR","Empty Fields")

def delete(result):
    deleteConfirm = messagebox.askyesno("Confirm","Do you want to delete UserAccount ?")
    if deleteConfirm:
        try:
            db= pymysql.connect("localhost","root","","LibraryDB")
            cursor = db.cursor()
            sql="delete from users where id="+str(result[0])
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(format(e))
            db.rollback()
            messagebox.showerror("Error","User Account not Deleted")
        db.close()
    getExistingUsersList()  


#users and Staff UI



def searchBookUsers():
    getExistingBooksUsers()
    searchEntryUsers.delete(0,END)
def searchBook1Users(event):
    getExistingBooksUsers()
    searchEntryUsers.delete(0,END)


Label(ussMain, text="Books", font=("TIMES NEW ROMAN",30)).place(x=450, y=10)
#Label(ussMain, text="Books", font=("TIMES NEW ROMAN",30)).pack()
searchEntryUsers = Entry(ussMain)
searchEntryUsers.place( x=325, y=60,width=300)
#searchEntryUsers.pack()
searchButtonUsers = Button(ussMain, text="Search", width=10,command=searchBookUsers)
searchEntryUsers.bind('<Return>',searchBook1Users)
searchButtonUsers.place(x=645, y=57)
#searchButtonUsers.pack()

def backtobooks():
    bookDetailsLabel1.grid_forget()
    bookDetailsLabel2.grid_forget()
    bookDetailsLabel3.grid_forget()
    bookDetailsLabel4.grid_forget()
    bookDetailsLabel5.grid_forget()
    bookDetailsLabel6.grid_forget()
    bookDetailsLabel7.grid_forget()
    bookDetailsLabel8.grid_forget()
    bookDetailsLabel9.grid_forget()
    bookDetailsLabel10.grid_forget()
    bookDetailsLabel11.grid_forget()
    bookMain.pack_forget()
    ussMain.lift()
    ussMain.pack(fill='both', expand='yes', side='left')
    


Label(bookMain, text="Details", font=("TIMES NEW ROMAN",30)).grid(row=0, column=1)
Button(bookMain, text="Back", command=backtobooks).grid(row=0,column=0)
Label(bookMain,text="Title")                .grid(row=1, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Author")               .grid(row=2, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="ISBN")                 .grid(row=3, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Subject")              .grid(row=4, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Type")                 .grid(row=5, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Number of Copies")     .grid(row=6, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Usage Account Type")   .grid(row=7, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Price")                .grid(row=8, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Publisher")            .grid(row=9, column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Publication Date")     .grid(row=10,column=0,sticky=W,padx=(100,30),pady=(10,0))
Label(bookMain,text="Image",width=20)       .grid(row=1, column=3,sticky=W,padx=(100,30),pady=(10,0))
noteFrame = LabelFrame(bookMain,text="Note",font=('Ubuntu mono',20))
noteFrame.grid(row=12,column=0,sticky=N+E+S+W,padx=100,columnspan=10,pady=(10,0))





main.mainloop()
