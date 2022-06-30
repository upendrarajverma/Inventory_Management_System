import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
cnx = mysql.connector.connect(user='root', password='lnct', host='localhost',database='inventorySoft')
cursor = cnx.cursor()
def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))
def Add_Customer():
    try:
        idd=int(input("Enter the Customer ID :- "))
        name=input("Enter the Customer Name :- ")
        add=input("Enter the Customer Address :- ")
        mob=int(input("Enter the Customer Mobile :- "))
        cursor.execute("insert into customer values({},'{}','{}',{});".format(idd,name,add,mob))
        cnx.commit()
        print("Customer Added..!")
    except:
        print("Wrong entry...Please fill proper details...!")
                
def Delete_Customer():
    try:
        idd=int(input("Enter the Customer Id :- "))
        cc=input("Do You Want to Delete Y/N :-")
        if(cc=='Y' or cc=='y'):
            cursor.execute("delete from customer where cid={}".format(idd))
            cnx.commit()
            print("Customer Deleted Successfully..!")
        else:
            print("Thanks for confirmation...!")
    except:
        print("Wrong Details....Please check..!")


def Search_Customer():
    try:
        no = input("Enter customer ID to search : ")
        query = ("SELECT * FROM customer WHERE cid = %s ")
        rec_srch = (no,)
        cursor.execute(query, rec_srch)
        Rec_count = 0
        print("Customer ID -       Name     -      Addresss     -    Mobile  ")
        for(CID, CNAME, CADD, CMO) in cursor:
            Rec_count += 1
            print("-"*80)
            print(" ",CID," "*10,CNAME," "*10," ",CADD," "*10,CMO)
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Cusomer(s) found..!")
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
def Edit_Customer():
    try:
        no=int(input("Enter the Customer ID :- "))
        name=input("Enter new customer name :-")
        add=input("Enter new address :-")
        mob=int(input("Enter new mobile no :-"))
        cursor.execute("update customer set CNAME='{}',CADD='{}',CMO={} where CID={}".format(name,add,mob,no))
        cnx.commit()
        print("Customer updated successfully..!")
    except:
        print("Plese Enter Valid Customer ID...!")
