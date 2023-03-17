import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mysql"
)
myCursor = mydb.cursor()
ch = int(0)


def insert():
    name = input("Enter your name : ")
    password = input("Enter your password : ")
    myCursor.execute("INSERT INTO login (name, pass) VALUES (%s, %s)", (name, password))
    print("Thank you")


def display():
    myCursor.execute("select * from login")
    for x in myCursor:
        print("Name : " + x[0] + "\tPassword : " + x[1])


def delete():
    name = input("Enter the name to delete : ")
    myCursor.execute("delete from login where name = (%s)", (name,))


def update():
    name = input("Enter your name to update : ")
    newname = input("Enter your new name : ")
    newpass = input("Enter your new password : ")

    myCursor.execute("update login set name = (%s),pass = (%s) where name = (%s)", (newname, newpass,  name))


while ch <= 3:
    ch = int(input("1. Add User \n2. Display User\n3. Delete User\n4. Update User\n5. Exit \nEnter your choice : "))
    match ch:
        case 1:
            insert()

        case 2:
            display()

        case 3:
            delete()

        case 4:
            update()


mydb.commit()
