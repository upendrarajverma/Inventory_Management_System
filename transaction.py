import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
cnx = mysql.connector.connect(user='root', password='lnct', host='localhost',database='inventorySoft')
cursor = cnx.cursor()

cost_price=0
sale_price=0
def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))
        
def Sale_Counter():
    try:
        global cost_price,sale_price
        cnx = mysql.connector.connect(user='root', password='lnct', host='localhost',database='inventorySoft')
        cursor = cnx.cursor()  
        dd=date.today()
        no=int(input("Enter the customer id :- "))
        query = ("SELECT * FROM customer WHERE CID = %s ")
        rec_srch =(no,)
        cursor.execute(query,rec_srch)
        for(CID,CNAME,CADD,CMO) in cursor:
            temp=CID
            cn=CNAME
            if(temp==no):
                q1=("SELECT * FROM ITEM")
                cursor.execute(q1)
                for(INO,INAME,CP,SP,QTY) in cursor:
                    sale=SP
                    cost_price=CP
                    sale_price=SP
                    print("Item NO. -    Item Name     -  Selling Price  -    Quantity ")
                    print(" ",INO," "*5,INAME," "*10,SP," "*8,QTY)
                it=int(input("Enter the item no :- "))
                q2=("SELECT * FROM ITEM WHERE INO=%s")
                val=(it,)
                cursor.execute(q2,val)
                for(INO,INAME,CP,SP,QTY) in cursor:
                    IN=INAME
                    S=SP
                    old_qty=QTY
                q=int(input("Enter no. of quantity :- "))
                m=q*S
                new_qty=old_qty-q
                q2=("INSERT INTO saledetails VALUES(%s, %s, %s, %s, %s, %s)")
                val=(it,no,IN,q,dd,m)
                cursor.execute(q2,val)
                cnx.commit()
                print("Item Sold....!")
                q3=("update item set qty=%s where ino=%s")
                val=(new_qty,it)
                cursor.execute(q3,val)
                cnx.commit()
            else:
                print("Customer Not found.....!")
        cnx.commit()
    except:
        print("Somthing Went Wrong.....!")
def Purchase_Counter():
    try:
        global cost_price,sale_price
        cnx = mysql.connector.connect(user='root', password='lnct', host='localhost',database='inventorySoft')
        cursor = cnx.cursor()
        dd=date.today()
        it=int(input("Enter item no:- "))
        q3=("SELECT * FROM ITEM WHERE INO=%s")
        val4=(it,)
        cursor.execute(q3,val4)
        r=cursor.fetchone()
        if (r==None):
            itname=input("Enter item name:- ")
            cpp=int(input("Enter the CP:- "))
            spp=int(input("Enter the CP:- "))
            qt=int(input("Enter Quantity :- "))
            total_amount=qt*cpp
            purchase_id=int(input("Enter purchase id:- "))
            q=("insert into purchasedetails values(%s,%s,%s,%s,%s,%s)")
            val=(it,itname,qt,dd,total_amount,purchase_id)
            cursor.execute(q,val)
            q2=("insert into item values(%s,%s,%s,%s,%s)")
            val2=(it,itname,cpp,spp,qt)
            cursor.execute(q2,val2)
            cnx.commit()
        else:
            cpp=r[2]
            itname=r[1]
            print("Item name is :-",itname)
            qt=int(input("Enter Quantity :- "))
            total_amount=qt*cpp
            purchase_id=int(input("Enter purchase id:- "))
            q=("insert into purchasedetails values(%s,%s,%s,%s,%s,%s)")
            val=(it,itname,qt,dd,total_amount,purchase_id)
            cursor.execute(q,val)
            cnx.commit()
            q1=("SELECT * FROM ITEM WHERE INAME=%s")
            val2=(itname,)
            cursor.execute(q1,val2)
            old_qty=0
            for(INO,INAME,CP,SP,QTY) in cursor:
                old_qty=QTY
            new_qty=old_qty+qt
            q2=("update item set qty=%s where ino=%s")
            val3=(new_qty,it)
            cursor.execute(q2,val3)
            cnx.commit()
        print("Item purchased and stock updated successfully..!")
    except:
        print("Somthing went wrong...!")
