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
            print("Connecting to MySQL Database......")
            cn = sqltor.connect(host='remotemysql.com',
                                user='AtRLZhnHtV',
                                passwd='SdjF2OD1Bd',
                                port='3306',
                                database='AtRLZhnHtV')
            cursor = cn.cursor()
            if cn.is_connected():
                print("Connection Successful.....")
                cursor.execute("use AtRLZhnHtV")
                cursor.execute(
                    "create table if not exists Customer_Data(Customer_ID varchar(10) NOT NULL PRIMARY KEY,Name varchar(20) NOT NULL,Mobile_Number char(10) NOT NULL,Date_of_First_Buy date NOT NULL)")
                cursor.execute("create table if not exists Invoice_List(Invoice_ID varchar(20) PRIMARY KEY NOT NULL,Customer_ID varchar(15) NOT NULL,Date_of_Billing date NOT NULL,Customer_Name varchar(20) NOT NULL,Mobile_Number char(10) NOT NULL,No_of_Items integer NOT NULL,Total_Amount integer NOT NULL)")
                print("Created required database and tables.")
                print("All records will be stored in the Billingram database.")
                print("Thanks for installing Billingram!")
                print("Software is installed!")
                break
        except (sqltor.errors.InterfaceError, sqltor.errors.ProgrammingError, sqltor.errors.DatabaseError) as e:
            print("Invalid Credentials! Re-run the program to try again.")
elif choice == "N":
    print("Close the installer. If you want to install Billingram, kindly re-run the program.")
