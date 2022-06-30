import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
cnx = mysql.connector.connect(user='root', password='lnct', host='localhost',database='inventorySoft')
cursor = cnx.cursor()

def Item_Details():
    try:
        query = ("SELECT * FROM item")
        cursor.execute(query)
        Rec_count = 0
        for(INO,INAME,CP,SP,QTY) in cursor:
            Rec_count += 1
            print("-"*80)
            print("Item NO. -    Item Name      -     Cost Price     -  Selling Price  -  Quantity ")
            print(" ",INO," "*5,INAME," "*7," ",CP," "*10,SP," "*12,QTY)
        print(Rec_count, "Item(s) found")
        if(Rec_count==0):
            print("Item Not Found..!")
        cnx.commit()
    except:
        print("Somthing Went Wrong..!")

def Customer_Details():
    try:
        query = ("SELECT * FROM customer")
        cursor.execute(query)
        Rec_count = 0
        for(CID,CNAME,CADD,CMO) in cursor:
            Rec_count += 1
            print("-"*80)
            print("Customer ID -   Customer Name      -   Address      -      Mobile ")
            print(" ",CID," "*10,CNAME," "*10," ",CADD," "*12,CMO)
        print(Rec_count, "Customer(s) found")
        if(Rec_count==0):
            print("Record Not Found..!")
        cnx.commit()
    except:
        print("Somthing went wrong...!")

def Sale_Details():
    try:
        query = ("SELECT * FROM saledetails")
        cursor.execute(query)
        Rec_count = 0
        for(INO,CID,INAME,QTY,DATE,TA) in cursor:
            Rec_count += 1
            print("-"*80)
            print("Item No -   Customer Id      -   Item Name      -      Quantity  -    Date   -      Total Amount   ")
            print(" ",INO," "*10,CID," "*10,INAME," "*5," "*7,QTY," "*7,DATE," "*5," "*5,TA)
        print(Rec_count, "Sale Record(s) found")
        if(Rec_count==0):
            print("No Sale Record Found..!")
        cnx.commit()
    except:
        print("Somthing went wrong...!")

def Purchase_Details():
    try:
        query = ("SELECT * FROM purchasedetails")
        cursor.execute(query)
        Rec_count = 0
        for(INO,INAME,QTY,DATE,TA,PID) in cursor:
            Rec_count += 1
            print("-"*80)
            print("Item No -   Seller Id      -   Item Name      -      Quantity  -       Date     -            Total Amount   ")
            print(" ",INO," "*5,PID," "*13,INAME," "*7," "*5,QTY," "*5," "*5,DATE," "*10," "*6,TA)
        print(Rec_count, "Purchase Record(s) found")
        if(Rec_count==0):
            print("No Purchase Record Found..!")
        cnx.commit()
    except:
        print("Somthing went wrong...!")
