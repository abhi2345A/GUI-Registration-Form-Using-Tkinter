from tkinter import *
import datetime
from tkinter import messagebox
import re
from validate_email import validate_email


root = Tk()

class Registration_Form:
    _params = []    # Protected Member can be accessed  within class or subclass
    # Private Members of the class
    __entry_1 = Entry()
    __entry_2 = Entry()
    __entry_3 = Entry()
    __ck = StringVar()
    __c2 = StringVar()
    __c3 = StringVar()
    __c4 = StringVar()
    __entry_4b = Entry()
    __var = IntVar()
    __entry_7 = Entry()
    __entry_8 = Entry()
    # ----------------------------
    def __init__(self):
        self._params = ['Himesh','Singh','example@example.com','+91','12121','Male','12345','12345'
                        ,'1996-12-12','1996','12','12']

    def __del__(self):
        self._params = []

    def special_match(self,strg, search=re.compile(r'[^a-zA-Z.]').search):

        return not bool(search(strg))

    def num_match(self,strg, search=re.compile(r'[^0-9.]').search):

        return not bool(search(strg))

    def mainget(self):

        fname =  self.__entry_1.get()
        lname =  self.__entry_2.get()
        mail  =  self.__entry_3.get()
        code  =  self.__ck.get()
        YeaR  =  self.__c2.get()
        MontH =  self.__c3.get()
        DatE  =  self.__c4.get()
        mob   =  self.__entry_4b.get()
        GendR =  self.__var.get()
        Pass  =  self.__entry_7.get()
        Conf_Pass=self.__entry_8.get()

        if GendR==1:
            GendR='Male'
        else:
            GendR='Female'

        date_format = '%Y-%m-%d'
        flag=0
        try:
            date_string = YeaR + '-' + MontH + '-' + DatE
            datetime.datetime.strptime(date_string, date_format)
        except ValueError:
            flag=1

        if self.special_match(fname)==False or self.special_match(lname)==False:
            messagebox.showinfo("Error!", "First name and last name should only have Characters")
        elif validate_email(mail)==False:
            messagebox.showinfo("Error!", "Please enter valid email(e.g.example@example.com)")
        elif self.num_match(mob)==False:
            messagebox.showinfo("Error!", "Mobile should contain only numbers")
        elif len(Pass)<8:
            messagebox.showinfo("Error!", "Password Must be atleast 8 characters long")
        elif(Pass!=Conf_Pass):
            messagebox.showinfo("Error!", "Password and Confirm-Password Field didn't match")
        elif flag==1:
            messagebox.showinfo("Error!", "Please select a valid date of birth")
        else:
            ch = messagebox.askyesno("Submit", "Do you Want to Submit?")
            if ch==True:
                root.destroy()

        self._params = [fname,lname,mail,code,mob,GendR,Pass, Conf_Pass,date_string,YeaR,MontH,DatE]
        self._params = self._params[:-3]


    def layout(self):

        root.title('Registration Form')
        self.pic = PhotoImage(file="background.png")
        ba__ckground_label = Label(image=self.pic)
        ba__ckground_label.pack()
        ba__ckground_label.place(x=0, y=0, relwidth=1, relheight=1)
        ba__ckground_label.image = self.pic
        canvas = Canvas(root,width=720,height=800,bg="grey")
        box=canvas.create_rectangle(700,720,20,20,fill="snow3")
        canvas.pack(expand=YES)
        label=Label(canvas,text="Registration Form",font=("Times",30,"bold"),fg="brown4",bg="snow3",)
        label.place(x=200,y=30)
        label1=Label(canvas,text="First Name",font=("Times",14),fg="black",bg="snow3",)
        label1.place(x=60,y=150)
        self.__entry_1= Entry(canvas,bg="white",bd=4)
        self.__entry_1.place(x=180,y=150)
        label2=Label(canvas,text="Last Name",font=("Times",14),fg="black",bg="snow3",)
        label2.place(x=350,y=150)
        self.__entry_2= Entry(canvas,bg="white",bd=4)
        self.__entry_2.place(x=470,y=150)
        label3=Label(canvas,text="Email ",font=("Times",14),fg="black",bg="snow3",)
        label3.place(x=60,y=220)
        self.__entry_3= Entry(canvas,bg="white",width=50,bd=4)
        self.__entry_3.place(x=180,y=220)
        label4=Label(canvas,text="Mobile",font=("Times",14),fg="black",bg="snow3")
        label4.place(x=60,y=290)

        list1 = ['+91','+54','+880','+32','+1','+20','+49','+972','+39','+977','+7','+44','+380'];

        droplist=OptionMenu(canvas,self.__ck,*list1)
        self.__ck.set('+91')
        droplist.place(x=180,y=290)
        self.__entry_4b= Entry(canvas,bg="white",width=39,bd=4)
        self.__entry_4b.place(x=260,y=290)
        label_5 = Label(canvas, text="Gender",font=("Times", 14),fg="black",bg="snow3")
        label_5.place(x=60,y=360)

        Radiobutton(canvas, text="Male",padx = 10, variable=self.__var, value=1,bg="snow3").place(x=180,y=360)
        Radiobutton(canvas, text="Female",padx = 20, variable=self.__var, value=2,bg="snow3").place(x=250,y=360)

        label6=Label(canvas,text="Date of Birth",font=("Times",14),fg="black",bg="snow3")
        label6.place(x=60,y=430)

        list2 = []
        for i in range(1980,2017):
            list2.append('{}'.format(i))

        droplist2=OptionMenu(canvas,self.__c2,*list2)
        self.__c2.set("Year")
        droplist2.place(x=400,y=430)

        list3 = []
        for i in range(1,13):
            list3.append('{}'.format(i))

        droplist3=OptionMenu(canvas,self.__c3,*list3)
        self.__c3.set("Month")
        droplist3.place(x=300,y=430)

        list4 = []
        for i in range(1,32):
            list4.append('{}'.format(i))

        droplist4=OptionMenu(canvas,self.__c4,*list4)
        self.__c4.set("Date")
        droplist4.place(x=200,y=430)

        label7=Label(canvas,text="Password",font=("Times",14),fg="black",bg="snow3",)
        label7.place(x=60,y=500)
        self.__entry_7= Entry(canvas,bg="white",width=50,show="*",bd=4)
        self.__entry_7.place(x=180,y=500)
        label8=Label(canvas,text="Password Must be atleast 8 characters long",font=("Times",7),fg="black",bg="snow3",)
        label8.place(x=180,y=530)

        label8=Label(canvas,text="Confirm",font=("Times",14),fg="black",bg="snow3",)
        label8.place(x=60,y=560)
        label9=Label(canvas,text="Password",font=("Times",14),fg="black",bg="snow3",)
        label9.place(x=60,y=590)
        self.__entry_8= Entry(canvas,bg="white",width=50,show="*",bd=4)
        self.__entry_8.place(x=180,y=570)
        w = Button(canvas,text="Submit",width=20,height=2,bd=4,font=("Times",10,"bold"),bg="brown",command=self.mainget)
        w.place(x=270,y=640)

class Store_data(Registration_Form): # Derived class of Super class Registration_Form (Inheritance)
    def __init__(self,sheet):
        Registration_Form.__init__(self)
        self.sheet = sheet

    def __del__(self):
        Registration_Form.__del__(self)

    def excel(self):
        # resize the width of columns in
        # excel spreadsheet
        self.sheet.column_dimensions['A'].width = 20
        self.sheet.column_dimensions['B'].width = 20
        self.sheet.column_dimensions['C'].width = 30
        self.sheet.column_dimensions['D'].width = 20
        self.sheet.column_dimensions['E'].width = 10
        self.sheet.column_dimensions['F'].width = 30
        self.sheet.column_dimensions['G'].width = 30

        # write given data to an excel spreadsheet
        # at particular location
        self.sheet.cell(row=1, column=1).value = "First Name"
        self.sheet.cell(row=1, column=2).value = "Last Name"
        self.sheet.cell(row=1, column=3).value = "Email"
        self.sheet.cell(row=1, column=4).value = "Mobile Number"
        self.sheet.cell(row=1, column=5).value = "Gender"
        self.sheet.cell(row=1, column=6).value = "Date of Birth"
        self.sheet.cell(row=1, column=7).value = "Password"



    def insert(self):

        current_row = self.sheet.max_row
        current_column = self.sheet.max_column
        self.sheet.cell(row=current_row + 1, column=1).value = self._params[0]
        self.sheet.cell(row=current_row + 1, column=2).value = self._params[1]
        self.sheet.cell(row=current_row + 1, column=3).value = self._params[2]
        self.sheet.cell(row=current_row + 1, column=4).value = self._params[3]+self._params[4]
        self.sheet.cell(row=current_row + 1, column=5).value = self._params[5]
        self.sheet.cell(row=current_row + 1, column=6).value = self._params[8]
        self.sheet.cell(row=current_row + 1, column=7).value = self._params[7]




