from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
import tempfile
import os
import tkinter.messagebox
from time import strftime
import mysql.connector as mysql
from tkcalendar import DateEntry
from datetime import datetime
from reportlab.pdfgen import canvas
import assets


global operator
operator = " "
choice = StringVar


splash=Tk()
splash.geometry('1350x750')
splash.title('WiRi RETAIL SYSTEMS v1.00')
splash.iconbitmap(r'assets/titlelogo.ico')
splash.resizable(1, 1)
splash.configure(background='cadetblue')

imglogo = ImageTk.PhotoImage(Image.open('assets/createlogosmall.png'))
logo_label = Label(splash, image=imglogo,bg='cadetblue')
logo_label.place(x=350, y=200)

will = open("wilson.txt", "r")
host_address = will.read()

con = mysql.connect(host=host_address, user='root', password='', database='retail-system2')
cursor = con.cursor()

cursor.execute("select * from server_info")
currency = cursor.fetchall()
main_currency = str(currency[0][2])

cursor.execute("select tender_name from tender_type")
tenders = cursor.fetchall()



l1=Label(splash,text="WiRi",font=("Garamond",50,"bold"),bg="cadetblue")
l1.place(x=500,y=275)

l2=Label(splash,text="RETAIL SYSTEMS",font=("Garamond",25,"bold"),bg="cadetblue")
l2.place(x=680,y=320)

l3=Label(splash,text="V1.00",font=("Garamond",12),bg="cadetblue")
l3.place(x=970,y=335)

l4=Label(splash,text="Loading...",font=("Garamond",12,"bold"),bg="cadetblue")
#l4.place(x=400,y=320)


progress=Progressbar(splash,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=700,mode="determinate")

def bar(*args):
    l4=Label(splash,text="Loading...please wait",fg="white",bg="cadetblue")
    lst34=("Calibri (Body)",10)
    l4.configure(font=lst34)
    l4.place(x=350,y=355)



    import time
    r=0
    for i in range(100):
        progress["value"]=r
        splash.update_idletasks()
        time.sleep(0.10)
        r=r+1

    splash.destroy()
    main_win()

progress.place(x=300,y=380)

bt=Button(splash,width=10,text="Proceed>>",command=bar,border=0,fg="black",bg="cadetblue")
bt.place(x=590,y=430)






def main_win():
    global imglogo1
    q = Tk()
    q.geometry('1350x750')
    q.title('WiRi RETAIL SYSTEMS v1.00')
    q.iconbitmap(r'assets/titlelogo.ico')
    q.resizable(0, 0)

    def loginwindow():
        global imglogo2, imglogo3,usernameEn
        w = Frame(q, width=1350, height=750, bg='cadet blue')
        w.place(x=0, y=0)

        imglogo3 = ImageTk.PhotoImage(Image.open('assets/createlogosmall.png'))
        logo_label2 = Label(w, image=imglogo3, bg='cadetblue')
        logo_label2.place(x=140, y=540)

        tf = Frame(w, width=900, height=750)
        tf.place(x=450, y=0)


        # Frame for login form
        lg = Frame(w, width=450, height=500, bg='white')
        lg.place(x=0, y=0)


        imglogo2 = ImageTk.PhotoImage(Image.open('assets/user-employee.png'))
        logo_label1 = Label(lg, image=imglogo2)
        logo_label1.place(x=110, y=8)

        usernamelbl = Label(lg, text='Username', bg='white',
                            font=("consolas", 13, 'bold'), padx=10).place(x=2, y=270)

        usernameEn = Entry(lg, width=40, fg="black", bg="white", bd=0, font=('consolas', 13))
        usernameEn.place(x=150, y=270)


        passwordlbl = Label(lg, text='Password', bg='white',
                            font=("consolas", 13, 'bold'), padx=10).place(x=2, y=350)

        passwordEn = Entry(lg, width=40, fg="black", bg="white", bd=0, font=('consolas', 13, 'bold'), show='*')
        passwordEn.place(x=150, y=350)

        usernameframe = Frame(lg, width=250, height=1, bg='black').place(x=150, y=290)
        passwordframe = Frame(lg, width=250, height=1, bg='black').place(x=150, y=370)

        def login(*args):
            if usernameEn.get() == "" or passwordEn.get() == "":
                messagebox.showerror("Login Status", "   Please Enter Username and Password   ")

            else:
                try:

                    des = "admin"
                    con = mysql.connect(host=host_address, user='root', password='', database='retail-system2')
                    cur = con.cursor()
                    cur.execute('select * from employee where name=%s and password=%s and designation=%s',
                                (usernameEn.get(), passwordEn.get(), des))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror('Error', '    Invalid  Username or Password')
                        usernameEn.delete(0, 'end')
                        passwordEn.delete(0, 'end')

                    else:
                        passwordEn.delete(0, 'end')
                        q.withdraw()
                        admin = Toplevel()
                        admin.geometry('1350x750')
                        admin.title('WiRi RETAIL SYSTEMS v1.00')
                        admin.iconbitmap(r'assets/titlelogo.ico')
                        admin.resizable(0, 0)

                        con = mysql.connect(host='localhost', user='root', password="",
                                            database="retail-system2")
                        cursor = con.cursor()
                        cursor.execute(
                            "SELECT employee_id FROM employee WHERE name like'%"+usernameEn.get()+"%'")
                        employee_id = cursor.fetchone()




                        def logout(*args):

                            try:

                                logoutwin = Tk()
                                logoutwin.geometry('450x400+440+150')
                                logoutwin.iconbitmap(r'assets/titlelogo.ico')
                                logoutwin.resizable(0, 0)
                                logoutwin.overrideredirect(1)
                                logoutwin.configure(background="cadetblue")

                                def yes():
                                    logoutwin.destroy()
                                    admin.destroy()
                                    q.deiconify()

                                def no():
                                    logoutwin.destroy()

                                trade_label = Label(logoutwin, text="WiRi Retail***", font=("cansalas", 14),
                                                    bg="cadetblue")
                                trade_label.place(x=5, y=10)

                                warn_label = Label(logoutwin, text="ARE YOU SURE YOU WOULD LIKE TO",
                                                   font=("georgia", 15, "bold"), bg="cadetblue")
                                warn_label.place(x=5, y=70)

                                warn_label = Label(logoutwin, text="LOG OUT ?",
                                                   font=("georgia", 15, "bold"), bg="cadetblue")
                                warn_label.place(x=5, y=100)

                                yes_butt = Button(logoutwin, text="Yes", width=7, height=3, font=("georgia", 14),
                                                  command=yes)
                                yes_butt.place(x=50, y=280)

                                no_butt = Button(logoutwin, text="No", width=7, height=3, font=("georgia", 14),
                                                 command=no)
                                no_butt.place(x=300, y=280)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')

                        menubar = Menu(admin)

                        def writeoffs():

                            con = mysql.connect(host='localhost', user='root', password="",
                                                database="retail-system2")
                            cursor = con.cursor()

                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()

                                def incre_id():
                                    global pap
                                    con = mysql.connect(host='localhost', user="root", password="",
                                                        database="retail-system2")
                                    cur = con.cursor()

                                    sql = "SELECT write_off_id FROM write_off ORDER BY write_off_id DESC LIMIT 1"
                                    cur.execute(sql)
                                    last_id = cur.fetchone()
                                    pap = int(last_id[0]) + 1
                                    fentry4.insert(0, "WO000000" + str(pap))

                                def insert():

                                    orderid = fentry4.get()
                                    date = cal.get()
                                    reference = fentry.get()
                                    product = fcombo.get()
                                    quantity = fentry2.get()
                                    price = fentry3.get()
                                    employee = str(employee_id[0])
                                    num1 = fentry3.get()
                                    num2 = fentry2.get()
                                    mul = float(price) * float(quantity)
                                    mul2 = str(mul)

                                    if (
                                            orderid == '' or date == '' or product == '' or quantity == ''):
                                        messagebox.showinfo("Insert Status", "All Fields Are Required")
                                    else:
                                        con = mysql.connect(host='localhost', user='root', password="",
                                                            database="retail-system2")
                                        cursor = con.cursor()
                                        cursor.execute(
                                            "insert into write_off(write_off_id,product_id,quantity,unit_price,total,reference,emp_id,date) values('" + str(pap) + "','" + product + "','" + quantity + "','" + price + "','" + mul2 + "','" + reference + "','" + employee + "','" + date + "')")

                                        cursor.execute("update product set unit_in_stock= unit_in_stock - '" + quantity + "' where product_id ='" + product + "'")
                                        cursor.execute("commit");

                                        sale = 'Write Off'
                                        cumulative = '100'

                                        cursor.execute(
                                            "insert into inventory_audit values('" + product + "', '" + sale + "', '" + quantity + "', '" + price + "', '" + cumulative + "', '" + date + "' )  ")
                                        cursor.execute("commit");

                                        cursor.execute(
                                            "update product set total_cost= unit_in_stock * cost_price where product_id='" + product + "'")
                                        cursor.execute("commit");
                                        fentry4.delete(0, 'end')
                                        cal.delete(0, 'end')
                                        fentry.delete(0, 'end')
                                        fcombo.delete(0, 'end')
                                        fentry2.delete(0, 'end')
                                        fentry3.delete(0, 'end')

                                        messagebox.showinfo("Insert Status", "Inserted")
                                        con.close()
                                        root.destroy()

                                def on_configure(event):
                                    my_canvas.configure(scrollregion=my_canvas.bbox('all'))

                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        transtrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=300)

                                transtrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",
                                                        height=23)
                                transtrv.place(x=0, y=0)

                                transtrv.column("1", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("2", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("3", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("4", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("5", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("6", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("7", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("8", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("9", anchor=CENTER, stretch=NO, width=130)

                                transtrv.heading(1, text="ID")
                                transtrv.heading(2, text="Product ID")
                                transtrv.heading(3, text="Quantity")
                                transtrv.heading(4, text="Unit Price")
                                transtrv.heading(5, text="Total")
                                transtrv.heading(6, text="Reference")
                                transtrv.heading(7, text="Employee ID")
                                transtrv.heading(8, text="Date")
                                transtrv.heading(9, text=" ")

                                cursor.execute("select * from write_off")
                                rows = cursor.fetchall()
                                update(rows)

                                cursor.close()



                                def get_product():
                                    root = Tk()
                                    root.geometry('1150x605+189+160')
                                    root.overrideredirect(1)
                                    root.attributes('-topmost', True)

                                    def update(rows):
                                        trv.delete(*trv.get_children())
                                        for i in rows:
                                            trv.insert('', 'end', values=i)

                                    def get_pro():
                                        pro = trv.focus()
                                        pro_main = trv.item(pro, "values")
                                        fcombo.delete(0, 'end')
                                        fcombo.insert(0, pro_main[0])
                                        root.destroy()

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(root, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                       height=23)
                                    trv.place(x=0, y=0)

                                    trv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    trv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    trv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    trv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    trv.heading(1, text="ID")
                                    trv.heading(2, text="Code")
                                    trv.heading(3, text="Name")
                                    trv.heading(4, text="Categroy ID")
                                    trv.heading(5, text="Sale Price")
                                    trv.heading(6, text="Unit ID")
                                    trv.heading(7, text="Unit in Stock")
                                    trv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    cursor.close()

                                    def lookup_products():
                                        productroot = Tk()
                                        productroot.geometry('250x150+600+300')
                                        productroot.title('Lookup Products')
                                        productroot.attributes('-topmost', True)
                                        productroot.iconbitmap(r'assets/titlelogo.ico')

                                        def search_view():
                                            def update(rows):
                                                trv.delete(*trv.get_children())
                                                for i in rows:
                                                    trv.insert('', 'end', values=i)

                                            mydb = mysql.connect(host='localhost', user="root", password="",
                                                                 database="retail-system2")
                                            cursor = mydb.cursor()

                                            cursor.execute(
                                                "select * from product where name like '%" + productname.get() + "%'")
                                            rows = cursor.fetchall()

                                            update(rows)
                                            productroot.destroy()

                                        productname = Entry(productroot, width=19, font=('georgia', 14))
                                        productname.place(x=10, y=20)

                                        product_search_butt = Button(productroot, width=10, height=3,
                                                                     font=('georgia', 10, 'bold'),
                                                                     text='Search\n' 'Name', command=search_view)
                                        product_search_butt.place(x=70, y=60)

                                    ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=get_pro)
                                    butt11.place(x=965, y=2)

                                    butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt12.place(x=560, y=2)

                                    butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt13.place(x=467, y=2)

                                    butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt14.place(x=374, y=2)

                                    butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt15.place(x=281, y=2)

                                    butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt16.place(x=188, y=2)

                                    butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt17.place(x=95, y=2)

                                    butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=lookup_products)
                                    butt18.place(x=2, y=2)

                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Write Off', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=insert)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt18.place(x=2, y=2)

                                wrapper2 = Frame(root, width=1150, height=240)

                                wrapper2.place(x=0, y=60)

                                my_canvas = Canvas(wrapper2, width=1150, height=240)
                                my_canvas.place(x=0, y=0)

                                frame = tkinter.Frame(my_canvas, width=1150, height=360)
                                frame.bind('<Configure>', on_configure)
                                my_canvas.create_window(0, 0, window=frame)

                                scrolly = tkinter.Scrollbar(wrapper2, command=my_canvas.yview)
                                scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
                                my_canvas.configure(yscrollcommand=scrolly.set)

                                f1 = Frame(frame, width=1130, height=28, bg="white")
                                f1.place(x=0, y=0)

                                fl1 = Label(f1, text="Write Off Number", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl1.place(x=40)

                                fentry4 = Entry(f1, font=('times new roman', 16), width=58)
                                fentry4.place(x=485)

                                f2 = Frame(frame, width=1130, height=28, bg='white')
                                f2.place(x=0, y=30)

                                fl2 = Label(f2, text="Receipt Date", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl2.place(x=40)

                                cal = DateEntry(f2, selectmode='day', width=69,
                                                font=('times new roman', 14), justify=LEFT, date_pattern="y-mm-dd")
                                cal.place(x=485, y=2)

                                f3 = Frame(frame, width=1130, height=28, bg='white')
                                f3.place(x=0, y=60)

                                fl3 = Label(f3, text="Supplier", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl3.place(x=40)



                                f4 = Frame(frame, width=1130, height=28, bg='white')
                                f4.place(x=0, y=90)

                                fl2 = Label(f4, text="Reference Number", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl2.place(x=40)

                                fentry = Entry(f4, font=('times new roman', 16), width=58)
                                fentry.place(x=485, y=2)

                                f5 = Frame(frame, width=1130, height=28, bg='white')
                                f5.place(x=0, y=120)

                                fl3 = Label(f5, text="Product ID", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl3.place(x=40)

                                fcombo = Entry(f5, width=20, font=("open sans", 16))
                                fcombo.place(x=485)

                                product_butt = Button(f5, width=1, height=1, text='...', command=get_product)
                                product_butt.place(x=1090)

                                product_cancel = Button(f5, width=1, height=1, text='X')
                                product_cancel.place(x=1110)

                                f6 = Frame(frame, width=1130, height=28, bg='white')
                                f6.place(x=0, y=150)

                                fl4 = Label(f6, text="Quantity", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl4.place(x=40)

                                fentry2 = Entry(f6, font=('times new roman', 16), width=58)
                                fentry2.place(x=485, y=2)

                                f7 = Frame(frame, width=1130, height=28, bg="white")
                                f7.place(x=0, y=180)

                                fl5 = Label(f7, text="Unit Price", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl5.place(x=40)

                                fentry3 = Entry(f7, font=('times new roman', 16), width=58)
                                fentry3.place(x=485)

                                f8 = Frame(frame, width=1130, height=28, bg="white")
                                f8.place(x=0, y=210)

                                fl6 = Label(f8, text="Employee ID", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl6.place(x=40)

                                f9 = Frame(frame, width=1130, height=28, bg="white")
                                f9.place(x=0, y=240)

                                fl7 = Label(f9, text="Supervisor", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl7.place(x=40)

                                fentry7 = Entry(f6, font=('times new roman', 16), width=58)
                                # fentry7.place(x=485)

                                f10 = Frame(frame, width=1130, height=28, bg="white")
                                f10.place(x=0, y=270)

                                fl8 = Label(f10, text="Receipt Date", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl8.place(x=40)

                                root.after(10, incre_id)

                            chib.after(3000, main_win)

                        def manage_emloyee():

                            def insert():
                                id = e11.get()
                                name = e12.get()
                                contact = e13.get()
                                gender = e14.get()
                                address = e15.get()
                                #proof = e16.get()
                                email = e17.get()
                                password = e18.get()
                                designation = e19.get()
                                if (
                                        id == '' or name == '' or contact == '' or gender == '' or address == '' or  email == '' or password == '' or designation == ''):
                                        messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into employee values('" + id + "','" + name + "','" + password + "','" + designation + "','" + contact + "','" + address + "','" + email + "','" + gender + "')")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e14.current(0)
                                    e15.delete(0, 'end')
                                    #   e16.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.current(0)

                                    messagebox.showinfo("Insert Status", "Inserted")
                                    con.close()

                            def delete():

                                if (e11.get() == ''):
                                        messagebox.showinfo("Delete Status", "Employee ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("delete from employee where id='" + e11.get() + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e14.current(0)
                                    e15.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.current(0)

                                    messagebox.showinfo("Delete Status", "Deleted Successfully")
                                    con.close()

                            def update():
                                id = e11.get()
                                name = e12.get()
                                contact = e13.get()
                                gender = e14.get()
                                address = e15.get()
                                email = e17.get()
                                password = e18.get()
                                designation = e19.get()

                                if ((
                                        id == '' or name == '' or contact == '' or gender == '' or address == ''
                                        or email == '' or password == '' or designation == '')):
                                    messagebox.showinfo("Update Status", "All Fields are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "update employee set name='" + name + "',contact='" + contact + "',gender='" + gender + "',address='" + address + "',email='" + email + "',password='" + password + "',designation='" + designation + "' where employee_id='" + id + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e14.set('')
                                    e15.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.set('')

                                    messagebox.showinfo("Update Status", "Update Successful")
                                    con.close()

                            def clear():
                                e10.delete(0, 'end')
                                e11.delete(0, 'end')
                                e12.delete(0, 'end')
                                e13.delete(0, 'end')
                                e14.current(0)
                                e15.delete(0, 'end')
                                e17.delete(0, 'end')
                                e18.delete(0, 'end')
                                e19.current(0)

                            def search():
                                if (e10.get() == ''):
                                    messagebox.showinfo("Search Status", "Employee ID is Required")
                                else:

                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e14.current(0)
                                    e15.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.current(0)

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from employee where employee_id='" + e10.get() + "'")
                                    rows = cursor.fetchall();

                                    for row in rows:
                                        e11.insert(0, row[0])
                                        e12.insert(0, row[1])
                                        e13.insert(0, row[4])
                                        e14.set(row[7])
                                        e15.insert(0, row[5])
                                        e17.insert(0, row[6])
                                        e18.insert(0, row[2])
                                        e19.set(row[3])

                                    con.close()

                            manage = Tk()
                            manage.geometry('1350x750')
                            manage.title('WiRi RETAIL SYSTEMS v1.00')
                            manage.iconbitmap(r'assets/titlelogo.ico')
                            manage.resizable(0, 0)
                            manage.configure(background='cadetblue')

                            l2 = Label(manage, text="EMPLOYEE MANAGEMENT", font=("times new roman", 35, 'bold'),
                                       bg="cadetblue")
                            l2.place(x=350, y=10)

                            frame1 = Frame(manage, width=730, height=80, relief=RIDGE, bg='cadetblue', bd=5)
                            frame1.place(x=300, y=80)

                            search_employee = Label(manage, text='Search Employee',
                                                    font=('times new roman', 12, "bold"), bg="cadetblue")
                            search_employee.place(x=310, y=70)

                            search_employee = Label(frame1, text='Employee ID',
                                                    font=('times new roman', 20, "bold"), bg="cadetblue")
                            search_employee.place(x=5, y=20)

                            e10 = Entry(frame1, width=20, bg="white", font=('times new roman', 20, "bold"))
                            e10.place(x=200, y=20)

                            buttsearch = Button(frame1, width=15, bg="white", text="Search",
                                                font=('times new roman', 14, "bold"), command=search)
                            buttsearch.place(x=500, y=20)

                            lab1 = Label(manage, text="Employee ID", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab1.place(x=200, y=190)

                            e11 = Entry(manage, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e11.place(x=400, y=190)

                            lab2 = Label(manage, text="Name", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab2.place(x=200, y=235)

                            e12 = Entry(manage, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e12.place(x=400, y=235)

                            lab3 = Label(manage, text="Contact No.", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab3.place(x=200, y=280)

                            e13 = Entry(manage, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e13.place(x=400, y=280)

                            lab4 = Label(manage, text="Gender Type", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab4.place(x=200, y=325)

                            e14 = ttk.Combobox(manage, font=('times new roman', 20), textvariable=choice,
                                               state="readonly", justify=LEFT, width=19)
                            e14['values'] = (" ", "Male", "Female")
                            e14.current(0)
                            e14.place(x=400, y=325)

                            lab5 = Label(manage, text="Address", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab5.place(x=200, y=370)

                            e15 = Entry(manage, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e15.place(x=400, y=370)

                            #lab6 = Label(manage, text="Proof Of ID", font=("times new roman", 20, "bold"),
                             #            bg="cadetblue")
                            #lab6.place(x=200, y=415)

                            #e16 = Entry(manage, width=20, bg="white", font=('times new roman', 20, "bold"),
                             #           relief=RIDGE, bd=2)
                            #e16.place(x=400, y=415)

                            lab7 = Label(manage, text="Email", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab7.place(x=700, y=190)

                            e17 = Entry(manage, width=22, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e17.place(x=900, y=190)

                            lab8 = Label(manage, text="Password", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab8.place(x=700, y=235)

                            e18 = Entry(manage, width=22, bg="white", font=('times new roman', 20, "bold"),
                                            relief=RIDGE, bd=2, show='*')
                            e18.place(x=900, y=235)

                            lab9 = Label(manage, text="Desgination", font=("times new roman", 20, "bold"),
                                             bg="cadetblue")
                            lab9.place(x=700, y=280)

                            e19 = ttk.Combobox(manage, font=('times new roman', 20), textvariable=choice,
                                                   state="readonly", justify=LEFT, width=21)
                            e19['values'] = (" ", "Admin", "Employee")
                            e19.current(0)
                            e19.place(x=900, y=280)

                            buttadd = Button(manage, width=15, bg="white", text="Add",
                                                 font=('times new roman', 14, "bold"), command=insert)
                            buttadd.place(x=250, y=600)

                            buttupdate = Button(manage, width=15, bg="white", text="Update",
                                                    font=('times new roman', 14, "bold"), command=update)
                            buttupdate.place(x=500, y=600)

                            buttdelete = Button(manage, width=15, bg="white", text="Delete",
                                                    font=('times new roman', 14, "bold"), command=delete)
                            buttdelete.place(x=750, y=600)

                            buttclear = Button(manage, width=15, bg="white", text="Clear",
                                                   font=('times new roman', 14, "bold"), command=clear)
                            buttclear.place(x=1000, y=600)

                            manage.mainloop()

                        def view_employee():
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.title('WiRi RETAIL SYSTEMS v1.00')
                            chib.iconbitmap(r'assets/titlelogo.ico')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)


                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root1 = Tk()
                                root1.geometry('1150x605+189+160')
                                root1.overrideredirect(1)
                                root1.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        emptrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="", database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root1, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                emptrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                      height=23)
                                emptrv.place(x=0, y=0)

                                emptrv.column("1", anchor=CENTER, stretch=NO, width=135)
                                emptrv.column("2", anchor=CENTER, stretch=NO, width=135)
                                emptrv.column("3", anchor=CENTER, stretch=NO, width=135)
                                emptrv.column("4", anchor=CENTER, stretch=NO, width=150)
                                emptrv.column("5", anchor=CENTER, stretch=NO, width=135)
                                emptrv.column("6", anchor=CENTER, stretch=NO, width=135)
                                emptrv.column("7", anchor=CENTER, stretch=NO, width=150)
                                emptrv.column("8", anchor=CENTER, stretch=NO, width=135)


                                emptrv.heading(1, text="Employee ID")
                                emptrv.heading(2, text="Name")
                                emptrv.heading(3, text="Password")
                                emptrv.heading(4, text="Designation")
                                emptrv.heading(5, text="Contact")
                                emptrv.heading(6, text="Address")
                                emptrv.heading(7, text="Email")
                                emptrv.heading(8, text="Gender")


                                cursor.execute("select * from employee")
                                rows = cursor.fetchall()
                                update(rows)

                                cursor.close()

                                def lookup_employee():
                                    emproot = Tk()
                                    emproot.geometry('250x150+600+300')
                                    emproot.title('Lookup Employee')
                                    emproot.attributes('-topmost', True)
                                    emproot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            emptrv.delete(*emptrv.get_children())
                                            for i in rows:
                                                emptrv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute(
                                            "select * from employee where name like '%" + empname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        emproot.destroy()

                                    empname = Entry(emproot, width=19, font=('georgia', 14))
                                    empname.place(x=10, y=20)

                                    emp_search_butt = Button(emproot, width=10, height=3,
                                                                  font=('georgia', 10, 'bold'), text='Search\n' 'Name',
                                                                  command=search_view)
                                    emp_search_butt.place(x=70, y=60)

                                ttframe = Frame(root1, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root1, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Employee', font=('times new roman', 19, 'bold'), bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=manage_emloyee)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lookup_employee)
                                butt18.place(x=2, y=2)

                            chib.after(3000, main_win)







                        def view_supplier():
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.title('WiRi RETAIL SYSTEMS v1.00')
                            chib.iconbitmap(r'assets/titlelogo.ico')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root1 = Tk()
                                root1.geometry('1150x605+189+160')
                                root1.overrideredirect(1)
                                root1.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        suptrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="", database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root1, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                suptrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6), show="headings",
                                                      height=23)
                                suptrv.place(x=0, y=0)

                                suptrv.column("1", anchor=CENTER, stretch=NO, width=190)
                                suptrv.column("2", anchor=CENTER, stretch=NO, width=190)
                                suptrv.column("3", anchor=CENTER, stretch=NO, width=190)
                                suptrv.column("4", anchor=CENTER, stretch=NO, width=190)
                                suptrv.column("5", anchor=CENTER, stretch=NO, width=190)
                                suptrv.column("6", anchor=CENTER, stretch=NO, width=190)

                                suptrv.heading(1, text="Supplier ID")
                                suptrv.heading(2, text="Supplier Code")
                                suptrv.heading(3, text="Name")
                                suptrv.heading(4, text="Contact")
                                suptrv.heading(5, text="Email")
                                suptrv.heading(6, text="Address")

                                cursor.execute("select * from supplier")
                                rows = cursor.fetchall()
                                update(rows)
                                cursor.close()

                                def lookup_supplier():
                                    suproot = Tk()
                                    suproot.geometry('250x150+600+300')
                                    suproot.title('Lookup Supplier')
                                    suproot.attributes('-topmost', True)
                                    suproot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            suptrv.delete(*suptrv.get_children())
                                            for i in rows:
                                                suptrv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute(
                                            "select * from supplier where supplier_name like '%" + supname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        suproot.destroy()

                                    supname = Entry(suproot, width=19, font=('georgia', 14))
                                    supname.place(x=10, y=20)

                                    sup_search_butt = Button(suproot, width=10, height=3,
                                                                  font=('georgia', 10, 'bold'), text='Search\n' 'Name',
                                                                  command=search_view)
                                    sup_search_butt.place(x=70, y=60)




                                ttframe=Frame(root1,width=1150,height=60,bg='cadetblue')
                                ttframe.place(x=0,y=0)

                                tt2frame = Frame(root1, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab=Label(ttframe,text='Supplier',font=('times new roman',19,'bold'),bg='cadetblue')
                                tlab.place(x=0,y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14,'bold'), width=8, height=3,
                                                command=root1.destroy)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14,'bold'), width=8, height=3,
                                                command=root1.destroy)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14,'bold'), width=8, height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14,'bold'), width=8, height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14,'bold'), width=8, height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14,'bold'), width=8, height=3,
                                                command=manage_supplier)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14,'bold'), width=8, height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14,'bold'), width=8, height=3,
                                                command=lookup_supplier)
                                butt18.place(x=2, y=2)



                            chib.after(3000, main_win)


                        def audit():
                            # splash.destroy()
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)
                                root.configure(background="white")

                                def get_pro():

                                    proroot = Tk()
                                    proroot.geometry('1150x605+189+160')
                                    proroot.overrideredirect(1)
                                    proroot.attributes('-topmost', True)

                                    def update(rows):
                                        protrv.delete(*protrv.get_children())
                                        for i in rows:
                                            protrv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(proroot, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    protrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8),
                                                          show="headings",
                                                          height=23)
                                    protrv.place(x=0, y=0)

                                    protrv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    protrv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    protrv.heading(1, text="ID")
                                    protrv.heading(2, text="Code")
                                    protrv.heading(3, text="Name")
                                    protrv.heading(4, text="Categroy ID")
                                    protrv.heading(5, text="Sale Price")
                                    protrv.heading(6, text="Unit ID")
                                    protrv.heading(7, text="Unit in Stock")
                                    protrv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    def insert_pro():
                                        global name_audit
                                        name_lab.configure(text='')
                                        category = protrv.focus()
                                        name_audit = protrv.item(category, "values")
                                        name_lab.configure(text=name_audit[2])
                                        proroot.destroy()

                                    cursor.close()

                                    ttframe = Frame(proroot, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(proroot, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=proroot.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=insert_pro)
                                    butt11.place(x=965, y=2)

                                def clear_pro():
                                    name_lab.configure(text='')

                                def clear_pro2():
                                    name_lab2.configure(text='')

                                def get_pro2():

                                    proroot = Tk()
                                    proroot.geometry('1150x605+189+160')
                                    proroot.overrideredirect(1)
                                    proroot.attributes('-topmost', True)

                                    def update(rows):
                                        protrv.delete(*protrv.get_children())
                                        for i in rows:
                                            protrv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(proroot, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    protrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8),
                                                          show="headings",
                                                          height=23)
                                    protrv.place(x=0, y=0)

                                    protrv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    protrv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    protrv.heading(1, text="ID")
                                    protrv.heading(2, text="Code")
                                    protrv.heading(3, text="Name")
                                    protrv.heading(4, text="Categroy ID")
                                    protrv.heading(5, text="Sale Price")
                                    protrv.heading(6, text="Unit ID")
                                    protrv.heading(7, text="Unit in Stock")
                                    protrv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    def insert_pro2():
                                        global name_audit2
                                        name_lab2.configure(text='')
                                        category = protrv.focus()
                                        name_audit2 = protrv.item(category, "values")
                                        name_lab2.configure(text=name_audit2[2])
                                        proroot.destroy()

                                    cursor.close()

                                    ttframe = Frame(proroot, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(proroot, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=proroot.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=insert_pro2)
                                    butt11.place(x=965, y=2)

                                def main_report():
                                    global img
                                    root1 = Tk()
                                    root1.geometry('1150x605+189+160')
                                    root1.overrideredirect(1)
                                    root1.attributes('-topmost', True)

                                    img = tk.PhotoImage(file="assets/imagelogo2small.png")

                                    def update(rows):
                                        for i in rows:
                                            emptrv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(root1, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    emptrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6), show="headings",
                                                          height=23)
                                    emptrv.place(x=0, y=0)

                                    emptrv.column("1", anchor=CENTER, stretch=NO, width=200)
                                    emptrv.column("2", anchor=CENTER, stretch=NO, width=200)
                                    emptrv.column("3", anchor=CENTER, stretch=NO, width=200)
                                    emptrv.column("4", anchor=CENTER, stretch=NO, width=200)
                                    emptrv.column("5", anchor=CENTER, stretch=NO, width=200)
                                    emptrv.column("6", anchor=CENTER, stretch=NO, width=200)


                                    emptrv.heading(1, text="Description")
                                    emptrv.heading(2, text="Document")
                                    emptrv.heading(3, text="Quantity")
                                    emptrv.heading(4, text="Cost")
                                    emptrv.heading(5, text="Cumulative Quantity")
                                    emptrv.heading(6, text="Date")

                                    a = from_date.get()
                                    b = to_date.get()

                                    try:
                                        cursor.execute(
                                            "SELECT * FROM `inventory_audit` WHERE `product` = '"+name_audit[0]+"' AND '"+name_audit2[0]+"' AND `transaction_date` BETWEEN '"+ a +"' AND '"+ b +"'")
                                        rows = cursor.fetchall()
                                    except:
                                        cursor.execute( "SELECT * FROM `inventory_audit` WHERE `transaction_date` BETWEEN '"+ a +"' AND '"+ b +"'")
                                        rows = cursor.fetchall()

                                    for i in range(len(rows)):
                                        rows[i] = list(rows[i])
                                        ids = str(rows[i][0])
                                        cursor.execute("select name from product where product_id = '"+ids+"' ")
                                        pro_ids = cursor.fetchall()
                                        for j in range(len(pro_ids)):
                                            rows[i][0] = pro_ids[j][0]
                                    update(rows)

                                    cursor.close()

                                    ttframe = Frame(root1, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(root1, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Inventory Audit', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root1.destroy)
                                    butt10.place(x=1057, y=2)



                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Inventory Audit', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                param_label = Label(root, text="Parameter Values",
                                                    font=('new times roman', 10, 'bold'), bg='white')
                                param_label.place(x=10, y=65)

                                from_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                from_frame.place(x=0, y=90)

                                from_label = Label(from_frame, text="From Date", font=('new times roman', 10),
                                                   bg='white')
                                from_label.place(x=10, y=5)

                                from_date = DateEntry(from_frame, selectmode='', width=61,
                                                      font=('times new roman', 14), justify=LEFT, bd=0,
                                                      date_pattern='y-mm-dd')
                                from_date.place(x=575, y=0)

                                to_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                to_frame.place(x=0, y=120)

                                to_label = Label(to_frame, text="To Date", font=('new times roman', 10),
                                                 bg='white')
                                to_label.place(x=10, y=5)

                                to_date = DateEntry(to_frame, selectmode='', width=61,
                                                    font=('times new roman', 14), justify=LEFT, bd=0,
                                                    date_pattern='y-mm-dd')
                                to_date.place(x=575, y=0)

                                store_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                store_frame.place(x=0, y=150)

                                store_label = Label(store_frame, text="Store", font=('new times roman', 10),
                                                    bg='white')
                                store_label.place(x=10, y=5)

                                store_name_frame = Frame(store_frame, width=575, height=30, bg='white', bd=1,
                                                         relief=RIDGE)
                                store_name_frame.place(x=575, y=0)

                                customer_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                customer_frame.place(x=0, y=180)

                                customer_label = Label(customer_frame, text="Customer",
                                                       font=('new times roman', 10),
                                                       bg='white')
                                customer_label.place(x=10, y=5)

                                customer_name_frame = Frame(customer_frame, width=575, height=30, bg='white', bd=1,
                                                            relief=RIDGE)
                                customer_name_frame.place(x=575, y=0)

                                get_customer = Button(customer_name_frame, width=1, height=1, text='...',
                                                      command=None, bd=0)
                                get_customer.place(x=540, y=2)

                                customer_cancel = Button(customer_name_frame, width=1, height=1, text='X', bd=0)
                                customer_cancel.place(x=555, y=2)

                                product_from_frame = Frame(root, width=1150, height=30, bg='white', bd=1,
                                                           relief=RIDGE)
                                product_from_frame.place(x=0, y=210)

                                product_from_label = Label(product_from_frame, text="From Product",
                                                           font=('new times roman', 10),
                                                           bg='white')
                                product_from_label.place(x=10, y=5)

                                product1_name_frame = Frame(product_from_frame, width=575, height=30, bg='white',
                                                            bd=1,
                                                            relief=RIDGE)
                                product1_name_frame.place(x=575, y=0)

                                get_product1 = Button(product1_name_frame, width=1, height=1, text='...',
                                                      command=get_pro,
                                                      bd=0)
                                get_product1.place(x=540, y=2)

                                product1_cancel = Button(product1_name_frame, width=1, height=1, text='X', bd=0,
                                                         command=clear_pro)
                                product1_cancel.place(x=555, y=2)

                                product_to_frame = Frame(root, width=1150, height=30, bg='white', bd=1,
                                                         relief=RIDGE)
                                product_to_frame.place(x=0, y=240)

                                product2_name_frame = Frame(product_to_frame, width=575, height=30, bg='white',
                                                            bd=1,
                                                            relief=RIDGE)
                                product2_name_frame.place(x=575, y=0)

                                get_product2 = Button(product2_name_frame, width=1, height=1, text='...',
                                                      command=get_pro2,
                                                      bd=0)
                                get_product2.place(x=540, y=2)

                                product2_cancel = Button(product2_name_frame, width=1, height=1, text='X', bd=0,
                                                         command=clear_pro2)
                                product2_cancel.place(x=555, y=2)

                                name_lab = Label(product1_name_frame, text='', font=('times new roman', 12),
                                                 bg='white')
                                name_lab.place(x=0, y=2)

                                name_lab2 = Label(product2_name_frame, text='', font=('times new roman', 12),
                                                  bg='white')
                                name_lab2.place(x=0, y=2)

                                product_to_label = Label(product_to_frame, text="To Product",
                                                         font=('new times roman', 10),
                                                         bg='white')
                                product_to_label.place(x=10, y=5)

                                report_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                report_frame.place(x=0, y=270)

                                report_label = Label(report_frame, text="Report By",
                                                     font=('new times roman', 10),
                                                     bg='white')
                                report_label.place(x=10, y=5)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=main_report)
                                butt11.place(x=965, y=2)

                            chib.after(3000, main_win)




                        def view_received():
                            # splash.destroy()
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root1 = Tk()
                                root1.geometry('1150x605+189+160')
                                root1.overrideredirect(1)
                                root1.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        transtrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root1, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                transtrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",
                                                        height=23)
                                transtrv.place(x=0, y=0)

                                transtrv.column("1", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("2", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("3", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("4", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("5", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("6", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("7", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("8", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("9", anchor=CENTER, stretch=NO, width=130)

                                transtrv.heading(1, text="ID")
                                transtrv.heading(2, text="Product ID")
                                transtrv.heading(3, text="Quantity")
                                transtrv.heading(4, text="Unit Price")
                                transtrv.heading(5, text="Total")
                                transtrv.heading(6, text="Supplier ID")
                                transtrv.heading(7, text="Date")
                                transtrv.heading(8, text="Employee ID")
                                transtrv.heading(9, text="Reference")

                                cursor.execute("select * from receive_product")
                                rows = cursor.fetchall()

                                update(rows)

                                cursor.close()

                                def lookup_received():
                                    receivedroot = Tk()
                                    receivedroot.geometry('250x150+600+300')
                                    receivedroot.title('Lookup Received')
                                    receivedroot.attributes('-topmost', True)
                                    receivedroot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            transtrv.delete(*transtrv.get_children())
                                            for i in rows:
                                                transtrv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute(
                                            "select * from receive_product where referece like '%" + receivedname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        receivedroot.destroy()

                                    receivedname = Entry(receivedroot, width=19, font=('georgia', 14))
                                    receivedname.place(x=10, y=20)

                                    received_search_butt = Button(receivedroot, width=10, height=3,
                                                                 font=('georgia', 10, 'bold'), text='Search\n' 'Name',
                                                                 command=search_view)
                                    received_search_butt.place(x=70, y=60)


                                ttframe = Frame(root1, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root1, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Received Product', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=send)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lookup_received)
                                butt18.place(x=2, y=2)

                            chib.after(3000, main_win)



                        def view_PO():
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.title('WiRi RETAIL SYSTEMS v1.00')
                            chib.iconbitmap(r'assets/titlelogo.ico')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root1 = Tk()
                                root1.geometry('1150x605+189+160')
                                root1.overrideredirect(1)
                                root1.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        transtrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root1, width=800, height=50)
                                wrapper1.place(x=0, y=60)



                                transtrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",
                                                        height=23)
                                transtrv.place(x=0, y=0)

                                transtrv.column("1", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("2", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("3", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("4", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("5", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("6", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("7", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("8", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("9", anchor=CENTER, stretch=NO, width=130)

                                transtrv.heading(1, text="ID")
                                transtrv.heading(2, text="Product ID")
                                transtrv.heading(3, text="Quantity")
                                transtrv.heading(4, text="Unit Price")
                                transtrv.heading(5, text="Total")
                                transtrv.heading(6, text="Supplier ID")
                                transtrv.heading(7, text="Date")
                                transtrv.heading(8, text="Employee ID")
                                transtrv.heading(9, text="Reference")


                                cursor.execute("select * from purchase_order")
                                rows = cursor.fetchall()
                                for i in range(len(rows)):
                                    rows[i] = list(rows[i])
                                    product_id = str(rows[i][1])
                                    cursor.execute("select name from product where product_id = '"+product_id+"'  ")
                                    ids = cursor.fetchall()
                                    for j in range(len(ids)):
                                        rows[i][1] = ids[j][0]

                                update(rows)

                                cursor.close()

                                def lookup_PO():
                                    POroot = Tk()
                                    POroot.geometry('250x150+600+300')
                                    POroot.title('Lookup PO')
                                    POroot.attributes('-topmost', True)
                                    POroot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            transtrv.delete(*transtrv.get_children())
                                            for i in rows:
                                                transtrv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute(
                                            "select * from purchase_order where reference_number like '%" + POname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        POroot.destroy()

                                    POname = Entry(POroot, width=19, font=('georgia', 14))
                                    POname.place(x=10, y=20)

                                    PO_search_butt = Button(POroot, width=10, height=3,
                                                                  font=('georgia', 10, 'bold'), text='Search\n' 'Name',
                                                                  command=search_view)
                                    PO_search_butt.place(x=70, y=60)

                                ttframe = Frame(root1, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root1, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Purchase Order', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root1.destroy)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3, 
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=receive)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lookup_PO)
                                butt18.place(x=2, y=2)

                            chib.after(3000, main_win)


                        def manage_supplier():
                            managesu = Toplevel()
                            managesu.geometry('1350x750')
                            managesu.title('WiRi RETAIL SYSTEMS v1.00')
                            managesu.iconbitmap(r'assets/titlelogo.ico')
                            managesu.resizable(0, 0)
                            managesu.configure(background='cadetblue')


                            def insert():
                                id = e11.get()
                                code = e12.get()
                                namee = e13.get()
                                contact = e16.get()
                                email = e18.get()
                                address = e17.get()

                                if (
                                        code == '' or namee == '' or contact == '' or  email == '' or address == ''):
                                        messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into supplier values('" + id + "','" + code + "','" + namee + "','" + contact + "','" + address + "','" + email + "')")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')

                                    e16.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')


                                    messagebox.showinfo("Insert Status", "Inserted")
                                    con.close()
                                    managesu.destroy()

                            def delete():

                                if (e11.get() == ''):
                                        messagebox.showinfo("Delete Status", "Supplier ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("delete from supplier where id='" + e11.get() + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')

                                    e16.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')


                                    messagebox.showinfo("Delete Status", "Deleted Successfully")
                                    con.close()
                                    managesu.destroy()

                            def update():
                                id = e11.get()
                                code = e12.get()
                                namee = e13.get()
                                contact = e16.get()
                                email = e18.get()
                                address = e17.get()


                                if ((
                                        code == '' or namee == '' or contact == '' or email == '' or address == '')):
                                    messagebox.showinfo("Update Status", "All Fields are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "update supplier set supplier_name='" + namee + "',contact='" + contact + "',email='" + email + "',address='" + address + "' where supplier_id='" + id + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')

                                    e16.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')


                                    messagebox.showinfo("Update Status", "Update Successful")
                                    con.close()
                                    managesu.destroy()

                            def clear():
                                e10.delete(0, 'end')
                                e11.delete(0, 'end')
                                e12.delete(0, 'end')
                                e13.delete(0, 'end')

                                e16.delete(0, 'end')
                                e17.delete(0, 'end')
                                e18.delete(0, 'end')


                            def search():
                                if (e10.get() == ''):
                                    messagebox.showinfo("Search Status", "Supplier ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from supplier where supplier_id='" + e10.get() + "'")
                                    rows = cursor.fetchall();

                                    for row in rows:
                                        e11.insert(0, row[0])
                                        e12.insert(0, row[1])
                                        e13.insert(0, row[2])
                                        e16.insert(0, row[3])
                                        e17.insert(0, row[4])
                                        e18.insert(0, row[5])


                                    con.close()



                            l2 = Label(managesu, text="SUPPLIER MANAGEMENT", font=("times new roman", 35, 'bold'),
                                       bg="cadetblue")
                            l2.place(x=350, y=10)

                            frame1 = Frame(managesu, width=730, height=80, relief=RIDGE, bg='cadetblue', bd=5)
                            frame1.place(x=300, y=80)

                            search_employee = Label(managesu, text='Search Supplier',
                                                    font=('times new roman', 12, "bold"), bg="cadetblue")
                            search_employee.place(x=310, y=70)

                            search_employee = Label(frame1, text='Supplier ID',
                                                    font=('times new roman', 20, "bold"), bg="cadetblue")
                            search_employee.place(x=5, y=20)

                            e10 = Entry(frame1, width=20, bg="white", font=('times new roman', 20, "bold"))
                            e10.place(x=200, y=20)

                            buttsearch = Button(frame1, width=15, bg="white", text="Search",
                                                font=('times new roman', 14, "bold"), command=search)
                            buttsearch.place(x=500, y=20)

                            lab1 = Label(managesu, text="Supplier ID", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab1.place(x=200, y=190)

                            e11 = Entry(managesu, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e11.place(x=400, y=190)

                            lab2 = Label(managesu, text="Code", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab2.place(x=200, y=235)

                            e12 = Entry(managesu, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e12.place(x=400, y=235)

                            lab3 = Label(managesu, text="Name", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab3.place(x=200, y=280)

                            e13 = Entry(managesu, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e13.place(x=400, y=280)



                            lab6 = Label(managesu, text="Contact", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab6.place(x=200, y=325)

                            e16 = Entry(managesu, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e16.place(x=400, y=325)

                            lab7 = Label(managesu, text="Email", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab7.place(x=700, y=190)

                            e17 = Entry(managesu, width=22, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e17.place(x=900, y=190)

                            lab8 = Label(managesu, text="Address", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab8.place(x=700, y=235)

                            e18 = Entry(managesu, width=22, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e18.place(x=900, y=235)



                            buttadd = Button(managesu, width=15, bg="white", text="Add",
                                             font=('times new roman', 14, "bold"), command=insert)
                            buttadd.place(x=250, y=600)

                            buttupdate = Button(managesu, width=15, bg="white", text="Update",
                                                font=('times new roman', 14, "bold"), command=update)
                            buttupdate.place(x=500, y=600)

                            buttdelete = Button(managesu, width=15, bg="white", text="Delete",
                                                font=('times new roman', 14, "bold"), command=delete)
                            buttdelete.place(x=750, y=600)

                            buttclear = Button(managesu, width=15, bg="white", text="Clear",
                                               font=('times new roman', 14, "bold"), command=clear)
                            buttclear.place(x=1000, y=600)

                            managesu.mainloop()


                        def manage_customer():
                            managecust = Toplevel()
                            managecust.geometry('1350x750')
                            managecust.title('WiRi RETAIL SYSTEMS v1.00')
                            managecust.iconbitmap(r'assets/titlelogo.ico')
                            managecust.resizable(0, 0)
                            managecust.configure(background='cadetblue')



                            def insert():
                                id = e11.get()
                                code = e12.get()
                                cusname = e13.get()
                                contact = e17.get()
                                address = e18.get()

                                if (
                                        code == '' or cusname == '' or contact == '' or  address == '' ):
                                        messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into customer values('" + id + "','" + code + "','" + cusname + "','" + contact + "','" + address + "')")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')


                                    messagebox.showinfo("Insert Status", "Inserted")
                                    con.close()
                                    managecust.destroy()


                            def delete():

                                if (e11.get() == ''):
                                        messagebox.showinfo("Delete Status", "Supplier ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("delete from customer where customer_id='" + e11.get() + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')


                                    messagebox.showinfo("Delete Status", "Deleted Successfully")
                                    con.close()

                            def update():
                                id = e11.get()
                                code = e12.get()
                                cusname = e13.get()
                                contact = e17.get()
                                address = e18.get()

                                if ((
                                        id == '' or code == '' or cusname == '' or contact == '' or address == '')):
                                    messagebox.showinfo("Update Status", "All Fields are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "update customer set customer_name='" + cusname + "',contact='" + contact + "',address='" + address + "' where id='" + id + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e13.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')


                                    messagebox.showinfo("Update Status", "Update Successful")
                                    con.close()

                            def clear():
                                e10.delete(0, 'end')
                                e11.delete(0, 'end')
                                e12.delete(0, 'end')
                                e13.delete(0, 'end')

                                e17.delete(0, 'end')
                                e18.delete(0, 'end')


                            def search():
                                if (e10.get() == ''):
                                    messagebox.showinfo("Search Status", "Supplier ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from customer where customer_id='" + e10.get() + "'")
                                    rows = cursor.fetchall();

                                    for row in rows:
                                        e11.insert(0, row[0])
                                        e12.insert(0, row[1])
                                        e13.insert(0, row[2])
                                        e17.insert(0, row[3])
                                        e18.insert(0, row[4])


                                    con.close()



                            l2 = Label(managecust, text="CUSTOMER MANAGEMENT", font=("times new roman", 35, 'bold'),
                                       bg="cadetblue")
                            l2.place(x=350, y=10)

                            frame1 = Frame(managecust, width=730, height=80, relief=RIDGE, bg='cadetblue', bd=5)
                            frame1.place(x=300, y=80)

                            search_employee = Label(managecust, text='Search Customer',
                                                    font=('times new roman', 12, "bold"), bg="cadetblue")
                            search_employee.place(x=310, y=70)

                            search_employee = Label(frame1, text='Customer ID',
                                                    font=('times new roman', 20, "bold"), bg="cadetblue")
                            search_employee.place(x=5, y=20)

                            e10 = Entry(frame1, width=20, bg="white", font=('times new roman', 20, "bold"))
                            e10.place(x=200, y=20)

                            buttsearch = Button(frame1, width=15, bg="white", text="Search",
                                                font=('times new roman', 14, "bold"), command=search)
                            buttsearch.place(x=500, y=20)

                            lab1 = Label(managecust, text="Customer ID", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab1.place(x=200, y=190)

                            e11 = Entry(managecust, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e11.place(x=400, y=190)

                            lab2 = Label(managecust, text="Customer Code", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab2.place(x=200, y=235)

                            e12 = Entry(managecust, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e12.place(x=400, y=235)

                            lab3 = Label(managecust, text="Name", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab3.place(x=200, y=280)

                            e13 = Entry(managecust, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e13.place(x=400, y=280)


                            lab7 = Label(managecust, text="Contact", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab7.place(x=700, y=190)

                            e17 = Entry(managecust, width=22, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e17.place(x=900, y=190)

                            lab8 = Label(managecust, text="Address", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab8.place(x=700, y=235)

                            e18 = Entry(managecust, width=22, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e18.place(x=900, y=235)

                            buttadd = Button(managecust, width=15, bg="white", text="Add",
                                             font=('times new roman', 14, "bold"), command=insert)
                            buttadd.place(x=250, y=600)

                            buttupdate = Button(managecust, width=15, bg="white", text="Update",
                                                font=('times new roman', 14, "bold"), command=update)
                            buttupdate.place(x=500, y=600)

                            buttdelete = Button(managecust, width=15, bg="white", text="Delete",
                                                font=('times new roman', 14, "bold"), command=delete)
                            buttdelete.place(x=750, y=600)

                            buttclear = Button(managecust, width=15, bg="white", text="Clear",
                                               font=('times new roman', 14, "bold"), command=clear)
                            buttclear.place(x=1000, y=600)

                            managecust.mainloop()

                        def view_customers():
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.title('WiRi RETAIL SYSTEMS v1.00')
                            chib.iconbitmap(r'assets/titlelogo.ico')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        custrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                custrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5), show="headings",
                                                        height=23)
                                custrv.place(x=0, y=0)

                                custrv.column("1", anchor=CENTER, stretch=NO, width=229)
                                custrv.column("2", anchor=CENTER, stretch=NO, width=229)
                                custrv.column("3", anchor=CENTER, stretch=NO, width=229)
                                custrv.column("4", anchor=CENTER, stretch=NO, width=229)
                                custrv.column("5", anchor=CENTER, stretch=NO, width=229)


                                custrv.heading(1, text="CustomerID")
                                custrv.heading(2, text="Customer Code")
                                custrv.heading(3, text="Name")
                                custrv.heading(4, text="Contact")
                                custrv.heading(5, text="Address")

                                cursor.execute("select * from customer")
                                rows = cursor.fetchall()
                                update(rows)

                                cursor.close()

                                def lookup_customer():
                                    cusroot = Tk()
                                    cusroot.geometry('250x150+600+300')
                                    cusroot.title('Lookup Customer')
                                    cusroot.attributes('-topmost', True)
                                    cusroot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            custrv.delete(*custrv.get_children())
                                            for i in rows:
                                                custrv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute(
                                            "select * from customer where name like '%" + cusname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        cusroot.destroy()

                                    cusname = Entry(cusroot, width=19, font=('georgia', 14))
                                    cusname.place(x=10, y=20)

                                    cus_search_butt = Button(cusroot, width=10, height=3,
                                                                  font=('georgia', 10, 'bold'), text='Search\n' 'Name',
                                                                  command=search_view)
                                    cus_search_butt.place(x=70, y=60)



                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Customer', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=manage_customer)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lookup_customer)
                                butt18.place(x=2, y=2)

                            chib.after(3000, main_win)



                    ####################################PRODUCTS########################################################



                        def view_products():
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.title('WiRi RETAIL SYSTEMS v1.00')
                            chib.iconbitmap(r'assets/titlelogo.ico')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)



                                def update(rows):
                                    trv.delete(*trv.get_children())
                                    for i in rows:
                                        trv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="", database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",
                                                   height=23)
                                trv.place(x=0, y=0)

                                trv.column("1", anchor=CENTER, stretch=NO, width=130)
                                trv.column("2", anchor=CENTER, stretch=NO, width=130)
                                trv.column("3", anchor=CENTER, stretch=NO, width=130)
                                trv.column("4", anchor=CENTER, stretch=NO, width=130)
                                trv.column("5", anchor=CENTER, stretch=NO, width=130)
                                trv.column("6", anchor=CENTER, stretch=NO, width=130)
                                trv.column("7", anchor=CENTER, stretch=NO, width=130)
                                trv.column("8", anchor=CENTER, stretch=NO, width=130)
                                trv.column("9", anchor=CENTER, stretch=NO, width=130)

                                trv.heading(1, text="ID")
                                trv.heading(2, text="Code")
                                trv.heading(3, text="Name")
                                trv.heading(4, text="Categroy ID")
                                trv.heading(5, text="Sale Price")
                                trv.heading(6, text="Unit ID")
                                trv.heading(7, text="Unit in Stock")
                                trv.heading(8, text="Discount Percentage")
                                trv.heading(9, text="Cost Price")


                                cursor.execute("select * from product")
                                rows = cursor.fetchall()
                                update(rows)

                                cursor.close()

                                def neg_stock():
                                    def update(rows):
                                        trv.delete(*trv.get_children())
                                        for i in rows:
                                            trv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()
                                    neg = "-"

                                    cursor.execute(
                                        "select * from product where unit_in_stock like '%" + neg + "%'")

                                    rows = cursor.fetchall()
                                    update(rows)

                                def report():
                                    try:
                                        global count
                                        con = mysql.connect(host='localhost', user='root', password="",
                                                            database="retail-system2")
                                        cursor = con.cursor()
                                        print_date = "Print Date: " + str(datetime.now().strftime("%Y-%m-%d"))
                                        cursor.execute("select * from product")
                                        products = cursor.fetchall()
                                        pdf_file = "multipage.pdf"
                                        can = canvas.Canvas(pdf_file)
                                        can.drawImage("klin.jpg", 20, 780, width=60, height=50)
                                        can.drawString(110, 810, "KLIN HORSE ENTERPRISES")
                                        can.drawString(110, 790, "Pumula East: No. 8566 Pumula East BYO")
                                        can.drawString(450, 810, print_date)
                                        can.drawString(20, 730, "Warehouse: Klin Horse Pumula")
                                        can.line(5, 750, 588, 750)
                                        can.line(5, 650, 588, 650)
                                        can.line(5, 750, 5, 650)
                                        can.line(588, 750, 588, 650)
                                        can.line(15, 610, 575, 610)
                                        can.line(15, 610, 15, 580)
                                        can.line(15, 580, 575, 580)
                                        can.line(575, 610, 575, 580)
                                        can.drawString(30, 590, "Sr")
                                        can.drawString(100, 590, "Code")
                                        can.drawString(200, 590, "Description")
                                        can.drawString(400, 590, "Quantity")
                                        can.drawString(500, 590, "Cost")
                                        can.drawString(600, 590, "Total Cost")
                                        count = 550
                                        for i in range(len(products)):
                                            row1 = "P000" + str(products[i][0])
                                            row2 = str(products[i][1])
                                            row3 = str(products[i][2])
                                            row4 = str(products[i][4])
                                            row5 = str(products[i][6])
                                            row6 = main_currency +''+ str(products[i][8])
                                            row7 = main_currency +''+ str(products[i][10])
                                            can.drawString(30, count, row1)
                                            can.drawString(100, count, row2)
                                            can.drawString(200, count, row3)
                                            can.drawString(400, count, row5)
                                            can.drawString(500, count, row6)
                                            can.drawString(600, count, row7)
                                            count -= 30
                                        can.showPage()
                                        print(i)
                                        if i > 23:
                                            cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 20")
                                            p2_products = cursor.fetchall()
                                            print(p2_products)
                                            count_p2 = 700
                                            for j in range(len(p2_products)):
                                                row1_p2 = "P000" + str(p2_products[j][0])
                                                row2_p2 = str(p2_products[j][1])
                                                row3_p2 = str(p2_products[j][2])
                                                row4_p2 = str(p2_products[j][4])
                                                row5_p2 = str(p2_products[j][6])
                                                row6_p2 = main_currency +''+ str(p2_products[j][8])
                                                row7_p2 = main_currency +''+ str(p2_products[j][10])
                                                can.drawString(20, 800, "2")
                                                can.drawString(30, count_p2, row1_p2)
                                                can.drawString(100, count_p2, row2_p2)
                                                can.drawString(200, count_p2, row3_p2)
                                                can.drawString(400, count_p2, row5_p2)
                                                can.drawString(500, count_p2, row6_p2)
                                                can.drawString(600, count_p2, row7_p2)
                                                count_p2 -= 30
                                            can.showPage()
                                            if j > 23:
                                                cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 43")
                                                p3_products = cursor.fetchall()
                                                count_p3 = 700
                                                for k in range(len(p3_products)):
                                                    row1_p3 = "P000" + str(p3_products[k][0])
                                                    row2_p3 = str(p3_products[k][1])
                                                    row3_p3 = str(p3_products[k][2])
                                                    row4_p3 = str(p3_products[k][4])
                                                    row5_p3 = str(p3_products[k][6])
                                                    row6_p3 = main_currency +''+ str(p3_products[k][8])
                                                    row7_p3 = main_currency +''+ str(p3_products[k][10])
                                                    can.drawString(20, 800, "3")
                                                    can.drawString(30, count_p3, row1_p3)
                                                    can.drawString(100, count_p3, row2_p3)
                                                    can.drawString(200, count_p3, row3_p3)
                                                    can.drawString(400, count_p3, row5_p3)
                                                    can.drawString(500, count_p3, row6_p3)
                                                    can.drawString(600, count_p3, row7_p3)
                                                    count_p3 -= 30

                                                can.showPage()
                                                if k > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 66")
                                                    p4_products = cursor.fetchall()
                                                    count_p4 = 700
                                                    for l in range(len(p4_products)):
                                                        row1_p4 = "P000" + str(p4_products[l][0])
                                                        row2_p4 = str(p4_products[l][1])
                                                        row3_p4 = str(p4_products[l][2])
                                                        row4_p4 = str(p4_products[l][4])
                                                        row5_p4 = str(p4_products[l][6])
                                                        row6_p4 = main_currency +''+ str(p4_products[l][8])
                                                        row7_p4 = main_currency +''+ str(p4_products[l][10])
                                                        can.drawString(20, 800, "4")
                                                        can.drawString(30, count_p4, row1_p4)
                                                        can.drawString(100, count_p4, row2_p4)
                                                        can.drawString(200, count_p4, row3_p4)
                                                        can.drawString(400, count_p4, row5_p4)
                                                        can.drawString(500, count_p4, row6_p4)
                                                        can.drawString(600, count_p4, row7_p4)
                                                        count_p4 -= 30
                                                can.showPage()
                                                if l > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 89")
                                                    p5_products = cursor.fetchall()
                                                    count_p5 = 700
                                                    for m in range(len(p5_products)):
                                                        row1_p5 = "P000" + str(p5_products[m][0])
                                                        row2_p5 = str(p5_products[m][1])
                                                        row3_p5 = str(p5_products[m][2])
                                                        row4_p5 = str(p5_products[m][4])
                                                        row5_p5 = str(p5_products[m][6])
                                                        row6_p5 = main_currency +''+ str(p5_products[m][8])
                                                        row7_p5 = main_currency +''+ str(p5_products[m][10])
                                                        can.drawString(20, 800, "5")
                                                        can.drawString(30, count_p5, row1_p5)
                                                        can.drawString(100, count_p5, row2_p5)
                                                        can.drawString(200, count_p5, row3_p5)
                                                        can.drawString(400, count_p5, row5_p5)
                                                        can.drawString(500, count_p5, row6_p5)
                                                        can.drawString(600, count_p5, row7_p5)
                                                        count_p5 -= 30

                                                can.showPage()
                                                if m > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 112")
                                                    p6_products = cursor.fetchall()
                                                    count_p6 = 700
                                                    for n in range(len(p6_products)):
                                                        row1_p6 = "P000" + str(p6_products[n][0])
                                                        row2_p6 = str(p6_products[n][1])
                                                        row3_p6 = str(p6_products[n][2])
                                                        row4_p6 = str(p6_products[n][4])
                                                        row5_p6 = str(p6_products[n][6])
                                                        row6_p6 = main_currency +''+ str(p6_products[n][8])
                                                        row7_p6 = main_currency +''+ str(p6_products[n][10])
                                                        can.drawString(20, 800, "6")
                                                        can.drawString(30, count_p6, row1_p6)
                                                        can.drawString(100, count_p6, row2_p6)
                                                        can.drawString(200, count_p6, row3_p6)
                                                        can.drawString(400, count_p6, row5_p6)
                                                        can.drawString(500, count_p6, row6_p6)
                                                        can.drawString(600, count_p6, row7_p6)
                                                        count_p6 -= 30
                                                can.showPage()
                                                if n > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 135")
                                                    p7_products = cursor.fetchall()
                                                    count_p7 = 700
                                                    for o in range(len(p7_products)):
                                                        row1_p7 = "P000" + str(p7_products[o][0])
                                                        row2_p7 = str(p7_products[o][1])
                                                        row3_p7 = str(p7_products[o][2])
                                                        row4_p7 = str(p7_products[o][4])
                                                        row5_p7 = str(p7_products[o][6])
                                                        row6_p7 = main_currency +''+ str(p7_products[o][8])
                                                        row7_p7 = main_currency +''+ str(p7_products[o][10])
                                                        can.drawString(20, 800, "7")
                                                        can.drawString(30, count_p7, row1_p7)
                                                        can.drawString(100, count_p7, row2_p7)
                                                        can.drawString(200, count_p7, row3_p7)
                                                        can.drawString(400, count_p7, row5_p7)
                                                        can.drawString(500, count_p7, row6_p7)
                                                        can.drawString(600, count_p7, row7_p7)
                                                        count_p7 -= 30
                                                can.showPage()
                                                if o > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 158")
                                                    p8_products = cursor.fetchall()
                                                    count_p8 = 700
                                                    for p in range(len(p8_products)):
                                                        row1_p8 = "P000" + str(p8_products[p][0])
                                                        row2_p8 = str(p8_products[p][1])
                                                        row3_p8 = str(p8_products[p][2])
                                                        row4_p8 = str(p8_products[p][4])
                                                        row5_p8 = str(p8_products[p][6])
                                                        row6_p8 = main_currency +''+ str(p8_products[p][8])
                                                        row7_p8 = main_currency +''+ str(p8_products[p][10])
                                                        can.drawString(20, 800, "8")
                                                        can.drawString(30, count_p8, row1_p8)
                                                        can.drawString(100, count_p8, row2_p8)
                                                        can.drawString(200, count_p8, row3_p8)
                                                        can.drawString(400, count_p8, row5_p8)
                                                        can.drawString(500, count_p8, row6_p8)
                                                        can.drawString(600, count_p8, row7_p8)
                                                        count_p7 -= 30
                                                can.showPage()
                                                if p > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 181")
                                                    p9_products = cursor.fetchall()
                                                    count_p9 = 700
                                                    for q in range(len(p9_products)):
                                                        row1_p9 = "P000" + str(p9_products[q][0])
                                                        row2_p9 = str(p9_products[q][1])
                                                        row3_p9 = str(p9_products[q][2])
                                                        row4_p9 = str(p9_products[q][4])
                                                        row5_p9 = str(p9_products[q][6])
                                                        row6_p9 = main_currency +''+ str(p9_products[q][8])
                                                        row7_p9 = main_currency +''+ str(p9_products[q][10])
                                                        can.drawString(20, 800, "9")
                                                        can.drawString(30, count_p9, row1_p9)
                                                        can.drawString(100, count_p9, row2_p9)
                                                        can.drawString(200, count_p9, row3_p9)
                                                        can.drawString(400, count_p9, row5_p9)
                                                        can.drawString(500, count_p9, row6_p9)
                                                        can.drawString(600, count_p9, row7_p9)
                                                        count_p9 -= 30
                                                can.showPage()
                                                if q > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 204")
                                                    p10_products = cursor.fetchall()
                                                    count_p10 = 700
                                                    for r in range(len(p10_products)):
                                                        row1_p10 = "P000" + str(p10_products[r][0])
                                                        row2_p10 = str(p10_products[r][1])
                                                        row3_p10 = str(p10_products[r][2])
                                                        row4_p10 = str(p10_products[r][4])
                                                        row5_p10 = str(p10_products[r][6])
                                                        row6_p10 = main_currency +''+ str(p10_products[r][8])
                                                        row7_p10 = main_currency +''+ str(p10_products[r][10])
                                                        can.drawString(20, 800, "10")
                                                        can.drawString(30, count_p10, row1_p10)
                                                        can.drawString(100, count_p10, row2_p10)
                                                        can.drawString(200, count_p10, row3_p10)
                                                        can.drawString(400, count_p10, row5_p10)
                                                        can.drawString(500, count_p10, row6_p10)
                                                        can.drawString(600, count_p10, row7_p10)
                                                        count_p10 -= 30
                                                can.showPage()
                                                if r > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 227")
                                                    p11_products = cursor.fetchall()
                                                    count_p11 = 700
                                                    for s in range(len(p11_products)):
                                                        row1_p11 = "P000" + str(p11_products[s][0])
                                                        row2_p11 = str(p11_products[s][1])
                                                        row3_p11 = str(p11_products[s][2])
                                                        row4_p11 = str(p11_products[s][4])
                                                        row5_p11 = str(p11_products[s][6])
                                                        row6_p11 = main_currency +''+ str(p11_products[s][8])
                                                        row7_p11 = main_currency +''+ str(p11_products[s][10])
                                                        can.drawString(20, 800, "11")
                                                        can.drawString(30, count_p11, row1_p11)
                                                        can.drawString(100, count_p11, row2_p11)
                                                        can.drawString(200, count_p11, row3_p11)
                                                        can.drawString(400, count_p11, row5_p11)
                                                        can.drawString(500, count_p11, row6_p11)
                                                        can.drawString(600, count_p11, row7_p11)
                                                        count_p11 -= 30
                                                can.showPage()
                                                if s > 23:
                                                    cursor.execute("SELECT * FROM `product` WHERE `product_id` >= 250")
                                                    p12_products = cursor.fetchall()
                                                    count_p12 = 700
                                                    for t in range(len(p12_products)):
                                                        row1_p12 = "P000" + str(p11_products[s][0])
                                                        row2_p12 = str(p12_products[s][1])
                                                        row3_p12 = str(p12_products[s][2])
                                                        row4_p12 = str(p12_products[s][4])
                                                        row5_p12 = str(p12_products[s][6])
                                                        row6_p12 = main_currency +''+ str(p12_products[s][8])
                                                        row7_p12 = main_currency +''+ str(p12_products[s][10])
                                                        can.drawString(20, 800, "11")
                                                        can.drawString(30, count_p12, row1_p12)
                                                        can.drawString(100, count_p12, row2_p12)
                                                        can.drawString(200, count_p12, row3_p12)
                                                        can.drawString(400, count_p12, row5_p12)
                                                        can.drawString(500, count_p12, row6_p12)
                                                        can.drawString(600, count_p12, row7_p12)
                                                        count_p12 -= 30
                                                can.showPage()
                                        can.save()
                                        file_name = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
                                        os.startfile('multipage.pdf', 'print')
                                        messagebox.showinfo('Success', "Report Printed Out")

                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')

                                def lookup_products():
                                    productroot = Tk()
                                    productroot.geometry('250x150+600+300')
                                    productroot.title('Lookup Products')
                                    productroot.attributes('-topmost', True)
                                    productroot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            trv.delete(*trv.get_children())
                                            for i in rows:
                                                trv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute("select * from product where name like '%" + productname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        productroot.destroy()



                                    productname = Entry(productroot,width=19,font=('georgia',14))
                                    productname.place(x=10,y=20)

                                    product_search_butt = Button(productroot,width=10,height=3,font=('georgia',10,'bold'),text='Search\n' 'Name',command=search_view)
                                    product_search_butt.place(x=70,y=60)






                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'), bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='Print', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=report)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=manage_products)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Show\n''Negative', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=neg_stock)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lookup_products)
                                butt18.place(x=2, y=2)

                            chib.after(3000, main_win)

                        def manage_products():

                            con = mysql.connect(host='localhost', user='root', password="",
                                                database="retail-system2")
                            cursor = con.cursor()
                            sql = "SELECT category_id FROM product_category"
                            cursor.execute(sql)
                            my_list = cursor.fetchall()


                            sql2 = "SELECT unit_id FROM product_unit"
                            cursor.execute(sql2)
                            my_unit = cursor.fetchall()

                            sql3 = "SELECT employee_id FROM employee"
                            cursor.execute(sql3)
                            my_employee = cursor.fetchall()



                            managepro = Toplevel()
                            managepro.geometry('1350x750')
                            managepro.title('WiRi RETAIL SYSTEMS v1.00')
                            managepro.iconbitmap(r'assets/titlelogo.ico')
                            managepro.resizable(0, 0)
                            managepro.configure(background='cadetblue')

                            def insert():
                                id = e11.get()
                                name = e12.get()
                                category = e16.get()
                                unit = enprounit.get()
                                code = e17.get()
                                sale = e18.get()
                                discount = '0'
                                employee = str(employee_id[0])
                                instock = e21.get()
                                cost = e19.get()
                                diff = str(float(sale) - float(cost))
                                total_cost = str(float(cost) * float(instock))



                                if (
                                       code == '' or name == '' or  category == ''  or sale == '' or unit == ''):
                                    messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into product values('" + id + "','" + code + "','" + name + "','" + category + "','" + sale + "','" + unit + "','" + instock + "','" + discount + "','" + cost + "','" + diff + "','" + total_cost + "','" + employee + "')")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e16.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.set('')
                                    e21.delete(0,'end')
                                    enprounit.set('')


                                    con.close()

                                    messagebox.showinfo("Insert Status",  "Successful")
                                    managepro.destroy()


                            def delete():

                                if (e11.get() == ''):
                                    messagebox.showinfo("Delete Status", "Product ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("delete from product where product_id='" + e11.get() + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e16.set('')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.set('')
                                    e21.delete(0, 'end')
                                    enprounit.set('')

                                    messagebox.showinfo("Delete Status", "Deleted Successfully")
                                    con.close()

                            def update():
                                id = e11.get()
                                name = e12.get()
                                category = e16.get()
                                unit = enprounit.get()
                                code = e17.get()
                                sale = e18.get()
                                cost = e19.get()
                                instock = e21.get()

                                if ((
                                        name == '' or category == '' or unit == '' or code == '' or sale == ''or instock == '')):
                                    messagebox.showinfo("Update Status", "All Fields are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "update product set name='" + name + "',category_id='" + category + "' ,unit_price='" + sale + "' ,unit_in_stock='" + instock + "',cost_price='" + cost + "', diff_cost= unit_price - cost_price , total_cost = cost_price * '"+instock+"' where product_id='" + id + "'")
                                    cursor.execute("commit");
                                    e11.delete(0, 'end')
                                    e12.delete(0, 'end')
                                    e16.delete(0, 'end')
                                    e17.delete(0, 'end')
                                    e18.delete(0, 'end')
                                    e19.delete(0, 'end')
                                    e21.delete(0, 'end')
                                    enprounit.delete(0, 'end')


                                    messagebox.showinfo("Update Status", "Update Successful")
                                    con.close()
                                    managepro.destroy()

                            def clear():
                                e10.delete(0, 'end')
                                e11.delete(0, 'end')
                                e12.delete(0, 'end')
                                e16.delete(0, 'end')
                                e17.delete(0, 'end')
                                e18.delete(0, 'end')
                                e19.delete(0, 'end')
                                e21.delete(0, 'end')
                                enprounit.delete(0, 'end')


                            def search():

                                e11.delete(0, 'end')
                                e12.delete(0, 'end')
                                e16.delete(0, 'end')
                                e17.delete(0, 'end')
                                e18.delete(0, 'end')
                                e19.delete(0, 'end')
                                e21.delete(0, 'end')
                                enprounit.delete(0, 'end')

                                if (e10.get() == ''):
                                    messagebox.showinfo("Search Status", "Product ID is Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from product where product_id='" + e10.get() + "'")
                                    rows = cursor.fetchall();

                                    for row in rows:
                                        e11.insert(0, row[0])
                                        e17.insert(0, row[1])
                                        e12.insert(0, row[2])
                                        e16.insert(0, row[3])
                                        e18.insert(0, row[4])
                                        enprounit.insert(0, row[5])
                                        e21.insert(0, row[6])
                                        e19.insert(0, row[7])


                                    con.close()


                            def get_category():
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                def update(rows):
                                    trv_category.delete(*trv_category.get_children())
                                    for i in rows:
                                        trv_category.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                trv_category = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                   height=23)
                                trv_category.place(x=0, y=0)

                                trv_category.column("1", anchor=CENTER, stretch=NO, width=146)
                                trv_category.column("2", anchor=CENTER, stretch=NO, width=146)
                                trv_category.column("3", anchor=CENTER, stretch=NO, width=180)
                                trv_category.column("4", anchor=CENTER, stretch=NO, width=120)
                                trv_category.column("5", anchor=CENTER, stretch=NO, width=146)
                                trv_category.column("6", anchor=CENTER, stretch=NO, width=120)
                                trv_category.column("7", anchor=CENTER, stretch=NO, width=146)
                                trv_category.column("8", anchor=CENTER, stretch=NO, width=150)

                                trv_category.heading(1, text="ID")
                                trv_category.heading(2, text="Category")
                                trv_category.heading(3, text="xxxxxxxxxxxxx")
                                trv_category.heading(4, text="xxxxxxxxxxxxx")
                                trv_category.heading(5, text="xxxxxxxxxxxxx")
                                trv_category.heading(6, text="xxxxxxxxxxxxx")
                                trv_category.heading(7, text="xxxxxxxxxxxxx")
                                trv_category.heading(8, text="xxxxxxxxxxxxx")

                                cursor.execute("select * from product_category")
                                rows = cursor.fetchall()
                                update(rows)

                                cursor.close()

                                def insert_category():
                                    category = trv_category.focus()

                                    category_main = trv_category.item(category, "values")
                                    e16.delete(0, 'end')
                                    e16.insert(0,category_main[0])
                                    root.destroy()


                                ttframe = Frame(root, width=1150, height=60, bg='black')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='black')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Product Category', font=('times new roman', 19, 'bold'),
                                             bg='black', fg='white')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=insert_category)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=DISABLED)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)




                            def get_unit():
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                def update(rows):
                                    trv_unit.delete(*trv_unit.get_children())
                                    for i in rows:
                                        trv_unit.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                trv_unit = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                   height=23)
                                trv_unit.place(x=0, y=0)

                                trv_unit.column("1", anchor=CENTER, stretch=NO, width=150)
                                trv_unit.column("2", anchor=CENTER, stretch=NO, width=150)
                                trv_unit.column("3", anchor=CENTER, stretch=NO, width=180)
                                trv_unit.column("4", anchor=CENTER, stretch=NO, width=120)
                                trv_unit.column("5", anchor=CENTER, stretch=NO, width=146)
                                trv_unit.column("6", anchor=CENTER, stretch=NO, width=120)
                                trv_unit.column("7", anchor=CENTER, stretch=NO, width=146)
                                trv_unit.column("8", anchor=CENTER, stretch=NO, width=150)

                                trv_unit.heading(1, text="Unit ID")
                                trv_unit.heading(2, text="Unit")
                                trv_unit.heading(3, text="xxxxxxxxxxxx")
                                trv_unit.heading(4, text="xxxxxxxxxxxx")
                                trv_unit.heading(5, text="xxxxxxxxxxxx")
                                trv_unit.heading(6, text="xxxxxxxxxxxx")
                                trv_unit.heading(7, text="xxxxxxxxxxxx")
                                trv_unit.heading(8, text="xxxxxxxxxxxx")

                                cursor.execute("select * from product_unit")
                                rows = cursor.fetchall()
                                update(rows)

                                cursor.close()

                                def insert_unit():
                                    unit = trv_unit.focus()

                                    unit_main = trv_unit.item(unit, "values")
                                    enprounit.delete(0,'end')
                                    enprounit.insert(0,unit_main[0])
                                    root.destroy()


                                ttframe = Frame(root, width=1150, height=60, bg='black')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='black')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Product Category', font=('times new roman', 19, 'bold'),
                                             bg='black', fg='white')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=insert_unit)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=DISABLED)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)




                            l2 = Label(managepro, text="PRODUCT MANAGEMENT", font=("times new roman", 35, 'bold'),
                                       bg="cadetblue")
                            l2.place(x=350, y=10)

                            frame1 = Frame(managepro, width=730, height=80, relief=RIDGE, bg='cadetblue', bd=5)
                            frame1.place(x=300, y=80)

                            search_employee = Label(managepro, text='Search Product',
                                                    font=('times new roman', 12, "bold"), bg="cadetblue")
                            search_employee.place(x=310, y=70)

                            search_employee = Label(frame1, text='Product ID',
                                                    font=('times new roman', 20, "bold"), bg="cadetblue")
                            search_employee.place(x=5, y=20)

                            e10 = Entry(frame1, width=20, bg="white", font=('times new roman', 20, "bold"))
                            e10.place(x=200, y=20)

                            buttsearch = Button(frame1, width=15, bg="white", text="Search",
                                                font=('times new roman', 14, "bold"), command=search)
                            buttsearch.place(x=500, y=20)

                            lab1 = Label(managepro, text="Product ID", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab1.place(x=200, y=190)

                            e11 = Entry(managepro, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e11.place(x=400, y=190)

                            lab2 = Label(managepro, text="Name", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab2.place(x=200, y=235)

                            e12 = Entry(managepro, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e12.place(x=400, y=235)



                            lab6 = Label(managepro, text="Category ", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab6.place(x=200, y=280)



                            e16 = Entry(managepro,width=17,font=("times new roman",20))
                            e16.place(x=400,y=280)

                            category_butt = Button(managepro, width=1, text="...",command=get_category)
                            category_butt.place(x=680,y=290)

                            labprounit = Label(managepro, text="Product Unit", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            labprounit.place(x=200, y=325)

                            enprounit = Entry(managepro,width=17,font=("times new roman",20))
                            enprounit.place(x=400,y=325)

                            unit_butt = Button(managepro, width=1, text="...",command=get_unit)
                            unit_butt.place(x=680, y=335)

                            lab7 = Label(managepro, text="Product Code", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab7.place(x=700, y=190)

                            e17 = Entry(managepro, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e17.place(x=900, y=190)

                            lab8 = Label(managepro, text="Sale Price", font=("times new roman", 20, "bold"),
                                         bg="cadetblue")
                            lab8.place(x=700, y=235)

                            e18 = Entry(managepro, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e18.place(x=900, y=235)

                            lab9 = Label(managepro, text="Cost Price", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab9.place(x=700, y=280)

                            e19 = Entry(managepro, width=20, font=('times new roman', 20, "bold"))
                            e19.place(x=900, y=280)

                            lab10 = Label(managepro, text="In Stock", font=("times new roman", 20, "bold"), bg="cadetblue")
                            lab10.place(x=700, y=325)


                            e21 = Entry(managepro, width=20, bg="white", font=('times new roman', 20, "bold"),
                                        relief=RIDGE, bd=2)
                            e21.place(x=900, y=325)



                            buttadd = Button(managepro, width=15, bg="white", text="Add",
                                             font=('times new roman', 14, "bold"), command=insert)
                            buttadd.place(x=250, y=600)

                            buttupdate = Button(managepro, width=15, bg="white", text="Update",
                                                font=('times new roman', 14, "bold"), command=update)
                            buttupdate.place(x=500, y=600)

                            buttdelete = Button(managepro, width=15, bg="white", text="Delete",
                                                font=('times new roman', 14, "bold"), command=delete)
                            buttdelete.place(x=750, y=600)

                            buttclear = Button(managepro, width=15, bg="white", text="Clear",
                                               font=('times new roman', 14, "bold"), command=clear)
                            buttclear.place(x=1000, y=600)

                            buttscan = Button(managepro, width=10, bg="white", text="Scan",
                                               font=('times new roman', 14, "bold"), command=None)
                            buttscan.place(x=1200, y=190)



                            managepro.mainloop()

                        def productcategory():
                            will = Toplevel()
                            will.geometry('750x500+320+150')
                            will.iconbitmap(r'assets/titlelogo.ico')
                            will.resizable(0, 0)

                            def insert():
                                id = willentry.get()
                                name = willentry2.get()

                                if (
                                        name == '' ):
                                    messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                      database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into product_category values('" + id + "','" + name + "')")
                                    cursor.execute("commit");
                                    willentry.delete(0, 'end')
                                    willentry2.delete(0, 'end')


                                    messagebox.showinfo("Insert Status", "Inserted")
                                    con.close()
                                    will.destroy()


                            willframe = Frame(will,width=750,height=80,bg="lightblue")
                            willframe.place(x=0,y=0)

                            willlabel = Label(willframe,text="Product Category",font=("open sans",14),bg="lightblue")
                            willlabel.place(x=0,y=45)

                            willlabel2 = Label(will,text="Category ID",font=("open sans",14))
                            willlabel2.place(x=10,y=150)

                            willlabel3 = Label(will,text="Category Name",font=("open sans",14))
                            willlabel3.place(x=10,y=250)

                            willentry = Entry(will,width=20,font=("open sans",14))
                            willentry.place(x=200,y=150)

                            willentry2 = Entry(will, width=20, font=("open sans", 14))
                            willentry2.place(x=200, y=250)

                            willframe2 = Frame(will,width=750,height=80,bg="cadetblue")
                            willframe2.place(x=0,y=421)

                            def closewill():
                                will.destroy()

                            willbut = Button(willframe2,text="Search",font=("open sans",10),width=15,height=5,command=None)
                            willbut.place(x=12,y=2)

                            willbut2 = Button(willframe2, text="Add", font=("open sans", 10), width=15, height=5,
                                             command=insert)
                            willbut2.place(x=160, y=2)

                            willbut3 = Button(willframe2, text="Delete", font=("open sans", 10), width=15, height=5,
                                             command=None)
                            willbut3.place(x=308, y=2)

                            willbut4 = Button(willframe2, text="Copy", font=("open sans", 10), width=15, height=5,
                                             command=None)
                            willbut4.place(x=456, y=2)

                            willbut5 = Button(willframe2, text="Cancel", font=("open sans", 10), width=15, height=5,
                                             command=closewill)
                            willbut5.place(x=604, y=2)


                        def productunit():

                            will = Toplevel()
                            will.geometry('750x500+320+150')
                            will.iconbitmap(r'assets/titlelogo.ico')
                            will.resizable(0, 0)

                            def insert():
                                id = willentry.get()
                                name = willentry2.get()

                                if (
                                        name == '' ):
                                    messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into product_unit values('" + id + "','" + name + "')")
                                    cursor.execute("commit");
                                    willentry.delete(0, 'end')
                                    willentry2.delete(0, 'end')

                                    messagebox.showinfo("Insert Status", "Inserted")
                                    con.close()
                                    will.destroy()

                            willframe = Frame(will, width=750, height=80, bg="lightblue")
                            willframe.place(x=0, y=0)

                            willlabel = Label(willframe, text="Product Unit", font=("open sans", 14), bg="lightblue")
                            willlabel.place(x=0, y=45)

                            willlabel2 = Label(will, text="Unit ID", font=("open sans", 14))
                            willlabel2.place(x=10, y=150)

                            willlabel3 = Label(will, text="Unit Name", font=("open sans", 14))
                            willlabel3.place(x=10, y=250)

                            willentry = Entry(will, width=20, font=("open sans", 14))
                            willentry.place(x=200, y=150)

                            willentry2 = Entry(will, width=20, font=("open sans", 14))
                            willentry2.place(x=200, y=250)

                            willframe2 = Frame(will, width=750, height=80, bg="cadetblue")
                            willframe2.place(x=0, y=421)

                            def closewill():
                                will.destroy()

                            willbut = Button(willframe2, text="Search", font=("open sans", 10), width=15, height=5,
                                             command=None)
                            willbut.place(x=12, y=2)

                            willbut2 = Button(willframe2, text="Add", font=("open sans", 10), width=15, height=5,
                                              command=insert)
                            willbut2.place(x=160, y=2)

                            willbut3 = Button(willframe2, text="Delete", font=("open sans", 10), width=15, height=5,
                                              command=None)
                            willbut3.place(x=308, y=2)

                            willbut4 = Button(willframe2, text="Copy", font=("open sans", 10), width=15, height=5,
                                              command=None)
                            willbut4.place(x=456, y=2)

                            willbut5 = Button(willframe2, text="Cancel", font=("open sans", 10), width=15, height=5,
                                              command=closewill)
                            willbut5.place(x=604, y=2)






##################################################################CustomerInvoices##########################################################################





                        def customerbill():
                            # splash.destroy()
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)



                                def update(rows):
                                    for i in rows:
                                        transtrv.insert('', 'end', values=i)





                                mydb = mysql.connect(host='localhost', user="root", password="", database="retail-system2")
                                cursor = mydb.cursor()


                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=60)

                                transtrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7,8), show="headings",
                                                   height=23)
                                transtrv.place(x=0, y=0)

                                transtrv.column("1", anchor=CENTER, stretch=NO, width=140)
                                transtrv.column("2", anchor=CENTER, stretch=NO, width=140)
                                transtrv.column("3", anchor=CENTER, stretch=NO, width=140)
                                transtrv.column("4", anchor=CENTER, stretch=NO, width=140)
                                transtrv.column("5", anchor=CENTER, stretch=NO, width=140)
                                transtrv.column("6", anchor=CENTER, stretch=NO, width=140)
                                transtrv.column("7", anchor=CENTER, stretch=NO, width=160)
                                transtrv.column("8", anchor=CENTER, stretch=NO, width=140)




                                transtrv.heading(1, text="Transaction ID")
                                transtrv.heading(2, text="Customer ID")
                                transtrv.heading(3, text="Payment Type")
                                transtrv.heading(4, text="Total Amount")
                                transtrv.heading(5, text="Amount Tendered")
                                transtrv.heading(6, text="Change")
                                transtrv.heading(7, text="Date")
                                transtrv.heading(8, text="Employee ID")


                                cursor.execute("select * from transaction")
                                rows = cursor.fetchall()
                                update(rows)

                                def lookup_transaction():
                                    billroot = Tk()
                                    billroot.geometry('250x150+600+300')
                                    billroot.title('Lookup Bill')
                                    billroot.attributes('-topmost', True)
                                    billroot.iconbitmap(r'assets/titlelogo.ico')

                                    def search_view():
                                        def update(rows):
                                            transtrv.delete(*transtrv.get_children())
                                            for i in rows:
                                                transtrv.insert('', 'end', values=i)

                                        mydb = mysql.connect(host='localhost', user="root", password="",
                                                             database="retail-system2")
                                        cursor = mydb.cursor()

                                        cursor.execute(
                                            "select * from transaction where transaction_id like '%" + billname.get() + "%'")
                                        rows = cursor.fetchall()

                                        update(rows)
                                        billroot.destroy()

                                    billname = Entry(billroot, width=19, font=('georgia', 14))
                                    billname.place(x=10, y=20)

                                    bill_search_butt = Button(billroot, width=10, height=3,
                                                                 font=('georgia', 10, 'bold'), text='Search\n' 'Name',
                                                                 command=search_view)
                                    bill_search_butt.place(x=70, y=60)

                                def get_tree():
                                    global trans_id
                                    itemsaler = transtrv.focus()
                                    sales_items = transtrv.item(itemsaler, "values")


                                    trans_id = sales_items[0]



                                def show_sales():

                                    def update_sales(salesrows):
                                        for row in salesrows:
                                            salestrv.insert('', END, values=row)


                                    salesroot = Tk()
                                    salesroot.geometry('1150x605+189+160')
                                    salesroot.overrideredirect(1)
                                    salesroot.attributes('-topmost', True)



                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    saleswrapper1 = Label(salesroot, width=800, height=50)
                                    saleswrapper1.place(x=0, y=60)

                                    salestrv = ttk.Treeview(saleswrapper1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings",
                                                       height=23)
                                    salestrv.place(x=0, y=0)

                                    salestrv.column("1", anchor=CENTER, stretch=NO, width=180)
                                    salestrv.column("2", anchor=CENTER, stretch=NO, width=180)
                                    salestrv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    salestrv.column("4", anchor=CENTER, stretch=NO, width=200)
                                    salestrv.column("5", anchor=CENTER, stretch=NO, width=200)
                                    salestrv.column("6", anchor=CENTER, stretch=NO, width=200)
                                    #salestrv.column("7", anchor=CENTER, stretch=NO, width=160)

                                    salestrv.heading(1, text="Sales ID")
                                    salestrv.heading(2, text="Transaction ID")
                                    salestrv.heading(3, text="Product ID")
                                    salestrv.heading(4, text="Quantity")
                                    salestrv.heading(5, text="Unit Price")
                                    salestrv.heading(6, text="Total")


                                    cursor.execute("select * from sales where invoice_id='"+trans_id+"'")
                                    salesrows = cursor.fetchall()
                                    for i in range(len(salesrows)):
                                        salesrows[i] = list(salesrows[i])
                                        product_ids = str(salesrows[i][2])
                                        cursor.execute("select name from product where product_id = '"+product_ids+"' ")
                                        spro_ids = cursor.fetchall()
                                        for j in range(len(spro_ids)):
                                            salesrows[i][2] = spro_ids[j][0]
                                    update_sales(salesrows)







                                    salesttframe = Frame(salesroot, width=1150, height=60, bg='cadetblue')
                                    salesttframe.place(x=0, y=0)

                                    salestt2frame = Frame(salesroot, width=1150, height=70, bg='cadetblue')
                                    salestt2frame.place(x=0, y=540)

                                    salestlab = Label(salesttframe, text='Customer Bill', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    salestlab.place(x=0, y=20)

                                    salesbutt10 = Button(salestt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=salesroot.destroy)

                                    salesbutt10.place(x=1057, y=2)

                                    salesbutt11 = Button(salestt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=show_sales)
                                    salesbutt11.place(x=965, y=2)

                                    salesbutt12 = Button(salestt2frame, text='View', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    salesbutt12.place(x=560, y=2)

                                    salesbutt13 = Button(salestt2frame, text='Copy', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    salesbutt13.place(x=467, y=2)

                                    salesbutt14 = Button(salestt2frame, text='Delete', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    salesbutt14.place(x=374, y=2)

                                    salesbutt15 = Button(salestt2frame, text='Edit', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    salesbutt15.place(x=281, y=2)

                                    salesbutt16 = Button(salestt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    salesbutt16.place(x=188, y=2)

                                    salesbutt17 = Button(salestt2frame, text='Clear', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    salesbutt17.place(x=95, y=2)

                                    salesbutt18 = Button(salestt2frame, text='Search', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=None)
                                    salesbutt18.place(x=2, y=2)


                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Customer Bill', font=('times new roman', 19, 'bold'), bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lambda:[get_tree(),show_sales()])
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lookup_transaction)
                                butt18.place(x=2, y=2)

                            chib.after(3000, main_win)

##########################################################################LOSSES###########################################################################################3######

                        def loss():

                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                report = Tk()
                                report.geometry('1150x605+189+160')
                                report.overrideredirect(1)
                                report.attributes('-topmost', True)
                                report.configure(background="white")

                                con = mysql.connect(host='localhost', user='root', password='',
                                                    database='retail-system2')
                                cur = con.cursor()
                                cur.execute(
                                    "SELECT total FROM `write_off`")
                                rows = cur.fetchall()
                                total = 0
                                for i in range(len(rows)):
                                    total = total + rows[i][0]

                                tt2frame = Frame(report, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                total_frame = Frame(report, width=575, height=300)
                                total_frame.place(x=0, y=0)

                                gross_frame = Frame(report, width=575, height=300, bg="floral white")
                                gross_frame.place(x=575, y=0)

                                tot_lab = Label(gross_frame, text="LOSS VALUE",
                                                font=("times new roman", 20, 'bold'), bg="floral white")
                                tot_lab.place(x=190, y=20)

                                yut = main_currency +''+ str(total)

                                tot_lab2 = Label(gross_frame, text=yut,
                                                 font=("times new roman", 40, 'bold'), bg="floral white",
                                                 fg='red')
                                tot_lab2.place(x=160, y=120)

                                date_label = Label(total_frame,
                                                   text="Date From :\n""\n""Date To : ""\n""\n""Store : \n""\nProduct: \n",
                                                   font=("times new roman", 14, 'bold'))
                                date_label.place(x=10, y=20)

                                store1 = Label(total_frame, text="KLIN HORSE ENTERPRISE",
                                               font=("times new roman", 14, 'bold'))
                                store1.place(x=120, y=105)

                                pro1 = Label(total_frame, text="",
                                             font=("times new roman", 14, 'bold'))
                                pro1.place(x=133, y=152)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                width=8,
                                                height=3,
                                                command=report.destroy)
                                butt10.place(x=1057, y=2)

                            chib.after(3000, main_win)

##############################################################################################################################################################
                        def tender():
                            will = Toplevel()
                            will.geometry('750x500+320+150')
                            will.iconbitmap(r'assets/titlelogo.ico')
                            will.resizable(0, 0)

                            def insert():
                                id = willentry.get()
                                name = willentry2.get()

                                if (
                                        name == ''):
                                    messagebox.showinfo("Insert Status", "All Fields Are Required")
                                else:
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                        "insert into tender_type values('" + id + "','" + name + "')")
                                    cursor.execute("commit");
                                    willentry.delete(0, 'end')
                                    willentry2.delete(0, 'end')

                                    messagebox.showinfo("Insert Status", "Inserted")
                                    con.close()
                                    will.destroy()

                            willframe = Frame(will, width=750, height=80, bg="lightblue")
                            willframe.place(x=0, y=0)

                            willlabel = Label(willframe, text="Add Tender Type", font=("open sans", 14), bg="lightblue")
                            willlabel.place(x=0, y=45)

                            willlabel2 = Label(will, text="Tender ID", font=("open sans", 14))
                            willlabel2.place(x=10, y=150)

                            willlabel3 = Label(will, text="Tender Name", font=("open sans", 14))
                            willlabel3.place(x=10, y=250)

                            willentry = Entry(will, width=20, font=("open sans", 14))
                            willentry.place(x=200, y=150)

                            willentry2 = Entry(will, width=20, font=("open sans", 14))
                            willentry2.place(x=200, y=250)

                            willframe2 = Frame(will, width=750, height=80, bg="cadetblue")
                            willframe2.place(x=0, y=421)

                            def closewill():
                                will.destroy()

                            willbut = Button(willframe2, text="Search", font=("open sans", 10), width=15, height=5,
                                             state=DISABLED)
                            willbut.place(x=12, y=2)

                            willbut2 = Button(willframe2, text="Add", font=("open sans", 10), width=15, height=5,
                                              command=insert)
                            willbut2.place(x=160, y=2)

                            willbut3 = Button(willframe2, text="Delete", font=("open sans", 10), width=15, height=5,
                                              state=DISABLED)
                            willbut3.place(x=308, y=2)

                            willbut4 = Button(willframe2, text="Copy", font=("open sans", 10), width=15, height=5,
                                              state=DISABLED)
                            willbut4.place(x=456, y=2)

                            willbut5 = Button(willframe2, text="Cancel", font=("open sans", 10), width=15, height=5,
                                              command=closewill)
                            willbut5.place(x=604, y=2)


####################################################################STOCK_VALUE####################################################################################################
                        def stock_value():
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                report = Tk()
                                report.geometry('1150x605+189+160')
                                report.overrideredirect(1)
                                report.attributes('-topmost', True)
                                report.configure(background="white")

                                con = mysql.connect(host='localhost', user='root', password='',
                                                    database='retail-system2')
                                cur = con.cursor()
                                cur.execute(
                                    "SELECT total_cost FROM `product`")
                                rows = cur.fetchall()
                                total = 0
                                for i in range(len(rows)):
                                    total = total + rows[i][0]

                                tt2frame = Frame(report, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                total_frame = Frame(report, width=575, height=300)
                                total_frame.place(x=0, y=0)

                                gross_frame = Frame(report, width=575, height=300, bg="floral white")
                                gross_frame.place(x=575, y=0)

                                tot_lab = Label(gross_frame, text="STOCK COST VALUE",
                                                font=("times new roman", 20, 'bold'), bg="floral white")
                                tot_lab.place(x=190, y=20)

                                yut = main_currency +''+ str(total)

                                if total <= 125000:
                                    tot_lab2 = Label(gross_frame, text=yut,
                                                 font=("times new roman", 40, 'bold'), bg="floral white",
                                                 fg='red')
                                    tot_lab2.place(x=160, y=120)



                                else:
                                    tot_lab2 = Label(gross_frame, text=yut,
                                                     font=("times new roman", 40, 'bold'), bg="floral white",
                                                     fg='green')
                                    tot_lab2.place(x=160, y=120)

                                date_label = Label(total_frame,
                                                   text="Date From :\n""\n""Date To : ""\n""\n""Store : \n""\nProduct: \n",
                                                   font=("times new roman", 14, 'bold'))
                                date_label.place(x=10, y=20)

                                store1 = Label(total_frame, text="KLIN HORSE ENTERPRISE",
                                               font=("times new roman", 14, 'bold'))
                                store1.place(x=120, y=105)

                                pro1 = Label(total_frame, text="",
                                             font=("times new roman", 14, 'bold'))
                                pro1.place(x=133, y=152)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                width=8,
                                                height=3,
                                                command=report.destroy)
                                butt10.place(x=1057, y=2)

                            chib.after(3000, main_win)


##########################################################GROSS-PROFIT###############################################################################################################

                        def gross():

                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)
                                root.configure(background="white")

                                def get_pro():

                                    proroot = Tk()
                                    proroot.geometry('1150x605+189+160')
                                    proroot.overrideredirect(1)
                                    proroot.attributes('-topmost', True)

                                    def update(rows):
                                        protrv.delete(*protrv.get_children())
                                        for i in rows:
                                            protrv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(proroot, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    protrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                          height=23)
                                    protrv.place(x=0, y=0)

                                    protrv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    protrv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    protrv.heading(1, text="ID")
                                    protrv.heading(2, text="Code")
                                    protrv.heading(3, text="Name")
                                    protrv.heading(4, text="Categroy ID")
                                    protrv.heading(5, text="Sale Price")
                                    protrv.heading(6, text="Unit ID")
                                    protrv.heading(7, text="Unit in Stock")
                                    protrv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    def insert_pro():
                                        global name
                                        name_lab.configure(text='')
                                        category = protrv.focus()
                                        name = protrv.item(category, "values")
                                        name_lab.configure(text=name[2])
                                        proroot.destroy()

                                    cursor.close()

                                    ttframe = Frame(proroot, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(proroot, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=proroot.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=insert_pro)
                                    butt11.place(x=965, y=2)

                                def clear_pro():
                                    name_lab.configure(text='')


                                def main_report():
                                    report = Tk()
                                    report.geometry('1150x605+189+160')
                                    report.overrideredirect(1)
                                    report.attributes('-topmost', True)
                                    report.configure(background="white")

                                    con = mysql.connect(host='localhost', user='root', password='',
                                                        database='retail-system2')
                                    cur = con.cursor()

                                    a = str(from_date.get()) + " 00:00:00"
                                    b = str(to_date.get()) + " 23:59:59"

                                    sample = "3"



                                    cur.execute(
                                    "SELECT total_cost FROM `profitter` WHERE  `date` BETWEEN '" + a + "' AND '" + b + "'")
                                    rows = cur.fetchall()
                                    total = 0
                                    for i in range(len(rows)):
                                        total = total + rows[i][0]




                                    tt2frame = Frame(report, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    total_frame = Frame(report, width=575, height=300)
                                    total_frame.place(x=0, y=0)

                                    gross_frame = Frame(report, width=575, height=300, bg="floral white")
                                    gross_frame.place(x=575, y=0)

                                    tot_lab = Label(gross_frame, text="GROSS PROFIT",
                                                    font=("times new roman", 20, 'bold'), bg="floral white")
                                    tot_lab.place(x=190, y=20)

                                    yut = main_currency +''+ str(total)

                                    tot_lab2 = Label(gross_frame, text=yut,
                                                     font=("times new roman", 40, 'bold'), bg="floral white",
                                                     fg='green')
                                    tot_lab2.place(x=160, y=120)

                                    date_label = Label(total_frame,
                                                       text="Date From :\n""\n""Date To : ""\n""\n""Store : \n""\nProduct: \n",
                                                       font=("times new roman", 14, 'bold'))
                                    date_label.place(x=10, y=20)

                                    date1 = Label(total_frame, text=from_date.get(),
                                                  font=("times new roman", 14, 'bold'))
                                    date1.place(x=120, y=20)

                                    date2 = Label(total_frame, text=to_date.get(),
                                                  font=("times new roman", 14, 'bold'))
                                    date2.place(x=120, y=63)

                                    store1 = Label(total_frame, text="KLIN HORSE ENTERPRISE",
                                                   font=("times new roman", 14, 'bold'))
                                    store1.place(x=120, y=105)

                                    pro1 = Label(total_frame, text="",
                                                 font=("times new roman", 14, 'bold'))
                                    pro1.place(x=133, y=152)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=report.destroy)
                                    butt10.place(x=1057, y=2)

                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='GROSS PROFIT REPORT', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                param_label = Label(root, text="Parameter Values", font=('new times roman', 10, 'bold'),
                                                    bg='white')
                                param_label.place(x=10, y=65)

                                from_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                from_frame.place(x=0, y=90)

                                from_label = Label(from_frame, text="From Date", font=('new times roman', 10),
                                                   bg='white')
                                from_label.place(x=10, y=5)

                                from_date = DateEntry(from_frame, selectmode='', width=61,
                                                      font=('times new roman', 14), justify=LEFT, bd=0,
                                                      date_pattern='y-mm-dd')
                                from_date.place(x=575, y=0)

                                to_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                to_frame.place(x=0, y=120)

                                to_label = Label(to_frame, text="To Date", font=('new times roman', 10),
                                                 bg='white')
                                to_label.place(x=10, y=5)

                                to_date = DateEntry(to_frame, selectmode='', width=61,
                                                    font=('times new roman', 14), justify=LEFT, bd=0,
                                                    date_pattern='y-mm-dd')
                                to_date.place(x=575, y=0)

                                store_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                store_frame.place(x=0, y=150)

                                store_label = Label(store_frame, text="Store", font=('new times roman', 10),
                                                    bg='white')
                                store_label.place(x=10, y=5)

                                store_name_frame = Frame(store_frame, width=575, height=30, bg='white', bd=1,
                                                         relief=RIDGE)
                                store_name_frame.place(x=575, y=0)

                                customer_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                customer_frame.place(x=0, y=180)

                                customer_label = Label(customer_frame, text="Customer", font=('new times roman', 10),
                                                       bg='white')
                                customer_label.place(x=10, y=5)

                                customer_name_frame = Frame(customer_frame, width=575, height=30, bg='white', bd=1,
                                                            relief=RIDGE)
                                customer_name_frame.place(x=575, y=0)

                                get_customer = Button(customer_name_frame, width=1, height=1, text='...', command=None,
                                                      bd=0)
                                get_customer.place(x=540, y=2)

                                customer_cancel = Button(customer_name_frame, width=1, height=1, text='X', bd=0)
                                customer_cancel.place(x=555, y=2)

                                product_from_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                product_from_frame.place(x=0, y=210)

                                product_from_label = Label(product_from_frame, text="Product",
                                                           font=('new times roman', 10),
                                                           bg='white')
                                product_from_label.place(x=10, y=5)

                                product1_name_frame = Frame(product_from_frame, width=575, height=30, bg='white', bd=1,
                                                            relief=RIDGE)
                                product1_name_frame.place(x=575, y=0)

                                get_product1 = Button(product1_name_frame, width=1, height=1, text='...',
                                                      command=get_pro,
                                                      bd=0)
                                get_product1.place(x=540, y=2)

                                product1_cancel = Button(product1_name_frame, width=1, height=1, text='X', bd=0,
                                                         command=clear_pro)
                                product1_cancel.place(x=555, y=2)

                                name_lab = Label(product1_name_frame, text='', font=('times new roman', 12),
                                                 bg='white')
                                name_lab.place(x=0, y=2)

                                report_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                report_frame.place(x=0, y=270)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=main_report)
                                butt11.place(x=965, y=2)

                            chib.after(3000, main_win)


##########################################################EXCHANGE RATES#################################################################################################################

                        def rates():

                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                con = mysql.connect(host='localhost', user='root', password="",
                                                    database="retail-system2")
                                cursor = con.cursor()
                                cursor.execute("select * from rates")
                                all_rates = cursor.fetchall()

                                pula_current = str(all_rates[0][2])
                                rand_current = str(all_rates[1][2])
                                usd_current = str(all_rates[2][2])

                                pula_tender = "pula"
                                rand_tender = "rand"
                                usd_tender = "usd"

                                def insert_rate():
                                    pula_rate.insert(0,pula_current)
                                    rand_rate.insert(0, rand_current)
                                    usd_rate.insert(0, usd_current)

                                def update_rate():

                                    pula = str(float(pula_rate.get()))
                                    rands = str(float(rand_rate.get()))
                                    usd = str(float(usd_rate.get()))


                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()

                                    cursor.execute(
                                        "update rates set actual_rate='"+pula+"' where tender='"+pula_tender+"' ")
                                    cursor.execute(
                                        "update rates set actual_rate='" + rands + "' where tender='" + rand_tender + "' ")
                                    cursor.execute(
                                        "update rates set actual_rate='" + usd + "' where tender='" + usd_tender + "' ")
                                    cursor.execute("commit");
                                    con.close()
                                    root.destroy()

                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                mainframe = Frame(root, width=1150, height=60, bg='floral white')
                                mainframe.place(x=0, y=60)

                                paytypelab = Label(mainframe, text="Pula", font=("georgia", 14), bg="floral white")
                                paytypelab.place(x=10, y=20)

                                expectedlab = Label(mainframe, text="Rand", font=("georgia", 14), bg="floral white")
                                expectedlab.place(x=300, y=20)

                                actuallab = Label(mainframe, text="USD", font=("georgia", 14),
                                                  bg="floral white")
                                actuallab.place(x=620, y=20)

                                main4frame1 = Frame(root, width=300, height=40, bg='white', relief=SUNKEN, bd=3)
                                main4frame1.place(x=0, y=120)

                                pula_rate = Entry(main4frame1, width=29, bd=0, justify=RIGHT,
                                                 font=("times new roman", 14, "bold"))
                                pula_rate.place(x=0, y=0)

                                main4frame2 = Frame(root, width=300, height=40, bg='white', relief=SUNKEN, bd=3)
                                main4frame2.place(x=300, y=120)

                                rand_rate = Entry(main4frame2, width=29, bd=0, justify=RIGHT,
                                                 font=("times new roman", 14, "bold"))
                                rand_rate.place(x=0, y=0)

                                main4frame3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3, bg="white")
                                main4frame3.place(x=600, y=120)

                                usd_rate = Entry(main4frame3, width=29, bd=0, justify=RIGHT,
                                                   font=("times new roman", 14, "bold"))
                                usd_rate.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Exchange Rates', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt18 = Button(tt2frame, text='Compile', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt18.place(x=2, y=2)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=update_rate)
                                butt11.place(x=965, y=2)

                                root.after(10, insert_rate)

                            chib.after(3000, main_win)



                            # Adding File Menu and commands
                        file = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='Employee', menu=file)
                        file.add_command(label='Manage Employee', command=manage_emloyee)
                        file.add_command(label='View Employee', command=view_employee)
                            # file.add_command(label='Save', command=None)
                        file.add_separator()
                            # file.add_command(label='Exit', command=root.destroy)

                            # Adding Edit Menu and commands
                        edit = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='Supplier', menu=edit)
                        edit.add_command(label='View Supplier', command=view_supplier)
                            # edit.add_command(label='Copy', command=None)
                            # edit.add_command(label='Paste', command=None)
                            # edit.add_command(label='Select All', command=None)
                        edit.add_separator()
                        edit.add_command(label='Manage Supplier.', command=manage_supplier)
                            # edit.add_command(label='Find again', command=None)

                            # Adding Product Menu
                        help_ = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='Inventory', menu=help_)
                        help_.add_command(label='View Products', command=view_products)
                        help_.add_separator()
                        help_.add_command(label='Manage Products', command=manage_products)
                        help_.add_command(label='Product Category', command=productcategory)
                        help_.add_command(label='Product Unit', command=productunit)
                        help_.add_command(label='View Purchase Order', command=view_PO)
                        help_.add_command(label='Received Product', command=view_received)
                        help_.add_command(label='Inventory Audit', command=audit)
                        help_.add_command(label='WriteOff', command=writeoffs)

                            # Adding Customer Bill Menu
                        help_ = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='Customer', menu=help_)
                        help_.add_command(label='Add Customer', command=manage_customer)
                        help_.add_command(label='View Customers', command=view_customers)
                        help_.add_command(label='View Customer Bills/Invoices', command=customerbill)


                            # Adding Exit Menu
                        help_ = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='Financials', menu=help_)
                        help_.add_command(label='Exchange Rates', command=rates)
                        help_.add_command(label='Gross Profit', command=gross)
                        help_.add_command(label='Accumulated Losses', command=loss)
                        help_.add_command(label='Value of Stock', command=stock_value)
                        help_.add_command(label='Add Tender Type', command=tender)


                            # display Menu------------------------------->>>>>>>>>>>>>>>>
                        admin.config(menu=menubar)
                        

                        tframe = Frame(admin, width=1328, height=100, bg='white', relief=RIDGE, bd=5)
                        tframe.place(x=10, y=5)

                        logbutt = Button(admin, text="Logout", font=("times new roman", 14, "bold"), command=logout,
                                             width=15, bg='skyblue')
                        logbutt.place(x=20, y=55)

                        imga = ImageTk.PhotoImage(Image.open('assets/user-employee3.png'))
                        c5_label = Label(tframe, image=imga)
                        c5_label.place(x=10, y=10)



                        admin_label = Label(tframe, text=usernameEn.get(), font=("times new roman", 20, "bold"), bg="white")
                        admin_label.place(x=50, y=10)

                        retail_label = Label(tframe, text="Retail Management System",
                                                 font=("times new roman", 30, "bold"), bg="white")
                        retail_label.place(x=450, y=40)

                        tframe2 = Frame(admin, width=1328, height=635, bg='white', relief=RIDGE, bd=5)
                        tframe2.place(x=10, y=103)

                        img2 = ImageTk.PhotoImage(Image.open('assets/background620.jpg'))
                        c2_label = Label(tframe2, image=img2)
                        c2_label.place(x=165, y=0)

                        def receive():

                            con = mysql.connect(host='localhost', user='root', password="",
                                                database="retail-system2")
                            cursor = con.cursor()

                            sql3 = "SELECT product_id FROM product"
                            cursor.execute(sql3)
                            my_product = cursor.fetchall()

                            sql3 = "SELECT employee_id FROM employee"
                            cursor.execute(sql3)
                            my_employee = cursor.fetchall()

                            sql3 = "SELECT supplier_id FROM supplier"
                            cursor.execute(sql3)
                            my_supplier = cursor.fetchall()


                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()

                                def incre_id():
                                    global pap
                                    con = mysql.connect(host='localhost', user="root", password="",
                                                        database="retail-system2")
                                    cur = con.cursor()

                                    sql = "SELECT purchase_order_id FROM purchase_order ORDER BY purchase_order_id DESC LIMIT 1"
                                    cur.execute(sql)
                                    last_id = cur.fetchone()
                                    pap = int(last_id[0]) + 1
                                    fentry4.insert(0, "PO000000"+str(pap))

                                def insert():

                                    orderid = fentry4.get()
                                    date = cal.get()
                                    supplier = fcombo2.get()
                                    reference = fentry.get()
                                    product = fcombo.get()
                                    quantity = fentry2.get()
                                    price = fentry3.get()
                                    employee = str(employee_id[0])
                                    num1 = fentry3.get()
                                    num2 = fentry2.get()
                                    mul = float(price) * float(quantity)
                                    mul2 = str(mul)

                                    if (
                                            orderid == '' or date == '' or supplier == '' or product == '' or quantity == ''):
                                        messagebox.showinfo("Insert Status", "All Fields Are Required")
                                    else:
                                        con = mysql.connect(host='localhost', user='root', password="",
                                                            database="retail-system2")
                                        cursor = con.cursor()
                                        cursor.execute(
                                            "insert into purchase_order(purchase_order_id,product_id,quantity,unit_price,sub_total,supplier_id,order_date,employee_id,reference_number) values('" + orderid + "','" + product + "','" + quantity + "','" + price + "','" + mul2 + "','" + supplier + "','" + date + "','" + employee + "','" + reference + "')")

                                        cursor.execute("commit");
                                        fentry4.delete(0, 'end')
                                        cal.delete(0, 'end')
                                        fcombo2.delete(0, 'end')
                                        fentry.delete(0, 'end')
                                        fcombo.delete(0, 'end')
                                        fentry2.delete(0, 'end')
                                        fentry3.delete(0, 'end')
                                        root.destroy()

                                        messagebox.showinfo("Insert Status", "Inserted")
                                        con.close()
                                        root.destroy()

                                def on_configure(event):
                                    my_canvas.configure(scrollregion=my_canvas.bbox('all'))
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                def update(rows):
                                    for i in rows:
                                        transtrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(root, width=800, height=50)
                                wrapper1.place(x=0, y=300)

                                transtrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",
                                                        height=23)
                                transtrv.place(x=0, y=0)

                                transtrv.column("1", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("2", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("3", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("4", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("5", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("6", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("7", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("8", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("9", anchor=CENTER, stretch=NO, width=130)

                                transtrv.heading(1, text="ID")
                                transtrv.heading(2, text="Product ID")
                                transtrv.heading(3, text="Quantity")
                                transtrv.heading(4, text="Unit Price")
                                transtrv.heading(5, text="Total")
                                transtrv.heading(6, text="Supplier ID")
                                transtrv.heading(7, text="Date")
                                transtrv.heading(8, text="Employee ID")
                                transtrv.heading(9, text="Reference")

                                cursor.execute("select * from purchase_order")
                                rows = cursor.fetchall()
                                for i in range(len(rows)):
                                    rows[i] = list(rows[i])
                                    product_id = str(rows[i][1])
                                    cursor.execute("select name from product where product_id = '"+product_id+"'  ")
                                    ids = cursor.fetchall()
                                    for j in range(len(ids)):
                                        rows[i][1] = ids[j][0]


                                update(rows)


                                cursor.close()

                                def get_supplier():
                                    root = Tk()
                                    root.geometry('1150x605+189+160')
                                    root.overrideredirect(1)
                                    root.attributes('-topmost', True)

                                    def update(rows):
                                        suptrv.delete(*suptrv.get_children())
                                        for i in rows:
                                            suptrv.insert('', 'end', values=i)

                                    def get_supp():
                                        supplier = suptrv.focus()
                                        supplier_main = suptrv.item(supplier, "values")
                                        fcombo2.delete(0, 'end')
                                        fcombo2.insert(0,supplier_main[0])
                                        root.destroy()


                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(root, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    suptrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6), show="headings",
                                                          height=23)
                                    suptrv.place(x=0, y=0)

                                    suptrv.column("1", anchor=CENTER, stretch=NO, width=190)
                                    suptrv.column("2", anchor=CENTER, stretch=NO, width=190)
                                    suptrv.column("3", anchor=CENTER, stretch=NO, width=190)
                                    suptrv.column("4", anchor=CENTER, stretch=NO, width=190)
                                    suptrv.column("5", anchor=CENTER, stretch=NO, width=190)
                                    suptrv.column("6", anchor=CENTER, stretch=NO, width=190)

                                    suptrv.heading(1, text="Supplier ID")
                                    suptrv.heading(2, text="Supplier Code")
                                    suptrv.heading(3, text="Name")
                                    suptrv.heading(4, text="Contact")
                                    suptrv.heading(5, text="Email")
                                    suptrv.heading(6, text="Address")

                                    cursor.execute("select * from supplier")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    cursor.close()

                                    def lookup_products():
                                        productroot = Tk()
                                        productroot.geometry('250x150+600+300')
                                        productroot.title('Lookup Products')
                                        productroot.attributes('-topmost', True)
                                        productroot.iconbitmap(r'assets/titlelogo.ico')

                                        def search_view():
                                            def update(rows):
                                                suptrv.delete(*suptrv.get_children())
                                                for i in rows:
                                                    suptrv.insert('', 'end', values=i)

                                            mydb = mysql.connect(host='localhost', user="root", password="",
                                                                 database="retail-system2")
                                            cursor = mydb.cursor()

                                            cursor.execute(
                                                "select * from supplier where supplier_name like '%" + productname.get() + "%'")
                                            rows = cursor.fetchall()

                                            update(rows)
                                            productroot.destroy()

                                        productname = Entry(productroot, width=19, font=('georgia', 14))
                                        productname.place(x=10, y=20)

                                        product_search_butt = Button(productroot, width=10, height=3,
                                                                     font=('georgia', 10, 'bold'),
                                                                     text='Search\n' 'Name', command=search_view)
                                        product_search_butt.place(x=70, y=60)

                                    ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Supplier', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=get_supp)
                                    butt11.place(x=965, y=2)

                                    butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt12.place(x=560, y=2)

                                    butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt13.place(x=467, y=2)

                                    butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt14.place(x=374, y=2)

                                    butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt15.place(x=281, y=2)

                                    butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt16.place(x=188, y=2)

                                    butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt17.place(x=95, y=2)

                                    butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=lookup_products)
                                    butt18.place(x=2, y=2)




                                def get_product():
                                    root = Tk()
                                    root.geometry('1150x605+189+160')
                                    root.overrideredirect(1)
                                    root.attributes('-topmost', True)

                                    def update(rows):
                                        trv.delete(*trv.get_children())
                                        for i in rows:
                                            trv.insert('', 'end', values=i)

                                    def get_pro():
                                        pro = trv.focus()
                                        pro_main = trv.item(pro, "values")
                                        fcombo.delete(0, 'end')
                                        fcombo.insert(0,pro_main[0])
                                        root.destroy()

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(root, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                       height=23)
                                    trv.place(x=0, y=0)

                                    trv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    trv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    trv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    trv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    trv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    trv.heading(1, text="ID")
                                    trv.heading(2, text="Code")
                                    trv.heading(3, text="Name")
                                    trv.heading(4, text="Categroy ID")
                                    trv.heading(5, text="Sale Price")
                                    trv.heading(6, text="Unit ID")
                                    trv.heading(7, text="Unit in Stock")
                                    trv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    cursor.close()

                                    def lookup_products():
                                        productroot = Tk()
                                        productroot.geometry('250x150+600+300')
                                        productroot.title('Lookup Products')
                                        productroot.attributes('-topmost', True)
                                        productroot.iconbitmap(r'assets/titlelogo.ico')

                                        def search_view():
                                            def update(rows):
                                                trv.delete(*trv.get_children())
                                                for i in rows:
                                                    trv.insert('', 'end', values=i)

                                            mydb = mysql.connect(host='localhost', user="root", password="",
                                                                 database="retail-system2")
                                            cursor = mydb.cursor()

                                            cursor.execute(
                                                "select * from product where name like '%" + productname.get() + "%'")
                                            rows = cursor.fetchall()

                                            update(rows)
                                            productroot.destroy()

                                        productname = Entry(productroot, width=19, font=('georgia', 14))
                                        productname.place(x=10, y=20)

                                        product_search_butt = Button(productroot, width=10, height=3,
                                                                     font=('georgia', 10, 'bold'),
                                                                     text='Search\n' 'Name', command=search_view)
                                        product_search_butt.place(x=70, y=60)

                                    ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=root.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=get_pro)
                                    butt11.place(x=965, y=2)

                                    butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt12.place(x=560, y=2)

                                    butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt13.place(x=467, y=2)

                                    butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt14.place(x=374, y=2)

                                    butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt15.place(x=281, y=2)

                                    butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt16.place(x=188, y=2)

                                    butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    state=DISABLED)
                                    butt17.place(x=95, y=2)

                                    butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=lookup_products)
                                    butt18.place(x=2, y=2)


                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Purchase Order', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=insert)
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt18.place(x=2, y=2)

                                wrapper2=Frame(root,width=1150, height=240)


                                wrapper2.place(x=0,y=60)

                                my_canvas= Canvas(wrapper2,width=1150,height=240)
                                my_canvas.place(x=0,y=0)

                                frame=tkinter.Frame(my_canvas,width=1150,height=360)
                                frame.bind('<Configure>', on_configure)
                                my_canvas.create_window(0, 0, window=frame)

                                scrolly = tkinter.Scrollbar(wrapper2, command=my_canvas.yview)
                                scrolly.place(relx=1, rely=0, relheight=1,anchor='ne')
                                my_canvas.configure(yscrollcommand=scrolly.set)


                                f1 = Frame(frame, width=1130, height=28, bg="white")
                                f1.place(x=0, y=0)

                                fl1 = Label(f1, text="Product Purchase Number", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl1.place(x=40)

                                fentry4 = Entry(f1, font=('times new roman', 16), width=58)
                                fentry4.place(x=485)

                                f2 = Frame(frame, width=1130, height=28, bg='white')
                                f2.place(x=0, y=30)

                                fl2 = Label(f2, text="Receipt Date", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl2.place(x=40)

                                cal = DateEntry(f2, selectmode='day', width=69,
                                                font=('times new roman', 14), justify=LEFT,date_pattern="y-mm-dd")
                                cal.place(x=485, y=2)

                                f3 = Frame(frame, width=1130, height=28, bg='white')
                                f3.place(x=0, y=60)

                                fl3 = Label(f3, text="Supplier", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl3.place(x=40)

                                fcombo2 = Entry(f3 , width=20, font=("open sans", 16))
                                fcombo2.place(x=485)

                                get_supplier = Button(f3, width=1, height=1, text='...',command= get_supplier)
                                get_supplier.place(x=1090)

                                supplier_cancel = Button(f3, width=1, height=1, text='X')
                                supplier_cancel.place(x=1110)

                                f4 = Frame(frame, width=1130, height=28, bg='white')
                                f4.place(x=0, y=90)

                                fl2 = Label(f4, text="Reference Number", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl2.place(x=40)

                                fentry = Entry(f4, font=('times new roman', 16), width=58)
                                fentry.place(x=485, y=2)

                                f5 = Frame(frame, width=1130, height=28, bg='white')
                                f5.place(x=0, y=120)

                                fl3 = Label(f5, text="Product ID", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl3.place(x=40)

                                fcombo = Entry(f5, width=20, font=("open sans", 16))
                                fcombo.place(x=485)

                                product_butt = Button(f5, width=1, height=1, text='...',command=get_product)
                                product_butt.place(x=1090)

                                product_cancel = Button(f5, width=1, height=1, text='X')
                                product_cancel.place(x=1110)

                                f6 = Frame(frame, width=1130, height=28, bg='white')
                                f6.place(x=0, y=150)

                                fl4 = Label(f6, text="Quantity", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl4.place(x=40)

                                fentry2 = Entry(f6, font=('times new roman', 16), width=58)
                                fentry2.place(x=485, y=2)

                                f7 = Frame(frame, width=1130, height=28, bg="white")
                                f7.place(x=0, y=180)

                                fl5 = Label(f7, text="Unit Price", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl5.place(x=40)

                                fentry3 = Entry(f7, font=('times new roman', 16), width=58)
                                fentry3.place(x=485)

                                f8 = Frame(frame, width=1130, height=28, bg="white")
                                f8.place(x=0, y=210)

                                fl6 = Label(f8, text="Employee ID", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl6.place(x=40)


                                f9 = Frame(frame, width=1130, height=28, bg="white")
                                f9.place(x=0, y=240)

                                fl7 = Label(f9, text="Supervisor", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl7.place(x=40)

                                fentry7 = Entry(f6, font=('times new roman', 16), width=58)
                                #fentry7.place(x=485)

                                f10 = Frame(frame, width=1130, height=28, bg="white")
                                f10.place(x=0, y=270)

                                fl8 = Label(f10, text="Receipt Date", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl8.place(x=40)

                                root.after(10, incre_id)





                            chib.after(3000, main_win)


##################################################################################GROSS-PROFIT########################################################################
                        def report():

                                # splash.destroy()
                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                        range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)
                                root.configure(background="white")

                                def get_pro():

                                    proroot = Tk()
                                    proroot.geometry('1150x605+189+160')
                                    proroot.overrideredirect(1)
                                    proroot.attributes('-topmost', True)

                                    def update(rows):
                                        protrv.delete(*protrv.get_children())
                                        for i in rows:
                                            protrv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(proroot, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    protrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                       height=23)
                                    protrv.place(x=0, y=0)

                                    protrv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    protrv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    protrv.heading(1, text="ID")
                                    protrv.heading(2, text="Code")
                                    protrv.heading(3, text="Name")
                                    protrv.heading(4, text="Categroy ID")
                                    protrv.heading(5, text="Sale Price")
                                    protrv.heading(6, text="Unit ID")
                                    protrv.heading(7, text="Unit in Stock")
                                    protrv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    def insert_pro():
                                        global name
                                        name_lab.configure(text='')
                                        category = protrv.focus()
                                        name = protrv.item(category, "values")
                                        name_lab.configure(text=name[2])
                                        proroot.destroy()



                                    cursor.close()

                                    ttframe = Frame(proroot, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(proroot, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=proroot.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=insert_pro)
                                    butt11.place(x=965, y=2)

                                def clear_pro():
                                    name_lab.configure(text='')

                                def clear_pro2():
                                    name_lab2.configure(text='')


                                def get_pro2():

                                    proroot = Tk()
                                    proroot.geometry('1150x605+189+160')
                                    proroot.overrideredirect(1)
                                    proroot.attributes('-topmost', True)

                                    def update(rows):
                                        protrv.delete(*protrv.get_children())
                                        for i in rows:
                                            protrv.insert('', 'end', values=i)

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    wrapper1 = Label(proroot, width=800, height=50)
                                    wrapper1.place(x=0, y=60)

                                    protrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",
                                                       height=23)
                                    protrv.place(x=0, y=0)

                                    protrv.column("1", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("2", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("3", anchor=CENTER, stretch=NO, width=180)
                                    protrv.column("4", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("5", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("6", anchor=CENTER, stretch=NO, width=120)
                                    protrv.column("7", anchor=CENTER, stretch=NO, width=146)
                                    protrv.column("8", anchor=CENTER, stretch=NO, width=150)

                                    protrv.heading(1, text="ID")
                                    protrv.heading(2, text="Code")
                                    protrv.heading(3, text="Name")
                                    protrv.heading(4, text="Categroy ID")
                                    protrv.heading(5, text="Sale Price")
                                    protrv.heading(6, text="Unit ID")
                                    protrv.heading(7, text="Unit in Stock")
                                    protrv.heading(8, text="Discount Percentage")

                                    cursor.execute("select * from product")
                                    rows = cursor.fetchall()
                                    update(rows)

                                    def insert_pro2():
                                        global name2
                                        name_lab2.configure(text='')
                                        category = protrv.focus()
                                        name2 = protrv.item(category, "values")
                                        name_lab2.configure(text=name2[2])
                                        proroot.destroy()

                                    cursor.close()

                                    ttframe = Frame(proroot, width=1150, height=60, bg='cadetblue')
                                    ttframe.place(x=0, y=0)

                                    tt2frame = Frame(proroot, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    tlab = Label(ttframe, text='Product', font=('times new roman', 19, 'bold'),
                                                 bg='cadetblue')
                                    tlab.place(x=0, y=20)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=proroot.destroy)
                                    butt10.place(x=1057, y=2)

                                    butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                    height=3,
                                                    command=insert_pro2)
                                    butt11.place(x=965, y=2)



                                def main_report():
                                    report = Tk()
                                    report.geometry('1150x605+189+160')
                                    report.overrideredirect(1)
                                    report.attributes('-topmost', True)
                                    report.configure(background="white")

                                    con = mysql.connect(host='localhost', user='root', password='',
                                                        database='retail-system2')
                                    cur = con.cursor()

                                    a = str(from_date.get()) + " 00:00:00"
                                    b = str(to_date.get()) + " 23:59:59"

                                    sample = "3"
                                    try:
                                        cur.execute(
                                            "SELECT sub_total FROM `sales` WHERE `product_id` BETWEEN '"+name[0]+"' AND '"+name2[0]+"' AND `date` BETWEEN '"+ a +"' AND '"+ b +"'")
                                        rows = cur.fetchall()
                                    except:
                                        cur.execute( "SELECT sub_total FROM `sales` WHERE `date` BETWEEN '"+ a +"' AND '"+ b +"'")
                                        rows = cur.fetchall()
                                    total = 0
                                    for i in range(len(rows)):
                                        total = total + rows[i][0]


                                    tt2frame = Frame(report, width=1150, height=70, bg='cadetblue')
                                    tt2frame.place(x=0, y=540)

                                    total_frame = Frame(report, width=575, height=300)
                                    total_frame.place(x=0, y=0)

                                    gross_frame = Frame(report, width=575, height=300, bg="floral white")
                                    gross_frame.place(x=575,y=0)

                                    tot_lab = Label(gross_frame, text="TOTAL SALES",
                                                  font=("times new roman", 20, 'bold'), bg="floral white")
                                    tot_lab.place(x=190, y=20)

                                    yut = main_currency +''+ str(total)

                                    tot_lab2 = Label(gross_frame, text=yut,
                                                    font=("times new roman", 40, 'bold'), bg="floral white", fg='green')
                                    tot_lab2.place(x=160, y=120)

                                    date_label = Label(total_frame, text="Date From :\n""\n""Date To : ""\n""\n""Store : \n""\nFrom Product: \n""\nTo Product: ", font=("times new roman",14,'bold'))
                                    date_label.place(x=10, y=20)

                                    date1 = Label(total_frame, text=from_date.get(), font=("times new roman",14,'bold'))
                                    date1.place(x=120, y=20)

                                    date2 = Label(total_frame, text=to_date.get(),
                                                  font=("times new roman", 14, 'bold'))
                                    date2.place(x=120, y=63)

                                    butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'),
                                                    width=8,
                                                    height=3,
                                                    command=report.destroy)
                                    butt10.place(x=1057, y=2)

                                    store1 = Label(total_frame, text="KLIN HORSE ENTERPRISE",
                                                  font=("times new roman", 14, 'bold'))
                                    store1.place(x=120, y=105)

                                    pro1 = Label(total_frame, text=name[2],
                                                   font=("times new roman", 14, 'bold'))
                                    pro1.place(x=133, y=152)

                                    pro2 = Label(total_frame, text=name2[2],
                                                   font=("times new roman", 14, 'bold'))
                                    pro2.place(x=130, y=195)





                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Sales Report', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                param_label = Label(root, text="Parameter Values", font=('new times roman',10,'bold'), bg='white')
                                param_label.place(x=10, y=65)

                                from_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                from_frame.place(x=0, y=90)

                                from_label = Label(from_frame, text="From Date", font=('new times roman', 10),
                                                    bg='white')
                                from_label.place(x=10, y=5)

                                from_date = DateEntry(from_frame, selectmode='', width=61,
                                                     font=('times new roman', 14), justify=LEFT, bd=0,
                                                     date_pattern='y-mm-dd')
                                from_date.place(x=575, y=0)

                                to_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                to_frame.place(x=0, y=120)

                                to_label = Label(to_frame, text="To Date", font=('new times roman', 10),
                                                   bg='white')
                                to_label.place(x=10, y=5)

                                to_date = DateEntry(to_frame, selectmode='', width=61,
                                                      font=('times new roman', 14), justify=LEFT, bd=0,
                                                      date_pattern='y-mm-dd')
                                to_date.place(x=575, y=0)

                                store_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                store_frame.place(x=0, y=150)

                                store_label = Label(store_frame, text="Store", font=('new times roman', 10),
                                                   bg='white')
                                store_label.place(x=10, y=5)

                                store_name_frame = Frame(store_frame, width=575, height=30, bg='white', bd=1, relief=RIDGE)
                                store_name_frame.place(x=575,y=0)

                                customer_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                customer_frame.place(x=0, y=180)

                                customer_label = Label(customer_frame, text="Customer", font=('new times roman', 10),
                                                   bg='white')
                                customer_label.place(x=10, y=5)

                                customer_name_frame = Frame(customer_frame, width=575, height=30, bg='white', bd=1,
                                                         relief=RIDGE)
                                customer_name_frame.place(x=575, y=0)

                                get_customer = Button(customer_name_frame, width=1, height=1, text='...', command=None, bd=0)
                                get_customer.place(x=540, y=2)

                                customer_cancel = Button(customer_name_frame, width=1, height=1, text='X', bd=0)
                                customer_cancel.place(x=555, y=2)

                                product_from_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                product_from_frame.place(x=0, y=210)

                                product_from_label = Label(product_from_frame, text="From Product", font=('new times roman', 10),
                                                   bg='white')
                                product_from_label.place(x=10, y=5)

                                product1_name_frame = Frame(product_from_frame, width=575, height=30, bg='white', bd=1,
                                                            relief=RIDGE)
                                product1_name_frame.place(x=575, y=0)

                                get_product1 = Button(product1_name_frame, width=1, height=1, text='...', command=get_pro,
                                                      bd=0)
                                get_product1.place(x=540, y=2)

                                product1_cancel = Button(product1_name_frame, width=1, height=1, text='X', bd=0, command=clear_pro)
                                product1_cancel.place(x=555, y=2)

                                product_to_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                product_to_frame.place(x=0, y=240)

                                product2_name_frame = Frame(product_to_frame, width=575, height=30, bg='white', bd=1,
                                                            relief=RIDGE)
                                product2_name_frame.place(x=575, y=0)

                                get_product2 = Button(product2_name_frame, width=1, height=1, text='...', command=get_pro2,
                                                      bd=0)
                                get_product2.place(x=540, y=2)

                                product2_cancel = Button(product2_name_frame, width=1, height=1, text='X', bd=0, command=clear_pro2)
                                product2_cancel.place(x=555, y=2)

                                name_lab = Label(product1_name_frame, text='', font=('times new roman', 12),
                                                 bg='white')
                                name_lab.place(x=0, y=2)

                                name_lab2 = Label(product2_name_frame, text='', font=('times new roman', 12),
                                                 bg='white')
                                name_lab2.place(x=0, y=2)

                                product_to_label = Label(product_to_frame, text="To Product",
                                                           font=('new times roman', 10),
                                                           bg='white')
                                product_to_label.place(x=10, y=5)

                                report_frame = Frame(root, width=1150, height=30, bg='white', bd=1, relief=RIDGE)
                                report_frame.place(x=0, y=270)

                                report_label = Label(report_frame, text="Report By",
                                                           font=('new times roman', 10),
                                                           bg='white')
                                report_label.place(x=10, y=5)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=main_report)
                                butt11.place(x=965, y=2)




                            chib.after(3000, main_win)


####################################################################################PRODUCT-RECEIVE###################################################################
                        def send():


                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()

                                def incre_idPO():
                                    global papPO
                                    con = mysql.connect(host='localhost', user="root", password="",
                                                        database="retail-system2")
                                    cur = con.cursor()

                                    sql = "SELECT purchase_order_id FROM purchase_order ORDER BY purchase_order_id DESC LIMIT 1"
                                    cur.execute(sql)
                                    last_id = cur.fetchone()
                                    papPO = str(last_id[0])
                                    fentry4.insert(0, "PO000000"+papPO)

                                def searchPO():

                                    if (fentry4.get() == ''):
                                        messagebox.showinfo("Search Status", "Purchase Order is Required")
                                        root.destroy()
                                    else:

                                        fentry8.delete(0,'end')
                                        fentry.delete(0, 'end')
                                        fentry5.delete(0, 'end')
                                        fentry2.delete(0, 'end')
                                        fentry6.delete(0, 'end')
                                        fentry7.delete(0, 'end')

                                        con = mysql.connect(host='localhost', user='root', password="",
                                                            database="retail-system2")
                                        cursor = con.cursor()
                                        cursor.execute("select * from purchase_order where purchase_order_id='" + papPO + "'")
                                        rows = cursor.fetchall();

                                        for row in rows:
                                            fentry8.insert(0, row[1])
                                            fentry.insert(0, row[2])
                                            fentry5.insert(0, row[3])
                                            fentry2.insert(0, row[4])
                                            fentry6.insert(0, row[5])
                                            fentry7.insert(0, row[8])

                                        con.close()

                                def insert():
                                    global price, quantity, product

                                    orderid = papPO
                                    date = cal.get()
                                    product = fentry8.get()
                                    quantity = fentry.get()
                                    price = fentry5.get()
                                    total = fentry2.get()
                                    reference = fentry7.get()
                                    supplier = fentry6.get()
                                    employee = str(employee_id[0])

                                    if (
                                            price == '' or date == '' or supplier == '' or product == '' or quantity == ''):
                                        received_root.destroy
                                        messagebox.showinfo("Insert Status", "All Fields Are Required")

                                    else:
                                        try:
                                            con = mysql.connect(host='localhost', user='root', password="",
                                                                database="retail-system2")
                                            cursor = con.cursor()
                                            cursor.execute(
                                                "insert into receive_product values('" + orderid + "','" + product + "','" + quantity + "','" + price + "','" + total + "','" + supplier + "','" + date + "','" + employee + "','" + reference + "') ")

                                            cursor.execute("commit");
                                            receival = "Goods Received"
                                            cumulative = "100"
                                            cursor.execute(
                                                "insert into inventory_audit values('" + product + "', '" + receival + "', '" + quantity + "', '" + total + "', '" + cumulative + "', '" + date + "' )  ")
                                            cursor.execute("commit");
                                            cursor.execute(
                                                "update product set unit_in_stock= unit_in_stock + '" + quantity + "', cost_price = '" + price + "', diff_cost= unit_price -'" + price + "' where product_id='" + product + "'")
                                            cursor.execute("commit");
                                            con.close()

                                            fentry8.delete(0, 'end')
                                            fentry.delete(0, 'end')
                                            fentry5.delete(0, 'end')
                                            fentry2.delete(0, 'end')
                                            fentry6.delete(0, 'end')
                                            fentry7.delete(0, 'end')

                                            messagebox.showinfo("Insert Status", "  Inserted   ")


                                        except Exception as es:
                                            received_root.destroy()
                                            messagebox.showerror('Error', f'Error due to: {str(es)}')



                                def decrease():

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()

                                    cursor.execute(
                                        "update product set total_cost = unit_in_stock * '" + price + "' where product_id='" + product + "' ")
                                    cursor.execute("commit");

                                    con.close()




                                def on_configure(event):
                                    my_canvas.configure(scrollregion=my_canvas.bbox('all'))
                                received_root = Tk()
                                received_root.geometry('1150x605+189+160')
                                received_root.overrideredirect(1)
                                received_root.attributes('-topmost', True)


                                def update(rows):
                                    for i in rows:
                                        transtrv.insert('', 'end', values=i)

                                mydb = mysql.connect(host='localhost', user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()

                                wrapper1 = Label(received_root, width=800, height=50)
                                wrapper1.place(x=0, y=300)

                                transtrv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",
                                                        height=23)
                                transtrv.place(x=0, y=0)

                                transtrv.column("1", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("2", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("3", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("4", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("5", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("6", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("7", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("8", anchor=CENTER, stretch=NO, width=130)
                                transtrv.column("9", anchor=CENTER, stretch=NO, width=130)

                                transtrv.heading(1, text="ID")
                                transtrv.heading(2, text="Product ID")
                                transtrv.heading(3, text="Quantity")
                                transtrv.heading(4, text="Unit Price")
                                transtrv.heading(5, text="Total")
                                transtrv.heading(6, text="Supplier ID")
                                transtrv.heading(7, text="Date")
                                transtrv.heading(8, text="Employee ID")
                                transtrv.heading(9, text="Reference")

                                cursor.execute("select * from receive_product")
                                rows = cursor.fetchall()
                                for i in range(len(rows)):
                                    rows[i] = list(rows[i])
                                    product_id = str(rows[i][1])
                                    cursor.execute("select name from product where product_id = '"+product_id+"'  ")
                                    ids = cursor.fetchall()
                                    for j in range(len(ids)):
                                        rows[i][1] = ids[j][0]


                                update(rows)

                                cursor.close()




                                ttframe = Frame(received_root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                tt2frame = Frame(received_root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Receive Product', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=received_root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=lambda :[insert(),decrease()])
                                butt11.place(x=965, y=2)

                                butt12 = Button(tt2frame, text='View', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt12.place(x=560, y=2)

                                butt13 = Button(tt2frame, text='Copy', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt13.place(x=467, y=2)

                                butt14 = Button(tt2frame, text='Delete', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt14.place(x=374, y=2)

                                butt15 = Button(tt2frame, text='Edit', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt15.place(x=281, y=2)

                                butt16 = Button(tt2frame, text='New', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt16.place(x=188, y=2)

                                butt17 = Button(tt2frame, text='Clear', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt17.place(x=95, y=2)

                                butt18 = Button(tt2frame, text='Search', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                state=DISABLED)
                                butt18.place(x=2, y=2)

                                wrapper2=Frame(received_root,width=1150, height=240)


                                wrapper2.place(x=0,y=60)

                                my_canvas= Canvas(wrapper2,width=1150,height=240)
                                my_canvas.place(x=0,y=0)

                                frame=tkinter.Frame(my_canvas,width=1150,height=350)
                                frame.bind('<Configure>', on_configure)
                                my_canvas.create_window(0, 0, window=frame)



                                scrolly = tkinter.Scrollbar(wrapper2, command=my_canvas.yview)
                                scrolly.place(relx=1, rely=0, relheight=1,anchor='ne')
                                my_canvas.configure(yscrollcommand=scrolly.set)

                                f1=Frame(frame,width=1130, height=28,bg="white")
                                f1.place(x=0,y=0)

                                fl1=Label(f1,text="Purchase Order Number",bg='lightblue',font=('times new roman',14,'bold'),width=40)
                                fl1.place(x=40)

                                fentry4 = Entry(f1, font=('times new roman', 16), width=40)
                                fentry4.place(x=485, y=2)

                                fb = Button(f1, width=1, height=1, text='...', command=searchPO)
                                fb.place(x=1090)

                                fbcancel = Button(f1, width=1, height=1, text='X')
                                fbcancel.place(x=1110)

                                f2 = Frame(frame, width=1130, height=28,bg='white')
                                f2.place(x=0, y=30)



                                fl2 = Label(f2, text="Received Date", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl2.place(x=40)

                                #fentry9 = Entry(f2, font=('times new roman', 16), width=58)
                                #fentry9.place(x=485, y=2)

                                cal=DateEntry(f2,selectmode='day',width=69,font=('times new roman',14),justify=LEFT,
                                              date_pattern="y-mm-dd")
                                cal.place(x=485,y=2)

                                f3 = Frame(frame, width=1130, height=28,bg='white')
                                f3.place(x=0, y=60)

                                fl3 = Label(f3, text="Product ID", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl3.place(x=40)

                                fentry8 = Entry(f3, font=('times new roman', 16), width=58)
                                fentry8.place(x=485, y=2)



                                f4 = Frame(frame, width=1130, height=28,bg='white')
                                f4.place(x=0, y=90)

                                fl2 = Label(f4, text="Quantity", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl2.place(x=40)

                                fentry = Entry(f4,font=('times new roman',16),width=58)
                                fentry.place(x=485,y=2)

                                f5 = Frame(frame, width=1130, height=28,bg='white')
                                f5.place(x=0, y=120)

                                fl3 = Label(f5, text="Unit Price", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl3.place(x=40)

                                fentry5 = Entry(f5, font=('times new roman', 16), width=58)
                                fentry5.place(x=485, y=2)


                                f6 = Frame(frame, width=1130, height=28,bg='white')
                                f6.place(x=0, y=150)

                                fl4 = Label(f6, text="Sub-Total", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl4.place(x=40)

                                fentry2 = Entry(f6, font=('times new roman', 16), width=58)
                                fentry2.place(x=485, y=2)

                                f7 = Frame(frame, width=1130, height=28,bg="white")
                                f7.place(x=0, y=180)

                                fl5 = Label(f7, text="Reference Number", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl5.place(x=40)

                                fentry7 = Entry(f7, font=('times new roman', 16), width=58)
                                fentry7.place(x=485, y=2)

                                f8 = Frame(frame, width=1130, height=28,bg="white")
                                f8.place(x=0, y=210)

                                fl6 = Label(f8, text="Supplier ID", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl6.place(x=40)

                                fentry6 = Entry(f8, font=('times new roman', 16), width=58)
                                fentry6.place(x=485, y=2)

                                f9 = Frame(frame, width=1130, height=28,bg="white")
                                f9.place(x=0, y=240)

                                fl7 = Label(f9, text="Supervisor", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl7.place(x=40)


                                f10 = Frame(frame, width=1130, height=28,bg="white")
                                f10.place(x=0, y=270)

                                fl8 = Label(f10, text="Receipt Date", bg='lightblue',
                                            font=('times new roman', 14, 'bold'), width=40)
                                fl8.place(x=40)

                                fentry10 = Entry(f10, font=('times new roman', 16), width=10)
                                fentry10.place(x=485, y=2)

                                received_root.after(10,incre_idPO)





                            chib.after(3000, main_win)

                        def banking():

                            chib = Toplevel()
                            chib.title('WW')
                            chib.geometry('140x50+500+400')
                            chib.resizable(0, 0)
                            chib.overrideredirect(1)
                            chib.attributes('-topmost', True)

                            frameCnt = 8
                            frames = [PhotoImage(file='assets/loading-gif2.gif', format='gif -index %i' % (i)) for i in
                                      range(frameCnt)]

                            def update(ind):
                                frame = frames[ind]
                                ind += 1
                                if ind == frameCnt:
                                    ind = 0
                                label.configure(image=frame)
                                chib.after(100, update, ind)

                            label = Label(chib)
                            label.place(x=0)
                            chib.after(0, update, 0)

                            label2 = Label(chib, text="Please Wait...", font=("times new roman", 12))
                            label2.place(x=55, y=15)

                            def main_win():
                                chib.destroy()
                                root = Tk()
                                root.geometry('1150x605+189+160')
                                root.overrideredirect(1)
                                root.attributes('-topmost', True)

                                def data_cash():
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "cash"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total=0
                                    for i in range(len(data)):
                                        total = total + data[i][0]
                                    total_cash = main_currency + str(" {:.2f}".format(total))

                                    cash_expected.configure(text=total_cash)



                                def data_eco():
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "ecocash"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total=0
                                    for i in range(len(data)):
                                        total = total + data[i][0]
                                    total_eco = main_currency + str(" {:.2f}".format(total))

                                    eco_expected.configure(text=total_eco)


                                def data_nmb():
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "NMB"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total=0
                                    for i in range(len(data)):
                                        total = total + data[i][0]
                                    total_nmb = main_currency + str(" {:.2f}".format(total))

                                    nmb_expected.configure(text=total_nmb)

                                def data_usd():
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "USD"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total=0
                                    for i in range(len(data)):
                                        total = total + data[i][0]
                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()



                                    total_usd = main_currency + str(" {:.2f}".format(total))

                                    usd_expected.configure(text=total_usd)

                                def data_rand():
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "rand"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total=0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")


                                    total_rand = main_currency + str(" {:.2f}".format(total))

                                    rand_expected.configure(text=total_rand)

                                def data_zb():
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "ZB"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total=0
                                    for i in range(len(data)):
                                        total = total + data[i][0]
                                    total_zb = main_currency + str(" {:.2f}".format(total))

                                    zb_expected.configure(text=total_zb)

                                def data_total():
                                    global total_expected_amount
                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total_expected_amount=0
                                    for i in range(len(data)):
                                        total_expected_amount = total_expected_amount + data[i][0]
                                    total_total = main_currency + str(" {:.2f}".format(total_expected_amount))

                                    total_expected.configure(text=total_total)

                                def cash():
                                    global cash_difference

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "cash"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total = 0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    cash_difference = float(total) - float(cash_actual.get())

                                    try:
                                        cash_diff.config(
                                            text=main_currency +" {:,.2f}".format(float(cash_difference)))


                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')
                                        root.destroy()


                                def ecocash():
                                    global eco_difference

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "ecocash"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total = 0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    eco_difference = float(total) - float(eco_actual.get())

                                    try:
                                        eco_diff.config(
                                            text=main_currency+" {:,.2f}".format(float(eco_difference)))
                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')
                                        root.destroy()


                                def Banco():
                                    global nmb_difference

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "NMB"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total = 0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    nmb_difference = float(total) - float(nmb_actual.get())

                                    try:
                                        nmb_diff.config(
                                            text=main_currency+" {:,.2f}".format(float(nmb_difference)))
                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')
                                        root.destroy()

                                def USD():
                                    global usd_difference

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "USD"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total = 0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    cursor.execute(
                                        "Select change_amount from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'")
                                    datausd = cursor.fetchall()

                                    totalusd = 0
                                    for j in range(len(datausd)):
                                        totalusd = totalusd + datausd[j][0]

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from rates")
                                    all_rates = cursor.fetchall()

                                    pula_current = str(all_rates[0][2])
                                    rand_current = str(all_rates[1][2])
                                    usd_current = float(all_rates[2][2])
                                    usd = float(usd_actual.get()) * float(usd_current)
                                    usd_difference = float(total) - float(usd)



                                    try:
                                        usd_diff.config(
                                            text=main_currency+" {:,.2f}".format(float(usd_difference)))
                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')
                                        root.destroy()

                                def rand():
                                    global rand_difference

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "rand"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total = 0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from rates")
                                    all_rates = cursor.fetchall()

                                    pula_current = str(all_rates[0][2])
                                    rand_current = str(all_rates[1][2])
                                    usd_current = float(all_rates[2][2])
                                    rands = float(rand_actual.get()) * float(rand_current)
                                    rand_difference = float(total) - float(rands)

                                    try:
                                        rand_diff.config(
                                            text=main_currency+" {:,.2f}".format(float(rand_difference)))
                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')
                                        root.destroy()

                                def ZB():
                                    global zb_difference

                                    mydb = mysql.connect(host='localhost', user="root", password="",
                                                         database="retail-system2")
                                    cursor = mydb.cursor()

                                    current = str(datetime.now().strftime("%Y-%m-%d"))

                                    type = "ZB"

                                    script = "Select amount_tendered from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'"

                                    cursor.execute(script)
                                    data = cursor.fetchall()
                                    total = 0
                                    for i in range(len(data)):
                                        total = total + data[i][0]

                                    cursor.execute("Select change_amount from transaction where date_recorded = '" + current + "' and payment_type = '" + type + "'")
                                    datazb = cursor.fetchall()

                                    totalzb = 0
                                    for j in range(len(datazb)):
                                        totalzb = totalzb + datazb[j][0]

                                    zb_difference = float(total) - float(zb_actual.get())

                                    try:
                                        zb_diff.config(
                                            text=main_currency+" {:,.2f}".format(float(zb_difference)))
                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')
                                        root.destroy()



                                def compile():
                                    global actual_total_amount,whole_difference

                                    con = mysql.connect(host='localhost', user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute("select * from rates")
                                    all_rates = cursor.fetchall()

                                    pula_current = str(all_rates[0][2])
                                    rand_current = str(all_rates[1][2])
                                    usd_current = float(all_rates[2][2])
                                    rands = float(rand_actual.get()) * float(rand_current)
                                    cash1=float(cash_actual.get())
                                    eco1=float(eco_actual.get())
                                    usd=float(usd_actual.get()) * float(usd_current)
                                    #zb=float(zb_actual.get())
                                    nmb=float(nmb_actual.get())
                                    zb=float(zb_actual.get())
                                    actual_total_amount = float(cash1+eco1+usd+rands+nmb+zb)
                                    actual_amount_amount1 =  main_currency + str(" {:.2f}".format(actual_total_amount))


                                    total_actual.configure(text=actual_amount_amount1)


                                    whole_difference = cash_difference + eco_difference + usd_difference + rand_difference + nmb_difference + zb_difference

                                    whole_diff_amount = main_currency + str(" {:.2f}".format(whole_difference))

                                    total_diff.configure(text=whole_diff_amount)


                                def insert_banking():
                                    amount1 = str(total_expected_amount)
                                    amount2 = str(actual_total_amount)
                                    amount3 = str(whole_difference)
                                    banker = str(employee_id[0])
                                    bank_date = str(datetime.now().strftime("%Y-%m-%d"))

                                    try:

                                        con = mysql.connect(host='localhost', user='root', password="",
                                                            database="retail-system2")
                                        cursor = con.cursor()
                                        cursor.execute(
                                            "insert into banking(expected,actual,amount_difference,date,banker) "
                                            "values('" + amount1 + "','" + amount2 + "'"
                                            ",'" + amount3 + "','" + bank_date + "','" + banker + "')")
                                        cursor.execute("commit");

                                        root.destroy()
                                        messagebox.showinfo("Insert Status", "Banking Record Added Successful")

                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')


                                ttframe = Frame(root, width=1150, height=60, bg='cadetblue')
                                ttframe.place(x=0, y=0)

                                mainframe = Frame(root, width=1150, height=60, bg='floral white')
                                mainframe.place(x=0, y=60)

                                paytypelab = Label(mainframe,text="Tender",font=("georgia",14),bg="floral white")
                                paytypelab.place(x=10,y=20)

                                expectedlab = Label(mainframe,text="Expected",font=("georgia",14),bg="floral white")
                                expectedlab.place(x=300, y=20)

                                actuallab = Label(mainframe, text="Actual", font=("georgia", 14),
                                                    bg="floral white")
                                actuallab.place(x=620, y=20)

                                difflab = Label(mainframe, text="Difference", font=("georgia", 14),
                                                  bg="floral white")
                                difflab.place(x=950, y=20)

                                mainframe1 = Frame(root, width=300, height=40, bg='floral white',relief=SUNKEN,bd=3)
                                mainframe1.place(x=0, y=120)

                                cash_label = Label(mainframe1, text=str(tenders[0][0]), font=("georgia", 14, "bold"),
                                                    bg="floral white")
                                cash_label.place(x=80, y=5)

                                mainframe2 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                mainframe2.place(x=300, y=120)

                                cash_expected = Label(mainframe2, text=main_currency+ " 0.00", font=("times new roman", 14, "bold"),
                                                      bg="floral white")
                                cash_expected.place(x=80, y=5)

                                mainframe3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3,bg="white")
                                mainframe3.place(x=600, y=120)

                                cash_actual = Entry(mainframe3, width=29,bd=0,justify=RIGHT,font=("times new roman", 14, "bold"))
                                cash_actual.place(x=0,y=0)

                                mainframe4 = Frame(root, width=250, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                mainframe4.place(x=900, y=120)

                                cash_diff = Label(mainframe4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                  bg="floral white")
                                cash_diff.place(x=80, y=5)

                                main2frame1 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main2frame1.place(x=0, y=160)

                                eco_label = Label(main2frame1, text="Ecocash", font=("georgia", 14, "bold"),
                                                   bg="floral white")
                                eco_label.place(x=80, y=5)

                                main2frame2 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main2frame2.place(x=300, y=160)

                                eco_expected = Label(main2frame2, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                      bg="floral white")
                                eco_expected.place(x=80, y=5)

                                main2frame3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3,bg="white")
                                main2frame3.place(x=600, y=160)

                                eco_actual = Entry(main2frame3, width=29, bd=0, justify=RIGHT,font=("times new roman", 14, "bold"))
                                eco_actual.place(x=0, y=0)

                                main2frame4 = Frame(root, width=250, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main2frame4.place(x=900, y=160)

                                eco_diff = Label(main2frame4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                  bg="floral white")
                                eco_diff.place(x=80, y=5)

                                main3frame1 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main3frame1.place(x=0, y=200)

                                nmb_label = Label(main3frame1, text="NMB", font=("georgia", 14, "bold"),
                                                  bg="floral white")
                                nmb_label.place(x=80, y=5)

                                main3frame2 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main3frame2.place(x=300, y=200)

                                nmb_expected = Label(main3frame2, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                     bg="floral white")
                                nmb_expected.place(x=80, y=5)

                                main3frame3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3,bg="white")
                                main3frame3.place(x=600, y=200)

                                nmb_actual = Entry(main3frame3, width=29, bd=0, justify=RIGHT,font=("times new roman", 14, "bold"))
                                nmb_actual.place(x=0, y=0)

                                main3frame4 = Frame(root, width=250, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main3frame4.place(x=900, y=200)

                                nmb_diff = Label(main3frame4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                 bg="floral white")
                                nmb_diff.place(x=80, y=5)

                                main4frame1 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main4frame1.place(x=0, y=240)

                                usd_label = Label(main4frame1, text="USD", font=("georgia", 14, "bold"),
                                                  bg="floral white")
                                usd_label.place(x=80, y=5)

                                main4frame2 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main4frame2.place(x=300, y=240)

                                usd_expected = Label(main4frame2, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                     bg="floral white")
                                usd_expected.place(x=80, y=5)

                                main4frame3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3,bg="green")
                                main4frame3.place(x=600, y=240)

                                usd_actual = Entry(main4frame3, width=29, bd=0, justify=RIGHT,font=("times new roman", 14, "bold"))
                                usd_actual.place(x=0, y=0)

                                main4frame4 = Frame(root, width=250, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main4frame4.place(x=900, y=240)

                                usd_diff = Label(main4frame4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                 bg="floral white")
                                usd_diff.place(x=80, y=5)

                                main5frame1 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main5frame1.place(x=0, y=280)

                                rand_label = Label(main5frame1, text="Rand", font=("georgia", 14, "bold"),
                                                   bg="floral white")
                                rand_label.place(x=80, y=5)


                                main5frame2 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main5frame2.place(x=300, y=280)

                                rand_expected = Label(main5frame2, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                     bg="floral white")
                                rand_expected.place(x=80, y=5)

                                main5frame3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3, bg="white")
                                main5frame3.place(x=600, y=280)

                                rand_actual = Entry(main5frame3, width=29, bd=0, justify=RIGHT,font=("times new roman", 14, "bold")
                                                   )
                                rand_actual.place(x=0, y=0)

                                main5frame4 = Frame(root, width=250, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main5frame4.place(x=900, y=280)

                                rand_diff = Label(main5frame4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                 bg="floral white")
                                rand_diff.place(x=80, y=5)

                                main6frame1 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main6frame1.place(x=0, y=320)

                                zb_label = Label(main6frame1, text="ZB", font=("georgia", 14, "bold"),
                                                      bg="floral white")
                                zb_label.place(x=80, y=5)


                                main6frame2 = Frame(root, width=300, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main6frame2.place(x=300, y=320)

                                zb_expected = Label(main6frame2, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                      bg="floral white")
                                zb_expected.place(x=80, y=5)

                                main6frame3 = Frame(root, width=300, height=40, relief=SUNKEN, bd=3,bg="white")
                                main6frame3.place(x=600, y=320)

                                zb_actual = Entry(main6frame3, width=29, bd=0, justify=RIGHT,font=("times new roman", 14, "bold")
                                                    )
                                zb_actual.place(x=0, y=0)

                                main6frame4 = Frame(root, width=250, height=40, bg='floral white', relief=SUNKEN, bd=3)
                                main6frame4.place(x=900, y=320)

                                zb_diff = Label(main6frame4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                  bg="floral white")
                                zb_diff.place(x=80, y=5)

                                main7frame1 = Frame(root, width=300, height=40, bg='black', relief=SUNKEN, bd=3)
                                main7frame1.place(x=0, y=440)

                                total_label = Label(main7frame1,text="Total",font=("georgia",14,"bold"),fg="white",bg="black")
                                total_label.place(x=80,y=5)

                                main7frame2 = Frame(root, width=300, height=40, bg='black', relief=SUNKEN, bd=3)
                                main7frame2.place(x=300, y=440)

                                total_expected = Label(main7frame2, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                     fg="white",bg="black")
                                total_expected.place(x=80, y=5)

                                main7frame3 = Frame(root, width=300, height=40, bg='black', relief=SUNKEN, bd=3)
                                main7frame3.place(x=600, y=440)

                                total_actual = Label(main7frame3, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                       fg="white", bg="black")
                                total_actual.place(x=80, y=5)

                                main7frame4 = Frame(root, width=250, height=40, bg='black', relief=SUNKEN, bd=3)
                                main7frame4.place(x=900, y=440)

                                total_diff = Label(main7frame4, text=main_currency+" 0.00", font=("times new roman", 14, "bold"),
                                                     fg="white", bg="black")
                                total_diff.place(x=80, y=5)

                                tt2frame = Frame(root, width=1150, height=70, bg='cadetblue')
                                tt2frame.place(x=0, y=540)

                                tlab = Label(ttframe, text='Banking', font=('times new roman', 19, 'bold'),
                                             bg='cadetblue')
                                tlab.place(x=0, y=20)

                                butt18 = Button(tt2frame, text='Compile', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=compile)
                                butt18.place(x=2, y=2)

                                butt10 = Button(tt2frame, text='Close', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=root.destroy)
                                butt10.place(x=1057, y=2)

                                butt11 = Button(tt2frame, text='Ok', font=('times new roman', 14, 'bold'), width=8,
                                                height=3,
                                                command=insert_banking)
                                butt11.place(x=965, y=2)
                                root.after(10, data_cash)
                                root.after(10, data_eco)
                                root.after(10, data_nmb)
                                root.after(10, data_usd)
                                root.after(10, data_rand)
                                root.after(10, data_zb)
                                root.after(10, data_total)
                                cash_actual.bind("<Key>", lambda v: root.after(10, cash))
                                eco_actual.bind("<Key>", lambda v: root.after(10, ecocash))
                                nmb_actual.bind("<Key>", lambda v: root.after(10, Banco))
                                usd_actual.bind("<Key>", lambda v: root.after(10, USD))
                                rand_actual.bind("<Key>", lambda v: root.after(10, rand))
                                zb_actual.bind("<Key>", lambda v: root.after(10, ZB))


                            chib.after(3000, main_win)



                        imglogo2 = ImageTk.PhotoImage(Image.open('assets/trolley2small.png'))
                        imglogo3 = ImageTk.PhotoImage(Image.open('assets/bankinglogo6small1.png'))
                        imglogo4 = ImageTk.PhotoImage(Image.open('assets/imagelogo4small.png'))
                        imglogo5 = ImageTk.PhotoImage(Image.open('assets/inventoryreportsmall1.png'))
                        imglogo6 = ImageTk.PhotoImage(Image.open('assets/imagelogo5small.jpg'))
                        imglogo7 = ImageTk.PhotoImage(Image.open('assets/myimageiconsmall2.png'))
                        clock_label = Label(tframe, image=imglogo7, bg="white")
                        clock_label.place(x=1105, y=40)

                        butt1 = Button(tframe2, text="will", width=160, height=120,
                                           font=("times new roman", 40, "bold"), image=imglogo2,command=receive)
                        butt1.place(x=0, y=0)
                        butt2 = Button(tframe2, text="Will", width=160, height=120,
                                           font=("times new roman", 15, "bold"), image=imglogo2,command=send)
                        butt2.place(x=0, y=120)
                        butt3 = Button(tframe2, text="Will", width=160, height=120,
                                           font=("times new roman", 15, "bold"), image=imglogo3,command=banking)
                        butt3.place(x=0, y=240)
                        butt4 = Button(tframe2, text="Will", width=160, height=125,
                                           font=("times new roman", 15, "bold"), image=imglogo5)
                        butt4.place(x=0, y=360)
                        butt5 = Button(tframe2, text="will", width=160, height=125,
                                           font=("times new roman", 15, "bold"), image=imglogo6, command=report)
                        butt5.place(x=0, y=490)

                        def clock_time():
                            time_string = strftime('%x\n %H:%M:%S %p')
                            time_label.config(text=time_string)
                            time_label.after(1000, clock_time)

                        time_label = Label(tframe, font=("times new roman", 20, 'bold'), bg="white")
                        time_label.place(x=1155, y=20)
                        clock_time()


                        admin.mainloop()

                except Exception as es:
                    messagebox.showerror('Error', f'Error due to: {str(es)}')


        lgBtn = Button(lg, width=10, height=2, bg='cadet blue', text='LOGIN', font=('cansalas', 13, 'bold'),
                       command=login).place(x=160, y=400)
        q.bind('<Return>', login)
    loginwindow()

splash.bind('<Return>',bar)
splash.mainloop()



