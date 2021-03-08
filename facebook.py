#importing all the required packages
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk


#programming User Interface

class Facebook:
    def __init__(self, app):
        self.app = app
        self.app.title('Facebook Module')
        self.app.geometry('1350x700+0+0')
        self.app.config( bg='white')

        #Backgound Image
        self.bg = ImageTk.PhotoImage(file = 'images/cayene.jpg')
        bg = Label(self.app, image = self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #side image configurations
        self.left = ImageTk.PhotoImage(file = 'images/facebook.webp')
        left = Label(self.app, image = self.left).place(x=80, y=100, width=400, height=500)

        #Configuring A frame container
        self.frame = ImageTk.PhotoImage(file = 'images/facebook.webp')
        frame = Label(self.app, image=self.frame).place(x=480, y=100, width=700, height=500)


        frame1 = Frame(self.app, bg='white')
        frame1.place(x=480, y=100, width=700, height=500)
        title = Label(frame1, text='ANALYSIS RESULTS', font=('times new roman', 20, 'bold'),bg='white', fg='green').place(x=50, y=30)
        
        f_name = Label(frame1, text='First Name', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_fname.place(x=50, y=130, width='250', height='30')
        l_name = Label(frame1, text='Last Name', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_lname.place(x=370, y=130, width='250', height='30')

        #--------------
        parts_list = Listbox(frame1, height=8, width=50, border=0, background='gray')
        parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

        contact = Label(frame1, text='Contact', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_contact.place(x=50, y=200, width='250', height='30')
        email = Label(frame1, text='Email', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=370, y=170)
        self.txt_email = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_email.place(x=370, y=200, width='250', height='30')
        #--------------
        question = Label(frame1, text='Sequrity Question', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=('times new roman', 13),state='readony', justify='center')
        self.cmb_quest['values']=('Select','Your First Pet Name','Your Birth Place', 'Your Best Friend Name')
        self.cmb_quest.place(x=50, y=270, width='250', height='30')
        self.cmb_quest.current(0)

        answer = Label(frame1, text='Answer', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_answer.place(x=370, y=270, width='250', height='30')
        #--------------
        password = Label(frame1, text='Password', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=50, y=310)
        self.txt_password = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_password.place(x=50, y=340, width='250', height='30')
        cpassword = Label(frame1, text='Confirm Password', font=('times new roman', 15, 'bold'),bg='white', fg='gray').place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=('times new roman', 15), bg='lightgray', bd=0)
        self.txt_cpassword.place(x=370, y=340, width='250', height='30')

        #------------ Terms
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text = 'I Agree To Terms & Conditions', onvalue=1, offvalue=0, bg='white', fg='blue', variable=self.var_chk, font=('times new roman', 12)).place(x=50, y=380)

        self.btn_img = ImageTk.PhotoImage(file='images/reg2.png')
        btn_register = Button(frame1, image=self.btn_img, bg='white', bd=0, cursor='hand2', command = self.register_data).place(x=50, y=420)

        


    def register_data(self):
        pass
      

app = Tk()
obj = Facebook(app)
app.mainloop()