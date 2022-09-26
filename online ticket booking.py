import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="ticket_booking"
)
#print(mydb)
mycursor=mydb.cursor()
#mycursor.execute("create database ticket_booking")
#mycursor.execute("create table train_booking(name varchar(200),age int,seats int,fav_seats varchar(200),category varchar(200),boarding_place varchar(200))")
#mycursor.execute("create table bus_booking(name varchar(200),age int,seats int,seat_types varchar(200))")
#mycursor.execute("create table aeroplane_booking(name varchar(200),age int)")
#print("created")
def chennai_to_delhi(name,age,seats,fav_seats,category,boarding_place):
 sql="insert into train_booking(name,age,seats,fav_seats,category,boarding_place) values(%s,%s,%s,%s,%s,%s)"
 values=(name,age,seats,fav_seats,category,boarding_place)
 mycursor.execute(sql,values)
 mydb.commit()
 price=seats*2000
 detail=name,age,fav_seats
 #f=open("receipt.txt","x")
 process=input("enter your card type:")
 if process=="rupay":
    print("there no due to use rupay card for particular bank")
    print("icic,sbi,these types of bank is not provided charge amount")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {boarding_place}\n {detail}")
 elif process=="credit card":
    print("10 rupees charges will be paid in at the same time")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {boarding_place}")
def tirunelveli_to_banglore(name,age,seats,fav_seats,category,boarding_place):
 sql="insert into train_booking(name,age,seats,fav_seats,category,boarding_place) values(%s,%s,%s,%s,%s,%s)"
 values=(name,age,seats,fav_seats,category,boarding_place)
 mycursor.execute(sql,values)
 mydb.commit()
 detail=name,age,fav_seats
 price=seats*800
 process=input("enter your card type:")
 if process=="rupay":
    print("there no due to use rupay card for particular bank")
    print("icic,sbi,these types of bank is not provided charge amount")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {boarding_place}\n{detail}")
 elif process=="credit card":
    print("10 rupees charges will be paid in at the same time")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {boarding_place}")
 elif process=="credit card":
    print("10 rupees charges will be paid in at the same time")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {boarding_place}")
def tenkasi_to_chennai(name,age,seats,seat_types):
 sql="insert into bus_booking(name,age,seats,seat_types) values(%s,%s,%s,%s)"
 values=(name,age,seats,seat_types)
 mycursor.execute(sql,values)
 mydb.commit()
 detail=name,age,seat_types
 price=seats*3000
 process=input("enter your card type:")
 if process=="rupay":
    print("there no due to use rupay card for particular bank")
    print("icic,sbi,these types of bank is not provided charge amount")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {detail}")
 elif process=="credit card":
    print("10 rupees charges will be paid in at the same time")
    print("save journey")
    today=datetime.datetime.now()
    f=open("receipt.txt","w")
    f.write(f"your rupees is {price} in per person \n {today}\n {detail}")
print("***********choice***********")
print("1.train")
print("2.bus")
print("3.aeroplane")
print("4.cancelled")
try:
 choice=int(input("enter your choice:"))
 if choice==1:
    print("1.chennai_to_delhi express")
    print("2.tirunelveli_to_banglore")
    user=int(input("enter your train:"))
    if user==1:
     training_through=["chennai","banglore","karnataka"]
     seats_types=("lower,middle,upper")
     name=input("enter your name:")
     age=int(input("enter your age:"))
     if age>=65:
        print("you'r older queen and king")
        print("we are provided the mask and the one compartment is especially in yours")
        print("there are 3 police alloted in that particular compartment")
        seats=int(input("enter you no.of seats:"))
        print(seats_types)
        fav_seats=input("enter your fav_seats: ")
        category=input("enter your gender:")
        print(training_through)
        boarding_place=input("enter your place:")
        while boarding_place in training_through:
         chennai_to_delhi(name,age,seats,fav_seats,category,boarding_place)
     elif age<=65:
        seats=int(input("enter you no.of seats:"))
        print(seats_types)
        fav_seats=input("enter your fav_seats: ")
        category=input("enter your gender:")
        boarding_place=input("enter your place:")
        while boarding_place in training_through:
         chennai_to_delhi(name,age,seats,fav_seats,category,boarding_place)
    elif user==2:
     training_through=["tirunelveli","sivakasi","madurai","virudhunagar"]
     seats_types=("lower,middle,upper")
     name=input("enter your name:")
     age=int(input("enter your age:"))
     if age>=65:
        print("you'r older queen and king")
        print("we are provided the mask and the one compartment is especially in yours")
        print("there are 3 police alloted in that particular compartment")
        seats=int(input("enter you no.of seats:"))
        print(seats_types)
        fav_seats=input("enter your fav_seats: ")
        category=input("enter your gender:")
        print(training_through)
        boarding_place=input("enter your place:")
        while boarding_place in training_through:
         chennai_to_delhi(name,age,seats,fav_seats,category,boarding_place)
     elif age<=65:
        seats=int(input("enter you no.of seats:"))
        print(seats_types)
        fav_seats=input("enter your fav_seats: ")
        category=input("enter your gender:")
        print(training_through)
        boarding_place=input("enter your place:")
        while boarding_place in training_through:
         chennai_to_delhi(name,age,seats,fav_seats,category,boarding_place)
    else:
         print("sorry only few trains are now running")
 elif choice==2:
   print("1.tenkasi_to_chennai")
   user=int(input("enter your number:"))
   if user==1:
     types=["window seats,normal seats"]
     bus_through=["sivakasi","madurai","virudhunagar"]
     name=input("enter your name:")
     age=int(input("enter your age:"))
     if age>=65:
        print("we given infornt of our bus max we will give seats of 1 or 1 to 10 ")
        seats=int(input("enter you no.of seats:"))
        print(types)
        seat_types=input("enter your fav_seats: ")
        category=input("enter your gender:")
        print(bus_through)
        seat_types=input("enter your fav_seats:")
        tenkasi_to_chennai(name,age,seats,seat_types)
     elif age<=65:
        seats=int(input("enter you no.of seats:"))
        print(types)
        seat_types=input("enter your fav_seats:")
        tenkasi_to_chennai(name,age,seats,seat_types)
   elif choice==4:
      print("thank you so much")
 else:
   print("sorry")
   print("only two types of transport are now in running due to climate")
except IndexError:
   print("this is my own error sorry")
except NameError:
   print("soryy this is my own fault")
finally:
   print("thank you for use")





    
