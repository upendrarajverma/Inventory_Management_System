#PROJECT OF INVENTORY MANAGEMENT SYSTEM
import creating_database
creating_database.CreateDatabase()
creating_database.table()
import os
import item
import customer
import transaction
import report
import pyttsx3
import maskpass
def speak(text,gender):
    speaker=pyttsx3.init()
    voices=speaker.getProperty('voices')
    speaker.setProperty('rate', 160)
    speaker.setProperty('voice', voices[gender].id)
    speaker.say(text)
    speaker.runAndWait()
password='lnct'
print('''
                                +--------------------------------------------+
                                |            Welcome To Login Window         |
                                +--------------------------------------------+         
''')
for i in range(3):
    pass1=maskpass.askpass(prompt="\t\t\t\t\t\tEnter Password :-",mask="*")
    if(pass1.lower()==password):
        speak("Authentication Success...!",1)
        break
    else:
        print("\t\t\t\t\t\t\tWrong Password")
        speak("wrong password...!",1)
        if(i==2):
            speak("Sorry...Please try again later!",1)
            exit()
        
while(True):
    os.system('cls')
    print("="*119)
    print("\t\t\t\t\tWelcome To Inventory Management System")
    print("="*119)
    print('''
                                    1. Item Management Section
                                    2. Customer Management Section
                                    3. Transaction Management Section
                                    4. Report Management Section
                                    5. Exit
    ''')
    print("="*119)
    speak("welcome...!",1)
    ch=(int(input("Enter Your Choice :- ")))
    print("="*119)
    if(ch==1):
        while(True):
            print('''
                                    1. Add Item
                                    2. Search item
                                    3. Delete item
                                    4. Change Item Rate
                                    5. Edit Item
                                    6. Exit
            ''')
            print("="*119)
            ch=(int(input("Enter Your Choice :- ")))
            print("="*119)
            if(ch==1):
                item.add_item()
            elif(ch==2):
                item.search_item()
            elif(ch==3):
                item.delete_item()
            elif(ch==4):
                item.change_item_rate()
            elif(ch==5):
                item.Edit_Item()
            elif(ch==6):
                break
    elif(ch==2):
        while(True):
            print("="*119)
            print('''
                                    1. Add Customer
                                    2. Delete Customer
                                    3. Search Customer
                                    4. Edit Customer
                                    5. Exit
            ''')
            print("="*119)
            ch=(int(input("Enter Your Choice :- ")))
            print("="*119)
            if(ch==1):
                customer.Add_Customer()
            elif(ch==2):
                customer.Delete_Customer()
            elif(ch==3):
                customer.Search_Customer()
            elif(ch==4):
                customer.Edit_Customer()
            elif(ch==5):
                break
    elif(ch==3):
        while(True):
            print("="*119)
            print('''
                                    1. Sale Counter
                                    2. Purchase Counter
                                    3. Exit
            ''')
            print("="*119)
            ch=(int(input("Enter Your Choice :- ")))
            print("="*119)
            if(ch==1):
                transaction.Sale_Counter()
            elif(ch==2):
                transaction.Purchase_Counter()
            elif(ch==3):
                break
    elif(ch==4):
        while(True):
            print("="*119)
            print('''
                                    1. Item Details
                                    2. Customer Details
                                    3. Sale Details
                                    4. Purchase Details
                                    5. Exit
            ''')
            print("="*119)
            ch=(int(input("Enter Your Choice :- ")))
            print("="*119)
            if(ch==1):
                report.Item_Details()
            elif(ch==2):
                report.Customer_Details()
            elif(ch==3):
                report.Sale_Details()
            elif(ch==4):
                report.Purchase_Details()
            elif(ch==5):
                break
    elif(ch==5):
        break
