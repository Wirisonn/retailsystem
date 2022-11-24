

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

import mysql
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
import tempfile
import os
import tkinter.messagebox
from time import strftime
import mysql.connector as mysql
from tkcalendar import DateEntry
from reportlab.pdfgen import canvas
from datetime import datetime







q = Tk()
q.geometry('1350x750')
q.title('WiRi RETAIL SYSTEMS v1.0.1')
q.iconbitmap(r'titlelogo.ico')
q.resizable(0, 0)

will = open("wilson.txt", "r")
host_address = will.read()

con = mysql.connect(host=host_address, user='root', password='', database='retail-system2')
cursor = con.cursor()

cursor.execute("select * from server_info")
info = cursor.fetchall()
main_currency = str(info[0][3])
main_name = str(info[0][1])
main_code = str(info[0][2])

cursor.execute("select tender_name from tender_type")
tenders = cursor.fetchall()

posframe = Frame(q,bg='lightblue',width=600,height=750)
posframe.place(x=0,y=0)

lg = Frame(posframe, width=600, height=490, bg='white')
lg.place(x=0, y=0)

imglogo2 = ImageTk.PhotoImage(Image.open('user-employee.png'))
logo_label1 = Label(lg, image=imglogo2)
logo_label1.place(x=180, y=20)

usernamelbl = Label(lg, text='Username', bg='white',
                    font=("consolas", 13, 'bold'), padx=10).place(x=2, y=270)

usernameEn = Entry(lg, width=40, fg="black", bg="white", bd=0, font=('consolas', 13))
usernameEn.place(x=150, y=270)

passwordlbl = Label(lg, text='Password', bg='white',
                    font=("consolas", 13, 'bold'), padx=10).place(x=2, y=350)

passwordEn = Entry(lg, width=40, fg="black", bg="white", bd=0, font=('consolas', 13, 'bold'), show='*')
passwordEn.place(x=150, y=350)

#username = usernameEn.get()

usernameframe = Frame(lg, width=350, height=1, bg='black').place(x=150, y=290)
passwordframe = Frame(lg, width=350, height=1, bg='black').place(x=150, y=370)

imglogo3 = ImageTk.PhotoImage(Image.open('createlogosmall.png'))
logo_label2 = Label(posframe, image=imglogo3,bg='lightblue')
logo_label2.place(x=200, y=540)

notfic = Label(q, text='New Notifications',font=('consolas',13))
notfic.place(x=605,y=5)


def login(*args):
    if usernameEn.get() == "" or passwordEn.get() == "":
        messagebox.showerror("Login Status", "   Please Enter Username and Password   ")

    else:
        try:





            con = mysql.connect(host='localhost',user='root',password='',database='retail-system2       ')
            cur = con.cursor()
            cur.execute('select * from employee where name=%s and password=%s',(usernameEn.get(),passwordEn.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error','    Invalid  Username or Password')
                usernameEn.delete(0,'end')
                passwordEn.delete(0,'end')

            else:

                global imglogo4,imglogo5,imglogo6
                passwordEn.delete(0, 'end')
                q.withdraw()
                w = Toplevel()
                w.geometry('1350x750')
                w.title('WiRi RETAIL SYSTEMS v1.0.1')
                w.iconbitmap(r'titlelogo.ico')
                w.resizable(0, 0)

                con = mysql.connect(host=host_address, user='root', password="",
                                    database="retail-system2")
                cursor = con.cursor()
                cursor.execute(
                    "SELECT employee_id FROM employee WHERE name like'%" + usernameEn.get() + "%'")
                employee_id = cursor.fetchone()

                def logout(*args):

                    try:

                        logoutwin = Tk()
                        logoutwin.geometry('450x400+440+150')
                        logoutwin.iconbitmap(r'titlelogo.ico')
                        logoutwin.resizable(0, 0)
                        logoutwin.overrideredirect(1)
                        logoutwin.configure(background="cadetblue")

                        def yes():
                            logoutwin.destroy()
                            w.destroy()
                            q.deiconify()

                        def no():
                            logoutwin.destroy()

                        trade_label = Label(logoutwin,text="WiRi Retail***",font=("cansalas",14),bg="cadetblue")
                        trade_label.place(x=5,y=10)

                        warn_label = Label(logoutwin,text="ARE YOU SURE YOU WOULD LIKE TO",font=("georgia",15,"bold"),bg="cadetblue")
                        warn_label.place(x=5,y=70)

                        warn_label = Label(logoutwin, text="LOG OUT THE POS?",
                                           font=("georgia", 15,"bold"), bg="cadetblue")
                        warn_label.place(x=5, y=100)

                        yes_butt = Button(logoutwin,text="Yes",width=7, height=3,font=("georgia",14),command=yes)
                        yes_butt.place(x=50,y=280)

                        no_butt = Button(logoutwin, text="No", width=7, height=3, font=("georgia", 14),command=no)
                        no_butt.place(x=300, y=280)

                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')

                def addupdate_main():
                    global tota

                    tota = 0
                    for child in trv.get_children():
                        tota += float(trv.item(child, 'values')[4])

                    try:
                        submoney.config(text=main_currency +" {:,.2f}".format(float(tota)))
                    except:
                        submoney.config(text=main_currency +" 0.00")

                upframe = Frame(w, width=1350,height=90,bg='lightblue')
                upframe.place(x=0,y=0)

                imglogo4 = ImageTk.PhotoImage(Image.open('createlogosmall1.png'))
                logo_label3 = Label(upframe, image=imglogo4, bg='lightblue')
                logo_label3.place(x=0, y=0)

                upperlabel = Button(upframe, text="WiRi", font=("Garamond", 18, "bold"), bg="lightblue",bd=0,
                                    command=logout)
                upperlabel.place(x=77, y=43)

                itemframe = Frame(w,width=1000,height=550,bg='red')
                itemframe.place(x=0,y=90)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=(None,14,'bold'),fg='pink')
                #style.theme_use('clam')

                trv = ttk.Treeview(itemframe, columns=(1, 2, 3, 4, 5), show="headings",
                                   height=23)
                trv.place(x=0, y=0)

                trv.column("1", anchor=CENTER, stretch=NO, width=200)
                trv.column("2", anchor=CENTER, stretch=NO, width=200)
                trv.column("3", anchor=CENTER, stretch=NO, width=200)
                trv.column("4", anchor=CENTER, stretch=NO, width=200)
                trv.column("5", anchor=CENTER, stretch=NO, width=200)



                trv.heading(1, text="Transaction ID")
                trv.heading(2, text="Description")
                trv.heading(3, text="Quantity")
                trv.heading(4, text="Price")
                trv.heading(5, text="Total")



                priceframe = Frame(itemframe,width=1000,height=80,bg='grey')
                priceframe.place(x=0,y=470)

                Qframe = Frame(priceframe, width=198, height=76,bd=10)
                Qframe.place(x=0, y=2)

                Qlabel = Label(Qframe,text="Items Quantity",font=("open sans",12,"bold"),fg='blue')
                Qlabel.place(x=0,y=0)

                Qnum = Label(Qframe, text="0/0.00", font=("open sans", 18, "bold"),fg='blue')
                Qnum.place(x=0, y=35)

                subframe = Frame(priceframe, width=198, height=76, bd=10)
                subframe.place(x=200, y=2)

                sublabel = Label(subframe, text="Sub Total", font=("open sans", 12, "bold"),fg='blue')
                sublabel.place(x=0, y=0)

                submoney = Label(subframe, text=main_currency+" 0.00", font=("open sans", 18, "bold"),fg='blue')
                submoney.place(x=0, y=35)

                discountframe = Frame(priceframe, width=198, height=76, bd=10)
                discountframe.place(x=400, y=2)

                discountlabel = Label(discountframe, text="Discount Amount", font=("open sans", 12, "bold"),fg='blue')
                discountlabel.place(x=0, y=0)

                discountmoney = Label(discountframe, text=main_currency +" 0.00", font=("open sans", 18, "bold"),fg='blue')
                discountmoney.place(x=0, y=35)

                taxframe = Frame(priceframe, width=198, height=76, bd=10)
                taxframe.place(x=600, y=2)

                taxlabel = Label(taxframe, text="Tax", font=("open sans", 12, "bold"),fg='blue')
                taxlabel.place(x=0, y=0)

                taxmoney = Label(taxframe, text=main_currency + " 0.00", font=("open sans", 18, "bold"),fg='blue')
                taxmoney.place(x=0, y=35)

                totalframe = Frame(priceframe, width=198, height=76, bd=10)
                totalframe.place(x=800, y=2)

                totallabel = Label(totalframe, text="Total", font=("open sans", 12, "bold"),fg='blue')
                totallabel.place(x=0, y=0)

                totalmoney = Label(totalframe, text=main_currency+" 0.00", font=("open sans", 18, "bold"),fg='blue')
                totalmoney.place(x=0, y=35)


                #w.after(10, addupdatemain)






                butframe = Frame(w, width=1350, height=100, bg='cadetblue')
                butframe.place(x=0, y=640)

######################################################################PAYMENTS#####################################################################



                def payments(*args):

                    try:

                        global usernameEn

                        paywin = Tk()
                        paywin.geometry('750x500+320+150')
                        paywin.iconbitmap(r'titlelogo.ico')
                        paywin.resizable(0, 0)





                        def change():

                            global change_amount


                            change_amount= float(amounten.get())-tot

                            try:

                                amountchangefig.config(text=main_currency+" {:,.2f}".format(float(change_amount)))
                                amounttendfig.config(text=main_currency+" {:,.2f}".format(float(amounten.get())))

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')
                                paywin.destroy()


                        def addupdate():
                            global tot

                            tot = 0
                            for child in trv.get_children():
                                tot += float(trv.item(child,'values')[4])

                            try:payamountfig.config(text=main_currency+" {:,.2f}".format(float(tot)))
                            except:payamountfig.config(text=main_currency+" 0.00")




                        def select():
                            global tot, proquan, ided,aim

                            if payen.get() == '' or amounten.get() == '' or trv.focus() == '':
                                messagebox.showerror('Error', "Please Enter Tender Type or Amount Tendered\n"
                                                              "Make Sure You Have Selected Your Products!!!")

                            else:

                                changee = str(change_amount)
                                total = str(tot)
                                trans_id=str(txnen.get())
                                tendered=str(amounten.get())
                                employee= str(employee_id[0])
                                type=payen.get()
                                date = str(datetime.now().strftime("%Y-%m-%d"))
                                customer = "1"

                                con = mysql.connect(host=host_address, user='root', password="",
                                                    database="retail-system2")
                                cursor = con.cursor()

                                cursor.execute(
                                    "insert into transaction values('" + trans_id + "','" + customer + "','" + type + "','" + total + "','" + tendered + "','" + changee + "','" + date + "','" + employee + "')")
                                cursor.execute("commit");
                                amounten.delete(0,'end')

                                curItems = trv.selection()
                                best = [(trv.item(i)['values']) for i in curItems]




                                for i in range(len(best)):
                                    con = mysql.connect(host=host_address, user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()

                                    aim = best[i][1]
                                    sql2 = "SELECT product_id FROM product WHERE name ='" + aim + "'"
                                    cursor.execute(sql2)
                                    proid = cursor.fetchall()
                                    proid2 = proid[0][0]
                                    proid22 = str(proid2)
                                    date = str(datetime.now().strftime("%Y-%m-%d"))
                                    best[i][1] = proid2
                                    proquan = str(best[i][2])
                                    ided = str(best[i][0])
                                    cursor.execute("select diff_cost from product where product_id='"+str(proid2)+"'")
                                    cost = cursor.fetchall()
                                    total_cost = float(cost[0][0])*float(proquan)
                                    total_cost1 = str(total_cost)
                                    employee = str(employee_id[0])
                                    sale = 'Sale'
                                    cumulative = '100'
                                    cursor.execute("insert into inventory_audit values('"+proid22+"', '"+sale+"', '"+proquan+"', '"+total_cost1+"', '"+cumulative+"', '"+date+"' )  ")
                                    cursor.execute("commit");






                                sql = "INSERT INTO sales( invoice_id,product_id,quantity, unit_price, sub_total) VALUES (%s, %s, %s,%s,%s)"

                                cursor.executemany(sql,
                                                   best[0:])
                                cursor.execute("commit")

                                cursor.execute("insert into profitter(pro_id, total_cost, date) values('"+str(proid2)+"', '"+str(total_cost)+"','"+date+"')")
                                cursor.execute("commit")
                                con.close()
                                con.close()
                                arrow_down = '↓'
                                arrow_up = '↑'

                                def printer():
                                    try:

                                        pap2 = str(pap - 1)

                                        con = mysql.connect(host=host_address, user='root', password="",
                                                            database="retail-system2")
                                        cursor = con.cursor()


                                        curItems = trv.selection()
                                        best = [(trv.item(i)['values']) for i in curItems]
                                        # Creating Canvas
                                        c = canvas.Canvas("invoicemain12.pdf", pagesize=(200, 400), bottomup=0)

                                        # Logo Section
                                        # Setting th origin to (10,40)
                                        c.translate(10, 40)
                                        # Inverting the scale for getting mirror Image of logo
                                        c.scale(1, -1)
                                        # Inserting Logo into the Canvas at required position
                                        c.drawImage("wilfa.jpg", 60, -10, width=60, height=50)

                                        # Title Section
                                        # Again Inverting Scale For strings insertion
                                        c.scale(1, -1)
                                        # Again Setting the origin back to (0,0) of top-left
                                        c.translate(-10, -40)
                                        # Setting the font for Name title of company
                                        c.setFont("Helvetica-Bold", 10)

                                        c.setFont("Helvetica-Bold", 5)
                                        c.drawCentredString(100, 65, "EN 8, em Direcçã ao Mercado Waresta")
                                        c.drawCentredString(100, 70, "Waresta - Nampula")
                                        c.drawCentredString(100, 75, "Telefone: (+258)844892251")
                                        c.drawCentredString(100, 80, "Cashier Nome: " + str(usernameEn.get()))
                                        c.setFont("Helvetica-Bold", 6)
                                        c.drawCentredString(100, 87, "NUIT : 400387494")

                                        c.line(5, 90, 195, 90)


                                        c.setFont("Courier-Bold", 8)



                                        c.setFont("Times-Bold", 5)
                                        c.drawRightString(70, 100, "FACTURA No. :")
                                        c.drawRightString(70, 110, "DATA & TEMPO :")
                                        c.drawRightString(70, 120, "CLIENTE ID :")
                                        c.drawRightString(70, 130, "TELEFONE   :")
                                        c.line(15, 95, 185, 95)
                                        c.line(15, 95, 15, 135)
                                        c.line(15, 135, 185, 135)
                                        c.line(185, 95, 185, 135)
                                        c.line(15, 105, 185, 105)
                                        c.line(15, 115, 185, 115)
                                        c.line(15, 125, 185, 125)


                                        yey = "GOODS DESCRIPTION"
                                        c.line(15, 167, 185, 167)
                                        c.drawCentredString(25, 165, "SR No.")
                                        c.drawCentredString(75, 165, yey)
                                        c.drawCentredString(125, 165, "QTY")
                                        c.drawCentredString(148, 165, "PRICE")
                                        c.drawCentredString(173, 165, "TOTAL")

                                        c.drawString(15, 360,
                                                     "*************************** THANK YOU ******************************")
                                        c.drawString(25, 326, "Payment Summary       |")
                                        c.drawString(75, 326, "             Amount           |")
                                        c.drawRightString(170, 326, "Tendered")
                                        c.line(15, 320, 185, 320)
                                        c.line(15, 330, 185, 330)
                                        count = 175
                                        for i in range(len(best)):
                                            best2 = best[i]



                                            best3 = str(best2[0])
                                            a2 = str(best2[1])
                                            a3 = str(best2[2])
                                            a4 = str(best2[3])
                                            a5 = str(best2[4])
                                            a6 = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                            a7 = customer
                                            a8 = "INV00000"+str(best2[0])

                                            c.setFont("Times-Bold", 6)
                                            c.drawString(20,count,best3)
                                            c.drawString(55, count, a2)
                                            c.drawString(123, count, a3)
                                            c.drawString(145, count, a4)
                                            c.drawString(167, count, a5)
                                            c.drawString(155, 340, total)
                                            c.drawString(95, 340, tendered)
                                            c.drawString(35, 340, type)
                                            c.drawString(85 , 100, a8)
                                            c.drawString(85, 110, a6)
                                            c.drawString(85, 120, a7)
                                            count += 10

                                        c.showPage()
                                        c.save()
                                        file_name = tempfile.NamedTemporaryFile(suffix=".pdf",delete=False)
                                        #os.startfile('invoicemain12.pdf', 'print')




                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')

                                printer()





                                paywin.destroy()




                        def incre_id():
                            global pap, last_main
                            con = mysql.connect(host=host_address, user="root", password="", database="retail-system2")
                            cur = con.cursor()

                            sql = "SELECT transaction_id FROM transaction ORDER BY transaction_id DESC LIMIT 1"
                            cur.execute(sql)
                            last_id = cur.fetchone()
                            pap = int(last_id[0]) + 1

                            txnen.insert(0,pap)
                            last_main = str(pap)




                        def decrease():
                            con = mysql.connect(host=host_address, user='root', password="",
                                                database="retail-system2")
                            cursor = con.cursor()
                            cursor.execute("select quantity from sales where invoice_id ='"+last_main+"' ")
                            main_sales = cursor.fetchall()
                            for i in range(len(main_sales)):
                                curItems = trv.selection()
                                best = [(trv.item(i)['values']) for i in curItems]

                                cursor.execute("select product_id from sales where invoice_id ='"+last_main+"' ")
                                main_id = cursor.fetchall()
                                for i in range(len(main_id)):
                                    print(main_id[i][0])

                                    con = mysql.connect(host=host_address, user='root', password="",
                                                        database="retail-system2")
                                    cursor = con.cursor()
                                    cursor.execute(
                                            "update product set unit_in_stock= unit_in_stock - '" + str(main_sales[i][0]) + "' where product_id='" + str(main_id[i][0]) + "'")
                                    cursor.execute("commit");

                                    cursor.execute(
                                        "update product set total_cost= unit_in_stock * cost_price where product_id='" + str(main_id[i][0]) + "'")
                                    cursor.execute("commit");

                                    trv.delete(*trv.get_children())

                                    con.close()
                                #except Exception as es:
                                    #messagebox.showerror('Error', f'Error due to: {str(es)}')






                        infoframe = Frame(paywin,width=250,height=500,bg="floral white")
                        infoframe.place(x=0,y=0)

                        txnlab = Label(infoframe,text="Transaction ID",font=("cansalas",15),bg="floral white")
                        txnlab.place(x=60,y=20)

                        txnen = Entry(infoframe,font=("cansalas",14),width=20)
                        txnen.place(x=15,y=60)

                        payinfo = Frame(paywin,width=650,height=50,bg="black")
                        payinfo.place(x=250,y=0)

                        payamount = Label(payinfo, text="Amount Payable",font=("cansalas",10),fg="white",bg="black")
                        payamount.place(x=5,y=5)

                        payamountfig = Label(payinfo, text=main_currency+" 0.00", font=("cansalas",10),fg="white",bg="black")
                        payamountfig.place(x=30, y=25)

                        amounttend = Label(payinfo, text="Amount Tendered",font=("cansalas",10),fg="white",bg="black")
                        amounttend.place(x=200, y=5)

                        amounttendfig = Label(payinfo, text=main_currency+" 0.00",font=("cansalas",10),fg="white",bg="black")
                        amounttendfig.place(x=220, y=25)

                        amountchange = Label(payinfo, text="Amount Change", font=("cansalas",10),fg="white",bg="black")
                        amountchange.place(x=400, y=5)

                        amountchangefig = Label(payinfo, text=main_currency+" 0.00", font=("cansalas",10),fg="white",bg="black")
                        amountchangefig.place(x=405, y=25)


                        paylab = Label(infoframe, text="Payment Type", font=("cansalas", 15), bg="floral white")
                        paylab.place(x=60, y=140)

                        payen = ttk.Combobox(infoframe, width=17, font=('open sans', 15, "bold"))
                        payen["values"] = tenders
                        payen.place(x=15, y=180)

                        okframe = Frame(paywin,width=650,height=100,bg="cadetblue")
                        okframe.place(x=250,y=400)

                        okbutt = Button(okframe,text="Ok",command=lambda:[select(),decrease()],width=5)
                        okbutt.place(x=0,y=5)

                        amountframe = Frame(paywin,width=255,height=280,bg="blue")
                        amountframe.place(x=350,y=80)

                        amounten = Entry(amountframe,width=23,font=("cansalas",14),justify=RIGHT)
                        amounten.place(x=0,y=0)

                        amount0 = Button(amountframe,width=11,height=4,text="0")
                        amount0.place(x=0,y=210)

                        amount1 = Button(amountframe, width=11, height=4, text="1")
                        amount1.place(x=0, y=150)

                        amount2 = Button(amountframe, width=11, height=4, text="2")
                        amount2.place(x=85, y=150)

                        amount3 = Button(amountframe, width=11, height=4, text="3")
                        amount3.place(x=170, y=150)

                        amount4 = Button(amountframe, width=11, height=4, text="4")
                        amount4.place(x=0, y=100)

                        amount5 = Button(amountframe, width=11, height=4, text="5")
                        amount5.place(x=85, y=100)

                        amount6 = Button(amountframe, width=11, height=4, text="6")
                        amount6.place(x=170, y=100)

                        amount7 = Button(amountframe, width=11, height=4, text="7")
                        amount7.place(x=0, y=30)

                        amount8 = Button(amountframe, width=11, height=4, text="8")
                        amount8.place(x=85, y=30)

                        amount9 = Button(amountframe, width=11, height=4, text="9")
                        amount9.place(x=170, y=30)


                        amounten.bind("<Key>", lambda v: paywin.after(10, change))
                        paywin.after(10, addupdate)
                        paywin.after(10, incre_id)


                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')










#####################################################====================================TransactionMode=========================================

                def transaction():

                    try:

                        trasnmode = Tk()
                        trasnmode.geometry("1350x750")
                        trasnmode.title('WiRi RETAIL SYSTEMS v1.0.1')
                        trasnmode.iconbitmap(r'titlelogo.ico')
                        trasnmode.resizable(0, 0)

                        transmodestatus = Label(trasnmode,text="Page Not Available !",font=("open sans",20,"bold"))
                        transmodestatus.place(x=550,y=350)

                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')

                #============================================CustomerSearch=========================================

                def custsearch(*args):

                    try:

                        cust = Tk()
                        cust.geometry("1350x750")
                        cust.title('WiRi RETAIL SYSTEMS v1.0.1')
                        cust.iconbitmap(r'titlelogo.ico')
                        cust.resizable(0, 0)


                        proframe = Frame(cust, width=1350, height=80, bg='lightblue')
                        proframe.place(x=0, y=0)

                        prolabel = Label(proframe, text="Customer Search", font=("open sans", 20), bg='lightblue')
                        prolabel.place(x=0, y=40)

                        criteria = Frame(cust, width=452, height=402, bd=1, relief=RIDGE)
                        criteria.place(x=3, y=80)

                        first = Frame(criteria, width=450, height=50, relief=RIDGE, bd=1, bg='floral white')
                        first.place(x=0, y=0)

                        firstlabel = Label(first, text="Search Criteria", font=("open sans", 14), bg="floral white")
                        firstlabel.place(x=0, y=20)

                        second = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        second.place(x=0, y=50)

                        secondlabel = Label(second, text="Customer Code", font=("open sans", 13))
                        secondlabel.place(x=1, y=20)

                        second2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                        second2.place(x=225, y=50)

                        secentry = Entry(second2, width=20, bd=0, font=("open sans", 13))
                        secentry.place(x=0, y=15)

                        third = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        third.place(x=0, y=100)

                        thirdlabel = Label(third, text="Customer Name", font=("open sans", 13))
                        thirdlabel.place(x=1, y=20)

                        third2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                        third2.place(x=225, y=100)

                        thirdentry = Entry(third2, width=20, bd=0, font=("open sans", 13))
                        thirdentry.place(x=0, y=15)

                        four = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        four.place(x=0, y=150)

                        fourlabel = Label(four, text="UPC Code", font=("open sans", 13))
                        fourlabel.place(x=1, y=20)

                        four2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        four2.place(x=225, y=150)

                        five = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        five.place(x=0, y=200)

                        fivelabel = Label(five, text="Group", font=("open sans", 13))
                        fivelabel.place(x=1, y=20)

                        five2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        five2.place(x=225, y=200)

                        six = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        six.place(x=0, y=250)

                        sixlabel = Label(six, text="Category", font=("open sans", 13))
                        sixlabel.place(x=1, y=20)

                        six2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        six2.place(x=225, y=250)

                        seven = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        seven.place(x=0, y=300)

                        sevenlabel = Label(seven, text="Customer Catalogue Number", font=("open sans", 13))
                        sevenlabel.place(x=1, y=20)

                        seven2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        seven2.place(x=225, y=300)

                        eight = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        eight.place(x=0, y=350)

                        eightlabel = Label(eight, text="Vendor ID", font=("open sans", 13))
                        eightlabel.place(x=1, y=20)

                        eight2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        eight2.place(x=225, y=350)

                        nine = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        nine.place(x=0, y=400)

                        ninelabel = Label(nine, text="Type", font=("open sans", 13))
                        ninelabel.place(x=1, y=20)

                        nine2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        nine2.place(x=225, y=400)

                        # =============================Treeview++++++++++++++++++++++++++++++++
                        def connection():
                            config = {
                                "user": "root",
                                "password": " ",
                                "host": "localhost",
                                "database": "retail-system2"
                            }
                            try:
                                c = mysql.connect(**config)
                                return c
                            except:
                                print("connection error")


                        def update(rows):
                            trv1.delete(*trv1.get_children())
                            for i in rows:
                                trv1.insert('', 'end', values=i)

                        def search():

                            try:

                                mydb = mysql.connect(host=host_address, user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()
                                cur.execute(
                                    "select * from customer where customer_code like '%" + secentry.get() + "%' and name like '%" + thirdentry.get() + "%' ")

                                rows = cur.fetchall()
                                update(rows)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')


                        mydb = mysql.connect(host=host_address, user="root", password="", database="retail-system2")
                        cursor = mydb.cursor()

                        wrapper1 = Label(cust, width=500, height=50)
                        wrapper1.place(x=455, y=80)

                        trv1 = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5), show="headings",
                                            height=26)
                        trv1.place(x=0, y=0)

                        trv1.column("1", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("2", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("3", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("4", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("5", anchor=CENTER, stretch=NO, width=170)


                        trv1.heading(1, text="Customer ID")
                        trv1.heading(2, text="Customer Code")
                        trv1.heading(3, text="Name")
                        trv1.heading(4, text="Contact")
                        trv1.heading(5, text="Address")

                        cursor.execute("select * from customer")
                        rows = cursor.fetchall()
                        update(rows)



                        prosearchbutf = Frame(cust, width=1350, height=105, bg="cadetblue")
                        prosearchbutf.place(x=0, y=630)

                        def closecussearch():
                            cust.destroy()

                        posbut1 = Button(prosearchbutf, width=13, height=7, text=("F1\n""Search"),
                                         font=('open sans', 10), command=search)
                        posbut1.place(x=0, y=2)

                        posbut2 = Button(prosearchbutf, width=13, height=7, text=("F2\n""Clear"),
                                         font=('open sans', 10), command=None)
                        posbut2.place(x=120, y=2)

                        posbut3 = Button(prosearchbutf, width=13, height=7, text=("F3\n""New"),
                                         font=('open sans', 10), command=None)
                        posbut3.place(x=240, y=2)

                        posbut4 = Button(prosearchbutf, width=13, height=7, text=("F4\n""Edit"),
                                         font=('open sans', 10))
                        posbut4.place(x=360, y=2)

                        posbut5 = Button(prosearchbutf, width=13, height=7, text=("F5\n""Delete"),
                                         font=('open sans', 10))
                        posbut5.place(x=480, y=2)

                        posbut6 = Button(prosearchbutf, width=13, height=7, text=("F6\n""View"),
                                         font=('open sans', 10))
                        posbut6.place(x=600, y=2)

                        posbut7 = Button(prosearchbutf, width=13, height=7, text=("F7\n""Serial\n""Numbers"),
                                         font=('open sans', 10))
                        posbut7.place(x=720, y=2)

                        posbut8 = Button(prosearchbutf, width=13, height=7, text=("F8\n""Batch\n""Numbers"),
                                         font=('open sans', 10))
                        posbut8.place(x=840, y=2)

                        posbut9 = Button(prosearchbutf, width=13, height=7, text=("F9\n""View\n""Inventory"),
                                         font=('open sans', 10))
                        posbut9.place(x=960, y=2)

                        posbut10 = Button(prosearchbutf, width=13, height=7, text=("F10\n""Ok"),
                                          font=('open sans', 10))
                        posbut10.place(x=1080, y=2)

                        posbut11 = Button(prosearchbutf, width=17, height=7, text=("F11\n""Cancel"),
                                          font=('open sans', 10), command=closecussearch)
                        posbut11.place(x=1200, y=2)

                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')





                ################################################ProductSearch############################################################

                def prosearch(*args):

                    try:

                        productsearch = Tk()
                        productsearch.geometry("1350x750")
                        productsearch.title('WiRi RETAIL SYSTEMS v1.0.1')
                        productsearch.iconbitmap(r'titlelogo.ico')
                        productsearch.resizable(0, 0)

                        proframe = Frame(productsearch,width=1350,height=80,bg='lightblue')
                        proframe.place(x=0,y=0)

                        prolabel = Label(proframe,text="Product Search",font=("open sans",20),bg='lightblue')
                        prolabel.place(x=0,y=40)

                        criteria = Frame(productsearch,width=452,height=402,bd=1,relief=RIDGE)
                        criteria.place(x=3,y=80)

                        first = Frame(criteria,width=450,height=50,relief=RIDGE,bd=1,bg='floral white')
                        first.place(x=0,y=0)

                        firstlabel = Label(first,text="Search Criteria",font=("open sans",14),bg="floral white")
                        firstlabel.place(x=0,y=20)

                        second = Frame(criteria,width=225,height=50,relief=RIDGE,bd=1)
                        second.place(x=0,y=50)

                        secondlabel = Label(second,text="Code",font=("open sans",13))
                        secondlabel.place(x=1,y=20)

                        second2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1,bg="white")
                        second2.place(x=225, y=50)

                        secentry = Entry(second2,width=20,bd=0,font=("open sans",13))
                        secentry.place(x=0,y=15)

                        third = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        third.place(x=0, y=100)

                        thirdlabel = Label(third, text="Description", font=("open sans", 13))
                        thirdlabel.place(x=1, y=20)

                        third2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1,bg="white")
                        third2.place(x=225, y=100)

                        thirdentry = Entry(third2, width=20, bd=0, font=("open sans", 13))
                        thirdentry.place(x=0, y=15)

                        four = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        four.place(x=0, y=150)

                        fourlabel = Label(four, text="UPC Code", font=("open sans", 13))
                        fourlabel.place(x=1, y=20)

                        four2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        four2.place(x=225, y=150)

                        five = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        five.place(x=0, y=200)

                        fivelabel = Label(five, text="Group", font=("open sans", 13))
                        fivelabel.place(x=1, y=20)

                        five2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        five2.place(x=225, y=200)

                        six = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        six.place(x=0, y=250)

                        sixlabel = Label(six, text="Category", font=("open sans", 13))
                        sixlabel.place(x=1, y=20)

                        six2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        six2.place(x=225, y=250)

                        seven = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        seven.place(x=0, y=300)

                        sevenlabel = Label(seven, text="Customer Catalogue Number", font=("open sans", 13))
                        sevenlabel.place(x=1, y=20)

                        seven2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        seven2.place(x=225, y=300)

                        eight = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        eight.place(x=0, y=350)

                        eightlabel = Label(eight, text="Vendor ID", font=("open sans", 13))
                        eightlabel.place(x=1, y=20)

                        eight2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        eight2.place(x=225, y=350)

                        nine = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        nine.place(x=0, y=400)

                        ninelabel = Label(nine, text="Type", font=("open sans", 13))
                        ninelabel.place(x=1, y=20)

                        nine2 = Frame(criteria, width=225, height=50, relief=RIDGE, bd=1)
                        nine2.place(x=225, y=400)

                        #=============================Treeview++++++++++++++++++++++++++++++++
                        def connection():
                            config = {
                                "user": "root",
                                "password" : " ",
                                "host":  "localhost",
                                "database": "retail-system2"
                            }
                            try:
                                c = mysql.connect(**config)
                                return c
                            except:
                                print ("connection error")



                        def update(rows):

                            try:

                                trv1.delete(*trv1.get_children())
                                for i in rows:
                                    trv1.insert('','end',values=i)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')




                        def search():
                            try:

                                mydb = mysql.connect(host=host_address, user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()
                                cursor.execute("select * from product where product_code like '%"+secentry.get()+"%' and name like '%"+thirdentry.get()+"%' ")
                                rows = cursor.fetchall()
                                update(rows)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')




                        def quantitywin():
                            global quanen, quanwin



                            quanwin = Tk()
                            quanwin.geometry('250x100+520+250')
                            quanwin.iconbitmap(r'titlelogo.ico')
                            quanwin.resizable(0, 0)

                            quanen = Entry(quanwin,font=("times new roman",14),width=15)
                            quanen.place(x=90,y=20)

                            quanlab = Label(quanwin,text="Quantity",font=("cansalas",16,"bold"))
                            quanlab.place(x=0,y=20)




                            def element_clicked():

                                global count, quanen, quanwin, last_id

                                quant = quanen.get()

                                con = mysql.connect(host=host_address, user="root", password="", database="retail-system2")
                                cur = con.cursor()

                                sql = "SELECT transaction_id FROM transaction ORDER BY transaction_id DESC LIMIT 1"
                                cur.execute(sql)
                                last_id = cur.fetchone()
                                pap = int(last_id[0]) + 1


                                item = trv1.focus()
                                pri = trv1.item(item, "values")

                                count = 0
                                tot = float(pri[4])*int(quant)
                                trv.insert('','end',values=(pap,pri[2],quant,pri[4],tot))
                                count += 1
                                productsearch.destroy()
                                quanwin.destroy()

                            quanbutt = Button(quanwin, text="OK", width=5, command=element_clicked)
                            quanbutt.place(x=50, y=50)


                        def voiditem():
                            x = trv.selection()[0]
                            trv.delete(x)

                        mydb = mysql.connect(host=host_address, user="root", password="", database="retail-system2")
                        cursor = mydb.cursor()

                        wrapper1 = Label(productsearch, width=500, height=50)
                        wrapper1.place(x=455, y=80)


                        trv1 = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5), show="headings",
                                           height=26)
                        trv1.place(x=0, y=0)

                        trv1.column("1", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("2", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("3", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("4", anchor=CENTER, stretch=NO, width=180)
                        trv1.column("5", anchor=CENTER, stretch=NO, width=170)


                        trv1.heading(1, text="Product ID")
                        trv1.heading(2, text="Product Code")
                        trv1.heading(3, text="Description")
                        trv1.heading(4, text="Category ID")
                        trv1.heading(5, text="Price")


                        cursor.execute("select * from product")
                        rows = cursor.fetchall()
                        update(rows)



                        #global count



                        prosearchbutf = Frame(productsearch,width=1350,height=105,bg="cadetblue")
                        prosearchbutf.place(x=0,y=630)

                        def closeprosearch():
                            productsearch.destroy()

                        posbut1 = Button(prosearchbutf, width=13, height=7, text=("F1\n""Search"),
                                         font=('open sans', 10), command=search)
                        posbut1.place(x=0, y=2)

                        posbut2 = Button(prosearchbutf, width=13, height=7, text=("F2\n""Clear"),
                                         font=('open sans', 10), command=None)
                        posbut2.place(x=120, y=2)

                        posbut3 = Button(prosearchbutf, width=13, height=7, text=("F3\n""New"),
                                         font=('open sans', 10), command=None)
                        posbut3.place(x=240, y=2)

                        posbut4 = Button(prosearchbutf, width=13, height=7, text=("F4\n""Edit"),
                                         font=('open sans', 10))
                        posbut4.place(x=360, y=2)

                        posbut5 = Button(prosearchbutf, width=13, height=7, text=("F5\n""Delete"),
                                         font=('open sans', 10))
                        posbut5.place(x=480, y=2)

                        posbut6 = Button(prosearchbutf, width=13, height=7, text=("F6\n""View"),
                                         font=('open sans', 10))
                        posbut6.place(x=600, y=2)

                        posbut7 = Button(prosearchbutf, width=13, height=7, text=("F7\n""Serial\n""Numbers"),
                                         font=('open sans', 10))
                        posbut7.place(x=720, y=2)

                        posbut8 = Button(prosearchbutf, width=13, height=7, text=("F8\n""Batch\n""Numbers"),
                                         font=('open sans', 10))
                        posbut8.place(x=840, y=2)

                        posbut9 = Button(prosearchbutf, width=13, height=7, text=("F9\n""View\n""Inventory"),
                                         font=('open sans', 10))
                        posbut9.place(x=960, y=2)

                        posbut10 = Button(prosearchbutf, width=13, height=7, text=("F10\n""Ok"),
                                          font=('open sans', 10), command= quantitywin)
                        posbut10.place(x=1080, y=2)

                        posbut11 = Button(prosearchbutf, width=17, height=7, text=("F11\n""Cancel"),
                                          font=('open sans', 10),command=closeprosearch)
                        posbut11.place(x=1200, y=2)


                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')





#########################################################VOID-ITEM#######################################################################################

                def voiditem(*args):

                    try:

                        x = trv.selection()[0]
                        trv.delete(x)

                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')




##########################################################VOID-SALE#######################################################################################

                def voidsale(*args):

                    try:

                        void_sale = Tk()
                        void_sale.geometry('450x400+440+150')
                        void_sale.iconbitmap(r'titlelogo.ico')
                        void_sale.resizable(0, 0)
                        void_sale.overrideredirect(1)
                        void_sale.configure(background="cadetblue")

                        def yes():
                            for record in trv.get_children():
                                trv.delete(record)
                                void_sale.destroy()

                        def no():
                            void_sale.destroy()

                        trade_label = Label(void_sale,text="WiRi Retail***",font=("cansalas",14),bg="cadetblue")
                        trade_label.place(x=5,y=10)

                        warn_label = Label(void_sale,text="ARE YOU SURE YOU WOULD LIKE TO",font=("georgia",15,"bold"),bg="cadetblue")
                        warn_label.place(x=5,y=70)

                        warn_label = Label(void_sale, text="CLEAR OUT THE SALE?",
                                           font=("georgia", 15,"bold"), bg="cadetblue")
                        warn_label.place(x=5, y=100)

                        yes_butt = Button(void_sale,text="Yes",width=7, height=3,font=("georgia",14),command=yes)
                        yes_butt.place(x=50,y=280)

                        no_butt = Button(void_sale, text="No", width=7, height=3, font=("georgia", 14),command=no)
                        no_butt.place(x=300, y=280)

                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')







######################################################TRANSACTION-SEARCH#################################################################################




                def transearch(*args):

                    try:

                        transactionsearch = Tk()
                        transactionsearch.geometry("1350x750")
                        transactionsearch.title('WiRi RETAIL SYSTEMS v1.0.1')
                        transactionsearch.iconbitmap(r'titlelogo.ico')
                        transactionsearch.resizable(0, 0)

                        transframe = Frame(transactionsearch, width=1350, height=80, bg='lightblue')
                        transframe.place(x=0, y=0)

                        translabel = Label(transframe, text="Transaction Search", font=("open sans", 20), bg='lightblue')
                        translabel.place(x=0, y=40)

                        transcriteria = Frame(transactionsearch, width=452, height=402, bd=1, relief=RIDGE)
                        transcriteria.place(x=3, y=80)

                        transfirst = Frame(transcriteria, width=450, height=50, relief=RIDGE, bd=1, bg='floral white')
                        transfirst.place(x=0, y=0)

                        transfirstlabel = Label(transfirst, text="Search Criteria",
                                                font=("open sans", 14), bg="floral white")
                        transfirstlabel.place(x=0, y=20)

                        transsecond = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transsecond.place(x=0, y=50)

                        transsecondlabel = Label(transsecond, text="Transaction ID", font=("open sans", 13))
                        transsecondlabel.place(x=1, y=20)

                        transsecond2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                        transsecond2.place(x=225, y=50)

                        transsecentry = Entry(transsecond2, width=20, bd=0, font=("open sans", 13))
                        transsecentry.place(x=0, y=15)

                        transthird = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transthird.place(x=0, y=100)

                        transthirdlabel = Label(transthird, text="Description", font=("open sans", 13))
                        transthirdlabel.place(x=1, y=20)

                        transthird2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                        transthird2.place(x=225, y=100)

                        transthirdentry = Entry(transthird2, width=20, bd=0, font=("open sans", 13))
                        transthirdentry.place(x=0, y=15)

                        transfour = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transfour.place(x=0, y=150)

                        transfourlabel = Label(transfour, text="Date From", font=("open sans", 13))
                        transfourlabel.place(x=1, y=20)

                        transfour2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1,bg="white")
                        transfour2.place(x=225, y=150)

                        transcal = DateEntry(transfour2, selectmode='', width=22,
                                        font=('times new roman', 14), justify=LEFT, bd=0,date_pattern='y-mm-dd')
                        transcal.place(x=0, y=21)

                        transfive = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transfive.place(x=0, y=200)

                        transfivelabel = Label(transfive, text="Date To", font=("open sans", 13))
                        transfivelabel.place(x=1, y=20)

                        transfive2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1,bg="white")
                        transfive2.place(x=225, y=200)

                        transcal2 = DateEntry(transfive2, selectmode='', width=22,
                                        font=('times new roman', 14), justify=LEFT, bd=0,date_pattern='y-mm-dd')
                        transcal2.place(x=0, y=21)

                        transsix = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transsix.place(x=0, y=250)

                        transsixlabel = Label(transsix, text="Payment Type", font=("open sans", 13))
                        transsixlabel.place(x=1, y=20)

                        transsix2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transsix2.place(x=225, y=250)

                        transseven = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transseven.place(x=0, y=300)

                        transsevenlabel = Label(transseven, text="Total Amount", font=("open sans", 13))
                        transsevenlabel.place(x=1, y=20)

                        transseven2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transseven2.place(x=225, y=300)

                        transeight = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transeight.place(x=0, y=350)

                        transeightlabel = Label(transeight, text="Vendor ID", font=("open sans", 13))
                        transeightlabel.place(x=1, y=20)

                        transeight2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transeight2.place(x=225, y=350)

                        transnine = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transnine.place(x=0, y=400)

                        transninelabel = Label(transnine, text="Type", font=("open sans", 13))
                        transninelabel.place(x=1, y=20)

                        transnine2 = Frame(transcriteria, width=225, height=50, relief=RIDGE, bd=1)
                        transnine2.place(x=225, y=400)

                        # =============================Treeview++++++++++++++++++++++++++++++++
                        def connection():
                            config = {
                                "user": "root",
                                "password" : " ",
                                "host":  "localhost",
                                "database": "retail-system2"
                            }
                            try:
                                c = mysql.connect(**config)
                                return c
                            except:
                                print ("connection error")



                        def update(rows):
                            try:

                                trv1.delete(*trv1.get_children())
                                for i in rows:
                                    trv1.insert('','end',values=i)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')




                        def search():

                            try:
                                mydb = mysql.connect(host=host_address, user="root", password="",
                                                     database="retail-system2")
                                cursor = mydb.cursor()
                                date_cal = str(transcal.get())
                                date_cal2 = str(transcal2.get())

                                cursor.execute("SELECT * FROM `transaction` WHERE `transaction_id` LIKE '"+transsecentry.get()+"'  AND `date_recorded` BETWEEN '"+ date_cal +"' AND '"+ date_cal2 +"'")
                                transrows = cursor.fetchall()
                                print(transrows)
                                update(transrows)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')





                        mydb = mysql.connect(host=host_address, user="root", password="", database="retail-system2")
                        cursor = mydb.cursor()

                        wrapper1 = Label(transactionsearch, width=500, height=50)
                        wrapper1.place(x=455, y=80)

                        current = str(datetime.now().strftime("%Y-%m-%d"))

                        trv1 = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5,6,7), show="headings",
                                            height=26)
                        trv1.place(x=0, y=0)

                        trv1.column("1", anchor=CENTER, stretch=NO, width=150)
                        trv1.column("2", anchor=CENTER, stretch=NO, width=150)
                        trv1.column("3", anchor=CENTER, stretch=NO, width=150)
                        trv1.column("4", anchor=CENTER, stretch=NO, width=150)
                        trv1.column("5", anchor=CENTER, stretch=NO, width=150)
                        trv1.column("6",  anchor=CENTER, stretch=NO, width=150)
                        trv1.column("7",  anchor=CENTER, stretch=NO, width=150)

                        trv1.heading(1, text="Transaction ID")
                        trv1.heading(2, text="Customer ID")
                        trv1.heading(3, text="Payment Type")
                        trv1.heading(4, text="Total Amount")
                        trv1.heading(5, text="Amount Tendered")
                        trv1.heading(6, text="Bank Account Name")
                        trv1.heading(7, text="Date")

                        cursor.execute("select * from transaction where date_recorded = '" + current + "'")
                        transrows = cursor.fetchall()
                        update(transrows)


                        def view_sales():

                            try:

                                def update(salesrows):
                                    salestrv1.delete(*salestrv1.get_children())
                                    for i in salesrows:
                                        salestrv1.insert('', 'end', values=i)

                                sales_view = Tk()
                                sales_view.geometry("1350x750")
                                sales_view.title('WiRi RETAIL SYSTEMS v1.0.1')
                                sales_view.iconbitmap(r'titlelogo.ico')
                                sales_view.resizable(0, 0)

                                item = trv1.focus()
                                sales_items = trv1.item(item, "values")

                                trans_id = sales_items[0]
                                trans_total = main_currency + sales_items[3]
                                trans_type = sales_items[2]
                                invoice_id = "INV0000000" + trans_id

                                def refund():

                                    try:

                                        logoutwin = Tk()
                                        logoutwin.geometry('450x400+440+150')
                                        logoutwin.iconbitmap(r'titlelogo.ico')
                                        logoutwin.resizable(0, 0)
                                        logoutwin.overrideredirect(1)
                                        logoutwin.configure(background="cadetblue")

                                        def yes():
                                            logoutwin.destroy()
                                            con = mysql.connect(host=host_address, user='root', password="",
                                                                database="retail-system2")
                                            cursor = con.cursor()
                                            cursor.execute(
                                                "select quantity from sales where invoice_id ='" + trans_id + "' ")
                                            main_sales = cursor.fetchall()
                                            for i in range(len(main_sales)):
                                                cursor.execute(
                                                    "select product_id from sales where invoice_id ='" + trans_id + "' ")
                                                main_id = cursor.fetchall()
                                                for i in range(len(main_id)):
                                                    con = mysql.connect(host=host_address, user='root', password="",
                                                                        database="retail-system2")
                                                    cursor = con.cursor()
                                                    cursor.execute(
                                                        "update product set unit_in_stock= unit_in_stock + '" + str(
                                                            main_sales[i][0]) + "' where product_id='" + str(
                                                            main_id[i][0]) + "'")
                                                    cursor.execute("DELETE FROM `transaction` WHERE `transaction`.`transaction_id` = '"+trans_id+"' ")

                                                    con.close()
                                                    sales_view.destroy()

                                        def no():
                                            logoutwin.destroy()

                                        trade_label = Label(logoutwin, text="WiRi Retail***", font=("cansalas", 14),
                                                            bg="cadetblue")
                                        trade_label.place(x=5, y=10)

                                        warn_label = Label(logoutwin, text="ARE YOU SURE YOU WOULD LIKE TO",
                                                           font=("georgia", 15, "bold"), bg="cadetblue")
                                        warn_label.place(x=5, y=70)

                                        warn_label = Label(logoutwin, text="REFUND THE SALE?",
                                                           font=("georgia", 15, "bold"), bg="cadetblue")
                                        warn_label.place(x=5, y=100)

                                        yes_butt = Button(logoutwin, text="Yes", width=7, height=3,
                                                          font=("georgia", 14), command=yes)
                                        yes_butt.place(x=50, y=280)

                                        no_butt = Button(logoutwin, text="No", width=7, height=3,
                                                         font=("georgia", 14), command=no)
                                        no_butt.place(x=300, y=280)

                                    except Exception as es:
                                        messagebox.showerror('Error', f'Error due to: {str(es)}')




                                salesframe = Frame(sales_view, width=1350, height=80, bg='lightblue')
                                salesframe.place(x=0, y=0)

                                saleslabel = Label(salesframe, text="Transaction Search", font=("open sans", 20),
                                                 bg='lightblue')
                                saleslabel.place(x=0, y=40)

                                salescriteria = Frame(sales_view, width=452, height=402, bd=1, relief=RIDGE)
                                salescriteria.place(x=3, y=80)

                                salesfirst = Frame(salescriteria, width=450, height=50, relief=RIDGE, bd=1, bg='floral white')
                                salesfirst.place(x=0, y=0)

                                salesfirstlabel = Label(salesfirst, text="Search Criteria", font=("open sans", 14), bg="floral white")
                                salesfirstlabel.place(x=0, y=20)

                                salessecond = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salessecond.place(x=0, y=50)

                                secondlabel = Label(salessecond, text="Transaction ID", font=("open sans", 13))
                                secondlabel.place(x=1, y=20)

                                salessecond2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salessecond2.place(x=225, y=50)

                                secondlabel = Label(salessecond2, text=invoice_id, font=("open sans", 13),fg="red")
                                secondlabel.place(x=10, y=20)

                                salesthird = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesthird.place(x=0, y=100)

                                salesthirdlabel = Label(salesthird, text="Description", font=("open sans", 13))
                                salesthirdlabel.place(x=1, y=20)

                                salesthird2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                                salesthird2.place(x=225, y=100)

                                salesthirdentry = Entry(salesthird2, width=20, bd=0, font=("open sans", 13))
                                salesthirdentry.place(x=0, y=15)

                                salesfour = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesfour.place(x=0, y=150)

                                salesfourlabel = Label(salesfour, text="Date From", font=("open sans", 13))
                                salesfourlabel.place(x=1, y=20)

                                salesfour2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                                salesfour2.place(x=225, y=150)

                                salescal = DateEntry(salesfour2, selectmode='day', width=22,
                                                font=('times new roman', 14), justify=LEFT, bd=0)
                                salescal.place(x=0, y=21)

                                salesfive = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesfive.place(x=0, y=200)

                                salesfivelabel = Label(salesfive, text="Date To", font=("open sans", 13))
                                salesfivelabel.place(x=1, y=20)

                                salesfive2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1, bg="white")
                                salesfive2.place(x=225, y=200)

                                salescal2 = DateEntry(salesfive2, selectmode='day', width=22,
                                                 font=('times new roman', 14), justify=LEFT, bd=0)
                                salescal2.place(x=0, y=21)

                                salessix = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salessix.place(x=0, y=250)

                                salessixlabel = Label(salessix, text="Payment Type", font=("open sans", 13))
                                salessixlabel.place(x=1, y=20)

                                salessix2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salessix2.place(x=225, y=250)

                                salessixlabel2 = Label(salessix2, text=trans_type, font=("open sans", 13),fg="red")
                                salessixlabel2.place(x=10, y=20)

                                salesseven = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesseven.place(x=0, y=300)

                                salessevenlabel = Label(salesseven, text="Total Amount", font=("open sans", 13))
                                salessevenlabel.place(x=1, y=20)

                                salesseven2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesseven2.place(x=225, y=300)

                                salessevenlabel2 = Label(salesseven2, text=trans_total, font=("open sans", 13),fg="red")
                                salessevenlabel2.place(x=10, y=20)

                                saleseight = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                saleseight.place(x=0, y=350)

                                saleseightlabel = Label(saleseight, text="Vendor ID", font=("open sans", 13))
                                saleseightlabel.place(x=1, y=20)

                                saleseight2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                saleseight2.place(x=225, y=350)

                                salesnine = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesnine.place(x=0, y=400)

                                salesninelabel = Label(salesnine, text="Type", font=("open sans", 13))
                                salesninelabel.place(x=1, y=20)

                                salesnine2 = Frame(salescriteria, width=225, height=50, relief=RIDGE, bd=1)
                                salesnine2.place(x=225, y=400)

                                mydb = mysql.connect(host=host_address, user="root", password="", database="retail-system2")
                                cursor = mydb.cursor()

                                saleswrapper = Label(sales_view, width=500, height=50)
                                saleswrapper.place(x=455, y=80)

                                salestrv1 = ttk.Treeview(saleswrapper, columns=(1, 2, 3, 4, 5, 6, 7), show="headings",
                                                    height=26)
                                salestrv1.place(x=0, y=0)

                                salestrv1.column("1", anchor=CENTER, stretch=NO, width=150)
                                salestrv1.column("2", anchor=CENTER, stretch=NO, width=150)
                                salestrv1.column("3", anchor=CENTER, stretch=NO, width=150)
                                salestrv1.column("4", anchor=CENTER, stretch=NO, width=150)
                                salestrv1.column("5", anchor=CENTER, stretch=NO, width=150)
                                salestrv1.column("6", anchor=CENTER, stretch=NO, width=150)
                                salestrv1.column("7", anchor=CENTER, stretch=NO, width=150)

                                salestrv1.heading(1, text="Sales ID")
                                salestrv1.heading(2, text="Transaction ID")
                                salestrv1.heading(3, text="Description")
                                salestrv1.heading(4, text="Quantity")
                                salestrv1.heading(5, text="Unit Price")
                                salestrv1.heading(6, text="Sub Total")
                                salestrv1.heading(7, text="Date")

                                cursor.execute("select * from sales where invoice_id = '"+trans_id+"'")
                                salesrows = cursor.fetchall()
                                for i in range(len(salesrows)):
                                    salesrows[i] = list(salesrows[i])
                                    spro_ids = str(salesrows[i][2])
                                    cursor.execute("select name from product where product_id = '"+spro_ids+"' ")
                                    ids = cursor.fetchall()
                                    for j in range(len(ids)):
                                        salesrows[i][2] = ids[j][0]

                                update(salesrows)



                                salessearchbutt = Frame(sales_view, width=1350, height=105, bg="cadetblue")
                                salessearchbutt.place(x=0, y=630)

                                def closesalessearch():
                                    sales_view.destroy()

                                salesposbut1 = Button(salessearchbutt, width=13, height=7, text=("Sale\n""Refund"),
                                                 font=('open sans', 10), command=refund)
                                salesposbut1.place(x=0, y=2)

                                salesposbut2 = Button(salessearchbutt, width=13, height=7, text=("Sale\n""Exchange"),
                                                 font=('open sans', 10), command=None)
                                salesposbut2.place(x=120, y=2)

                                salesposbut3 = Button(salessearchbutt, width=13, height=7, text=("Sale\n""Payment"),
                                                 font=('open sans', 10), command=None)
                                salesposbut3.place(x=240, y=2)

                                salesposbut4 = Button(salessearchbutt, width=13, height=7, text=("Special Order\n""Edit"),
                                                 font=('open sans', 10),state=DISABLED)
                                salesposbut4.place(x=360, y=2)

                                salesposbut5 = Button(salessearchbutt, width=13, height=7, text=("Special Order\n""Payment"),
                                                 font=('open sans', 10),state=DISABLED)
                                salesposbut5.place(x=480, y=2)

                                salesposbut6 = Button(salessearchbutt, width=13, height=7, text=("Fulfillment"),
                                                 font=('open sans', 10),state=DISABLED)
                                salesposbut6.place(x=600, y=2)

                                salesposbut7 = Button(salessearchbutt, width=13, height=7, text=("Layway"),
                                                 font=('open sans', 10),state=DISABLED)
                                salesposbut7.place(x=720, y=2)

                                salesposbut8 = Button(salessearchbutt, width=13, height=7, text=("Print Transaction"),
                                                 font=('open sans', 10))
                                salesposbut8.place(x=840, y=2)

                                asalesposbut9 = Button(salessearchbutt, width=13, height=7, text=("F9\n""View\n""Inventory"),
                                                 font=('open sans', 10))
                                #asalesposbut9.place(x=960, y=2)

                                salesposbut10 = Button(salessearchbutt, width=13, height=7, text=("F10\n""Ok"),
                                                  font=('open sans', 10), command=None)
                                salesposbut10.place(x=1080, y=2)

                                salesposbut11 = Button(salessearchbutt, width=17, height=7, text=("F11\n""Cancel"),
                                                  font=('open sans', 10), command=closesalessearch)
                                salesposbut11.place(x=1200, y=2)

                            except Exception as es:
                                messagebox.showerror('Error', f'Error due to: {str(es)}')



##############################################################BACK TO TRANSACTION SEARCH#############################################################



                        transsearcbutf = Frame(transactionsearch, width=1350, height=105, bg="cadetblue")
                        transsearcbutf.place(x=0, y=630)

                        def closetranssearch():
                            transactionsearch.destroy()

                        transposbut1 = Button(transsearcbutf, width=13, height=7, text=("F1\n""Search"),
                                         font=('open sans', 10), command=search)
                        transposbut1.place(x=0, y=2)

                        transposbut2 = Button(transsearcbutf, width=13, height=7, text=("F2\n""Clear"),
                                         font=('open sans', 10), command=None)
                        transposbut2.place(x=120, y=2)

                        transposbut3 = Button(transsearcbutf, width=13, height=7, text=("F3\n""New"),
                                         font=('open sans', 10), command=None)
                        transposbut3.place(x=240, y=2)

                        transposbut4 = Button(transsearcbutf, width=13, height=7, text=("F4\n""Edit"),
                                         font=('open sans', 10))
                        transposbut4.place(x=360, y=2)

                        transposbut5 = Button(transsearcbutf, width=13, height=7, text=("F5\n""Delete"),
                                         font=('open sans', 10))
                        transposbut5.place(x=480, y=2)

                        transposbut6 = Button(transsearcbutf, width=13, height=7, text=("F6\n""View"),
                                         font=('open sans', 10))
                        transposbut6.place(x=600, y=2)

                        transposbut7 = Button(transsearcbutf, width=13, height=7, text=("F7\n""Serial\n""Numbers"),
                                         font=('open sans', 10))
                        transposbut7.place(x=720, y=2)

                        transposbut8 = Button(transsearcbutf, width=13, height=7, text=("F8\n""Batch\n""Numbers"),
                                         font=('open sans', 10))
                        transposbut8.place(x=840, y=2)

                        transposbut9 = Button(transsearcbutf, width=13, height=7, text=("F9\n""View\n""Inventory"),
                                         font=('open sans', 10))
                        transposbut9.place(x=960, y=2)

                        transposbut10 = Button(transsearcbutf, width=13, height=7, text=("F10\n""Ok"),
                                          font=('open sans', 10), command=view_sales)
                        transposbut10.place(x=1080, y=2)

                        trasnposbut11 = Button(transsearcbutf, width=17, height=7, text=("F11\n""Cancel"),
                                          font=('open sans', 10), command=closetranssearch)
                        trasnposbut11.place(x=1200, y=2)



                    except Exception as es:
                        messagebox.showerror('Error', f'Error due to: {str(es)}')



######################################################################SUSPEND/RECALL####################################################################################







########################################################################BACK TO MAIN WINDOW#############################################################################


                posbut1 = Button(butframe,width=13,height=7,text=("F1\n""Transaction\n""Mode"),font=('open sans',10),command=transaction)
                posbut1.place(x=0,y=0)

                #lab=Label(posbut1,text=("F1\n""Transaction\n""Mode"),font=('times new roman',14))
                #lab.place(x=0,y=0)

                posbut2 = Button(butframe, width=13, height=7,text=("F2\n""Customer\n""Search"),font=('open sans',10),command=custsearch)
                posbut2.place(x=120, y=0)

                posbut3 = Button(butframe, width=13, height=7,text=("F3\n""Product\n""Search"),font=('open sans',10),command=prosearch)
                posbut3.place(x=240, y=0)

                posbut4 = Button(butframe, width=13, height=7,text=("F4\n""Sale\n""Edit"),font=('open sans',10))
                posbut4.place(x=360, y=0)

                posbut5 = Button(butframe, width=13, height=7,text=("F5\n""Transaction\n""Search"),font=('open sans',10),command=transearch)
                posbut5.place(x=480, y=0)

                posbut6 = Button(butframe, width=13, height=7,text=("F6\n""Fulfillment"),font=('open sans',10))
                posbut6.place(x=600, y=0)

                posbut7 = Button(butframe, width=13, height=7,text=("F7\n""Void\n""Item"),font=('open sans',10),command=voiditem)
                posbut7.place(x=720, y=0)

                posbut8 = Button(butframe, width=13, height=7,text=("F8\n""Void\n""Sale"),font=('open sans',10),command=voidsale)
                posbut8.place(x=840, y=0)

                posbut9 = Button(butframe, width=13, height=7,text=("F9\n""Suspend\n""/Recall"),font=('open sans',10), command=None)
                posbut9.place(x=960, y=0)

                posbut10 = Button(butframe, width=13, height=7,text=("F10\n""Quick\n""Payments-Cash"),font=('open sans',10), command=None)
                posbut10.place(x=1080, y=0)

                posbut11 = Button(butframe, width=17, height=7,text=("F11\n""Payments\n"),font=('open sans',10),command=payments)
                posbut11.place(x=1200, y=0)

                posbut12 = Button(butframe, width=20, height=100)
                #posbut12.place(x=1320, y=

                salelabel = Label(w,text="SALE",font=("open sans",18),bg="grey",width=25,justify=LEFT)
                salelabel.place(x=1000,y=94)

                customerframe = Frame(w,width=350,height=450)
                customerframe.place(x=1000,y=130)

                imglogo6 = ImageTk.PhotoImage(Image.open('customersmall.jpg'))
                logo_label4 = Label(customerframe, image=imglogo6)
                logo_label4.place(x=2, y=1)

                customerlabel = Label(customerframe,text="Customer Information",font=("open sans",12,"bold"))
                customerlabel.place(x=2,y=80)

                backframe = Frame(customerframe,width=350,height=100,bd=5,bg='white')
                backframe.place(x=0,y=110)

                idframe = Frame(backframe,width=340,height=2,bg='black')
                idframe.place(x=0,y=0)

                idframe2 = Frame(backframe, width=2, height=90, bg='black')
                idframe2.place(x=0, y=0)

                idframe3 = Frame(backframe, width=2, height=90, bg='black')
                idframe3.place(x=340, y=0)

                idframe4 = Frame(backframe, width=340, height=2, bg='black')
                idframe4.place(x=0, y=90)

                idframe5 = Frame(backframe, width=340, height=2, bg='black')
                idframe5.place(x=0, y=22)

                idframe6 = Frame(backframe, width=340, height=2, bg='black')
                idframe6.place(x=0, y=44)

                idframe7 = Frame(backframe, width=340, height=2, bg='black')
                idframe7.place(x=0, y=66)

                idlabel = Label(backframe,text="Id",font=("open sans",8),bg="white")
                idlabel.place(x=2,y=2)

                namelabel = Label(backframe, text="Name", font=("open sans", 8), bg="white")
                namelabel.place(x=2, y=24)

                descriptionlabel = Label(backframe, text="Description", font=("open sans", 8), bg="white")
                descriptionlabel.place(x=2, y=46)

                contactlabel = Label(backframe, text="Phone Number", font=("open sans", 8), bg="white")
                contactlabel.place(x=2, y=68)

                fish = Label(backframe,text='hey',font=("open sans",20),width=10,fg='white')
                #fish.place(x=10,y=68)

                fish2 = Label(backframe, text='Cash Customer', font=("open sans", 8), bg="white")
                fish2.place(x=180, y=46)

                fish3 = Label(backframe, text='Cash Customer', font=("open sans", 8), bg="white")
                fish3.place(x=180, y=24)

                fish4 = Label(backframe, text="CUS000001", font=("open sans", 8), bg="white")
                fish4.place(x=180, y=2)

                searchframe = Frame(w, width=400, height=80, bg='grey')
                searchframe.place(x=1000, y=560)

                searchframe2 = Frame(searchframe,width=255,height=76,bg='white')
                searchframe2.place(x=0,y=2)

                searchbar = Entry(searchframe2,width=225,font=("open sans",15,"bold"),bd=0)
                searchbar.place(x=2,y=28)

                imglogo5 = ImageTk.PhotoImage(Image.open('keyboardimagesmall.png'))
                #logo_label4 = Label(searchframe, image=imglogo5, bg='lightblue')
                #logo_label4.place(x=259, y=2)

                keybutt = Button(searchframe,image=imglogo5,bg='lightblue')
                keybutt.place(x=259,y=2)

                w.bind('<F8>', voidsale)
                w.bind('<F3>', prosearch)
                w.bind('<F7>', voiditem)
                w.bind('<F5>', transearch)
                w.bind('<F11>', payments)
                w.bind('<F2>', custsearch)
                w.after(10, addupdate_main)





        except Exception as es:
            messagebox.showerror('Error',f'Error due to: {str(es)}')



loginbut = Button(lg, text='LOGIN', width=20, height=2,command=login)
loginbut.place(x=210, y=400)
q.bind('<Return>',login)

q.mainloop()