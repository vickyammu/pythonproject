import datetime
import mysql.connector
atmdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atmc_db"
)
mycursor=atmdb.cursor()
print("$$$$welcome to nvs bank$$$\n\n^^^^^^^hand wash then use atm^^^^^^^^\n\n$$$$$$$ Insert your card$$$$$$")
abalance=5000
abbalance=50000
def balancechecking(acaccount,pin):
    sql="insert into balancecheck(acaccount,pin) Values(%s,%s)"
    Values=(acaccount,pin)
    mycursor.execute(sql,Values)
    atmdb.commit()
    x=datetime.datetime.now()
    f=open("bill.txt","w")
    f.write(f"your current balance is {abbalance} rupees \n {x}")
    print("data inserted successfully")
       
def deposite (status, number, amount,mobilenumber, receipt):
    sql="insert into deposite (status ,number ,amount ,mobilenumber,receipt) Value (%s,%s,%s,%s,%s)"
    value=(status,number,amount,mobilenumber,receipt)
    mycursor.execute(sql,value)
    atmdb.commit()
    finalbalance=amount+abalance
    x=datetime.datetime.now()
    f=open("bill.txt","w")
    f.write(f"your current balance is {finalbalance} rupees \n {x}\n{mobilenumber}")
    print("your amount is credited")

def withdraw(status,pin,amount,receipt):
    sql="insert into withdraw (status ,pin ,amount ,receipt,) Value (%s,%s,%s,%s)"
    value=(status,pin,amount,receipt)
    mycursor.execute(sql,value)
    atmdb.commit()
    finalbalance=amount-abalance
    x=datetime.datetime.now()
    f=open("bill.txt","w")
    f.write(f"your current balance is {finalbalance} rupees \n {x}")
    print("take your amount and properly take your card")
    print("properly cancelled it and then check it is cancelled")
    print("if it cancelled there is no issues")
    print("if its no cancelled another person use your accound and withdraw your amount\n")
    print("be carefully use atm card ")

def pingenerate(phonenumber,newp,cpassword):
    sql="insert into pin (phonenumber,newp,cpassword) values (%s,%s,%s)"
    values=(phonenumber,newp,cpassword)
    mycursor.execute(sql,values)
    atmdb.commit()
    x=datetime.datetime.now()
    f=open("bill.txt","w")
    f.write(f"your new password is created\n {x}")
    print("pin generate is successfully")
def vdata():
    sql="select * from balancecheck"
    mycursor.execute("select * from balancecheck")
    result=mycursor.fetchall()
    for i in result:
     print(i)
print("******hellow nvs customer**********")
print("***&&&&&******menu******&&&&&***")
print("1.pin generate")
print("2.customer service")
print("3.vdata")

choice=int(input("enter your what would you want:"))
try:
    if choice==1:
        phonenumber=int(input("enter your number which would you have in hand:"))
        newp=int(input("enter your fav four digit number to create a new password:"))
        cpassword=int(input("enter your newp to confirm the password:"))
        pingenerate(phonenumber,newp,cpassword)
    elif choice ==2:
        print("1.balance checking")
        print("2.deposite")
        print("3.withdraw")
        user=int(input("enter your number:"))
        if user==1:
                acaccount=int(input("enter your account number:"))
                pin=int(input("enter your pin number:"))
                balancechecking(acaccount,pin)
        elif user==2: 
                anotes=(500,100,2000,50)
                print(anotes)
                types=("savings,current") 
                print(types)
                status=input("status of your account:")
                number=int(input("enter you pin number:"))
                amount=int(input("enter your amount:"))
                mobilenumber=int(input("enter your current mobile number:"))
                receipt=input("if you want to receipt:")
                deposite(status,number,amount,mobilenumber,receipt)
        elif user==3:
                    anotes=(500,100,2000,50)
                    print(anotes)
                    types=("saving,current") 
                    print(types)
                    status=input("status of your account:")
                    pin=int(input("enter you pin number:"))
                    amount=int(input("enter your amount:"))
                    receipt=input("if you want to receipt:") 
                    withdraw(status,pin,amount,receipt)
    elif choice==3:
        vdata()
    else:
        print("thank you for using nvs atm")
finally:
    print("thank you for using the atm")
    print("be safe be live healthy")
    print("wash hand in properly after and before use of atm machine")