# Billingram Installer
import mysql.connector as sqltor
print("Welcome to Billingram!")
print("Visit https://github.com/theanuragmishra/billingram for more information.")
print("Current Version: V 1.0")
print("Billingram is a billing invoice system made for supermarkets,")
print("Required softwares to run Billingram:")
print("1. Python 3.6 or above")
print("2. MySQL")
print("3. Python modules: mysql-connector-python, prettytable")
print("In order to install Billingram, please make sure the essentials mentioned above are already installed in your pc.")
choice = input("Do you want to install Billingram(Y/N):")
if choice == "Y":
    while True:
        try:
            print(
                "Please enter your MySQL credentials in order to connect MySQL database.")
            host = input("Enter the name of the host:")
            user = input("Enter username:")
            password = input("Enter password:")
            while True:
                port = input("Enter port number:")
                if port.isdigit():
                    break
                print("Invalid port number! Please enter a valid port number.")
            print("Connecting to MySQL Database......")
            cn = sqltor.connect(host=host,
                                user=user, passwd=password, port=port)
            cursor = cn.cursor()
            if cn.is_connected():
                print("Connection Successful.....")
                print("Creating Database Billingram.....")
                cursor.execute("create database if not exists Billingram")
                print("Creating required tables in Database Billingram.....")
                cursor.execute("use Billingram")
                cursor.execute(
                    "create table if not exists Customer_Data(Customer_ID varchar(50) NOT NULL PRIMARY KEY,Name varchar(50) NOT NULL,Mobile_Number char(10) NOT NULL,Date_of_First_Buy date NOT NULL)")
                cursor.execute("create table if not exists Invoice_List(Invoice_ID varchar(100) PRIMARY KEY NOT NULL,Customer_ID varchar(50) NOT NULL,Date_of_Billing date NOT NULL,Name varchar(50) NOT NULL,Mobile_Number char(10) NOT NULL,No_of_Items integer NOT NULL,Total_Amount decimal(64,2) NOT NULL)")
                print("Created required database and tables.")
                print("All records will be stored in the Billingram database.")
                print("Thanks for installing Billingram!")
                print("Software is installed!")
                break
        except (sqltor.errors.InterfaceError, sqltor.errors.ProgrammingError, sqltor.errors.DatabaseError) as e:
            print("Invalid Credentials! Re-run the program to try again.")
elif choice == "N":
    print("Close the installer. If you want to install Billingram, kindly re-run the program.")
