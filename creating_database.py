import mysql.connector

def CreateDatabase():
    cnx = mysql.connector.connect(user='root', password='lnct', host='localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS inventorysoft")
    Cursor.execute("")
    Cursor.close()
    cnx.close()


def table():
    cnx = mysql.connector.connect(user='root',password='lnct',host='localhost',database='inventorySoft')
    cursor=cnx.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Item(INO INT(20), INAME VARCHAR(50),CP FLOAT,SP FLOAT,QTY INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Customer(CID INT(20), CNAME VARCHAR(50),CADD VARCHAR(100),CMO NUMERIC(10))")
    cursor.execute("CREATE TABLE IF NOT EXISTS SaleDetails(INO INTEGER, CID INTEGER,INAME VARCHAR(50),QTY INTEGER,DATE VARCHAR(15),TA NUMERIC(8,2))")
    cursor.execute("CREATE TABLE IF NOT EXISTS PurchaseDetails(INO INT(20),INAME VARCHAR(50),QTY INT, DATE DATE,TA FLOAT,PID INT)")
    cursor.execute("")
    cursor.close()
    cnx.close()
    
