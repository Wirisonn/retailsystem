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
from reportlab.lib import pagesizes







# Creating Canvas
c = canvas.Canvas("testpdf.pdf", pagesize=pagesizes.A4, bottomup=0)

# Logo Section
# Setting th origin to (10,40)
c.translate(10, 40)
# Inverting the scale for getting mirror Image of logo
c.scale(1, -1)
# Inserting Logo into the Canvas at required position
c.drawImage("wilfa.jpg", 230, -80, width=130, height=120)

# Title Section
# Again Inverting Scale For strings insertion
c.scale(1, -1)
# Again Setting the origin back to (0,0) of top-left
c.translate(-10, -40)
# Setting the font for Name title of company
c.setFont("Helvetica-Bold", 10)

c.setFont("Helvetica-Bold", 14)
c.drawCentredString(300, 150, "EN 8, em Direcçã ao Mercado Waresta")
c.drawCentredString(300, 170, "Waresta - Nampula")
c.drawCentredString(300, 190, "Telefone: (+258)844892251")
c.drawCentredString(300, 210, "Cashier Nome: " + "Wilson")
c.setFont("Helvetica-Bold", 14)
c.drawCentredString(300, 230, "NUIT : 400387494")

c.line(20, 260, 570, 260)

c.setFont("Courier-Bold", 8)

c.setFont("Times-Bold", 13)
c.drawRightString(230, 295, "FACTURA No. :")
c.drawRightString(230, 325, "DATA & TEMPO :")
#c.drawRightString(70, 120, "CLIENTE ID :")
#c.drawRightString(70, 130, "TELEFONE   :")
c.line(35, 280, 535, 280)
#c.line(15, 95, 15, 135)
c.line(35, 310, 535, 310)
#c.line(185, 95, 185, 135)
c.line(35, 340, 535, 340)
c.line(35, 280, 35, 340)
c.line(535, 280, 535, 340)

yey = "GOODS DESCRIPTION"
c.line(20, 370, 570, 370)
c.setFont("Times-Bold", 11)
c.drawCentredString(35, 365, "SR No.")
c.drawCentredString(150, 365, yey)
c.drawCentredString(380, 365, "QTY")
c.drawCentredString(460, 365, "PRICE")
c.drawCentredString(550, 365, "TOTAL")

c.drawString(70, 830,
             "********************************* THANK YOU *********************************")
c.drawString(30, 750, "Payment Summary                |")
c.drawString(250, 750, "             Amount                                        |")
c.drawRightString(550, 750, "Tendered")
#c.line(15, 320, 185, 320)
#c.line(15, 330, 185, 330)
count = 175


c.showPage()
c.save()
file_name = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
# os.startfile('invoicemain12.pdf', 'print')