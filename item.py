import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
cnx = mysql.connector.connect(user='root', password='lnct', host='localhost',database='inventorysoft')
Cursor = cnx.cursor()

def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))
        
def add_item():
    try:
        no=int(input("Enter the Item No. :- "))
        name=input("Enter the Item Name :- ")
        prate=int(input("Enter the Purchase Rate :- "))
        srate=int(input("Enter the selling Rate :- "))
        q=int(input("Enter the Quantity :- "))
        Cursor.execute("INSERT INTO ITEM VALUES({},'{}',{},{},{});".format(no,name,prate,srate,q))
        cnx.commit()
        print("Item Added")
    except:
        print("Wrong Entry....Please Check Details.!")

def search_item():
    try:
        no = input("Enter Item No to search : ")
        query = ("SELECT * FROM item WHERE ino = %s ")
        rec_srch = (no,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(INO, INAME, CP, SP, QTY) in Cursor:
            Rec_count += 1
            print("-"*80)
            print("Item NO. -       Item Name     -     Cost Price  -     Selling Price  -  Quantity ")
            print(" ",INO," "*10,INAME," "*10," ",CP," "*10,SP," "*8,QTY)
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        if(Rec_count==0):
            print("Record Not Found..!")
        cnx.commit()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def delete_item():
    try:
        no=int(input("Enter the Item No. :- "))
        Cursor.execute("delete from item where ino={}".format(no))
        cnx.commit()
        print("Iten deleted from your record.")
    except:
        print("Plese Enter Valid Ino.")

        
def change_item_rate():
    try:
        no=int(input("Enter the Item No. :- "))
        prate=int(input("Enter new purchase rate :-"))
        srate=int(input("Enter new selling rate :-"))
        Cursor.execute("update item set cp={},sp={} where ino={}".format(prate,srate,no))
        cnx.commit()
        print("Iten rate updated.")
    except:
        print("Plese Enter Valid Ino.")


def Edit_Item():
    try:
        no=int(input("Enter the Item No. :- "))
        name=input("Enter new item name :-")
        Cursor.execute("update item set iname='{}' where ino={}".format(name,no))
        cnx.commit()
        print("Iten name updated.")
    except:
        print("Plese Enter Valid Ino.")
        
        
