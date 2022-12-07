# Main Program
import mysql.connector as sqltor
from prettytable import PrettyTable
from prettytable import from_db_cursor


def invoice_id_gen():
    initial = "Invoice"
    cur.execute("select Invoice_ID from Invoice_List")
    z = cur.fetchall()
    last_num = len(z)
    new_num = last_num + 1
    gen_id = initial + str(new_num)
    return gen_id


def customer_id_gen():
    initial = "Customer"
    cur.execute("select Customer_ID from Customer_Data")
    z = cur.fetchall()
    last_num = len(z)
    new_num = last_num + 1
    gen_id = initial + str(new_num)
    return gen_id


def new_invoice(customer_name, mobile_number):
    cur.execute(
        "select * from Invoice_List WHERE (Customer_Name = '{}' AND Mobile_Number = '{}') "
        .format(customer_name, mobile_number))
    if_customer_exists = cur.fetchall()
    # If customer is new
    if len(if_customer_exists) == 0:
        name = customer_name
        Mob_no = mobile_number

        customer_id = customer_id_gen()
        invoice_id = invoice_id_gen()
        cur.execute("select curdate()")
        curdate = cur.fetchone()
        date_of_billing = curdate[0]
        # Invoice Generation
        ans = 'Y'
        i = 0
        total_amount = 0
        cur.execute("show tables like '{}'".format(invoice_id))
        result = cur.fetchall()
        if len(result) != 0:
            cur.execute("drop table {}".format(invoice_id))
        cur.execute(
            "create table {inv}(SN integer primary key,Item_Name varchar(20),Price_Per_Unit integer ,Quantity integer, Price integer)"
            .format(inv=invoice_id))
        while ans == 'Y':
            i += 1
            Sno = i
            Item_Name = input("Item Name:")
            Price_PU = float(input("Enter Price of the item:"))
            Qty = int(input("Enter quantity:"))
            Price = Price_PU * Qty
            total_amount += Price
            cur.execute("INSERT INTO {inp} VALUES({},'{}',{},{},{})".format(
                Sno, Item_Name, Price_PU, Qty, Price, inp=invoice_id))
            cn.commit()
            ans = input("Do you want to add more items(Y/N):")
        cur.execute("select * from {inp}".format(inp=invoice_id))
        inv_table = from_db_cursor(cur)
        print(inv_table)

        cur.execute(
            "insert into Invoice_List VALUES('{}','{}','{}','{}','{}',{},{})".
            format(invoice_id, customer_id, date_of_billing, name, Mob_no, i, total_amount))
        cn.commit()
        cur.execute(
            "insert into Customer_Data VALUES('{}','{}','{}','{}')".format(
                customer_id, name, Mob_no, date_of_billing))
        cn.commit()
    # If customer is old
    else:
        cur.execute(
            "select * from Customer_Data WHERE (Name='{}' AND Mobile_Number='{}')".
            format(customer_name, mobile_number))
        data = cur.fetchall()

        customer_id = data[0][0]
        invoice_id = invoice_id_gen()
        cur.execute("select curdate()")
        curdate = cur.fetchone()
        date_of_billing = curdate[0]
        # Invoice Generation
        ans = 'Y'
        i = 0
        total_amount = 0
        cur.execute("show tables like '{}'".format(invoice_id))
        result = cur.fetchall()
        if len(result) != 0:
            cur.execute("drop table {}".format(invoice_id))
        cur.execute(
            "create table {inv}(SN integer primary key,Item_Name varchar(20),Price_Per_Unit integer ,Quantity integer, Price integer)"
            .format(inv=invoice_id))
        while ans == 'Y':
            i += 1
            Sno = i
            Item_Name = input("Item Name:")
            Price_PU = float(input("Enter Price of the item:"))
            Qty = int(input("Enter quantity:"))
            Price = Price_PU * Qty
            total_amount += Price
            cur.execute("INSERT INTO {inp} VALUES({},'{}',{},{},{})".format(
                Sno, Item_Name, Price_PU, Qty, Price, inp=invoice_id))
            cn.commit()
            ans = input("Do you want to add more items(Y/N):")
        cur.execute("select * from {inp}".format(inp=invoice_id))
        inv_table = from_db_cursor(cur)
        print(inv_table)

        cur.execute(
            "insert into Invoice_List VALUES('{}','{}','{}','{}','{}',{},{})".
            format(invoice_id, customer_id, date_of_billing, customer_name, mobile_number, i, total_amount))
        cn.commit()


def search_invoice_by_invoice_id(invoice_id_to_find):
    stmt = "SHOW TABLES LIKE '{}'".format(invoice_id_to_find)
    cur.execute(stmt)
    result = cur.fetchone()
    if result:
        cur.execute("select * from {}".format(invoice_id_to_find))
        to_print = from_db_cursor(cur)
        print(to_print)
    else:
        print("No such invoice id exists")


def search_invoice_by_customer_id(customer_name, mobile_number, date_of_billing):
    cur.execute(
        "select * from Invoice_List WHERE (Customer_Name = '{}' AND Mobile_Number = '{}' AND Date_of_Billing = '{}') "
        .format(customer_name, mobile_number, date_billing))
    if_invoice_exists = cur.fetchall()
    if len(if_invoice_exists) == 0:
        print("No customer with these credentials yet!")
    else:
        for each_invoice in if_invoice_exists:
            invoice_id_to_find = each_invoice[0]
            cur.execute("select * from {}".format(invoice_id_to_find))
            to_print = from_db_cursor(cur)
            print(to_print)


def customer_data(customer_name, mobile_number):
    cur.execute(
        "select * from Customer_Data WHERE (Name = '{}' AND Mobile_Number = '{}') "
        .format(customer_name, mobile_number))
    if_customer_exists = cur.fetchall()
    if len(if_customer_exists) == 0:
        print("No customer with these credentials yet!")
    else:
        print("Fetching Customer Details!")
        customer_id_filter = if_customer_exists[0][0]
        cur.execute(
            "select * from Invoice_List WHERE(Customer_ID='{}')".format(customer_id_filter))
        no_of_purchases = str(len(cur.fetchall()))
        cur.execute(
            "select SUM(Total_Amount) 'Total Amount Spent' FROM Invoice_List WHERE Customer_ID='{}'"
            .format(customer_id_filter))
        total_spent = str(cur.fetchone()[0])
        customer_data_table = PrettyTable()
        customer_data_table.field_names = [
            "Customer Id", "Customer Name", "Mobile Number", "Date of First Buy", "Number of Purchases", "Total Amount Spent"]
        for a in if_customer_exists[0:]:
            customer_data_table.add_row([
                a[0], a[1], a[2], a[3], no_of_purchases, total_spent])
        print(customer_data_table)


def modify_data(customer_name, mobile_number, new_name, new_number):
    cur.execute(
        "select * from Customer_Data WHERE (Name = '{}' AND Mobile_Number = '{}') "
        .format(customer_name, mobile_number))
    if_customer_exists = cur.fetchall()
    customer_id_filter = if_customer_exists[0][0]
    if_prompt = input(
        "Do you want to implement these changes in Customer Database?(Y/N):")

    if if_prompt == 'Y':
        cur.execute(
            "UPDATE Customer_Data SET Name='{}',Mobile_Number='{}' WHERE Customer_ID='{}'"
            .format(new_name, new_number, customer_id_filter))
        cn.commit()
        cur.execute(
            "UPDATE Invoice_List SET Customer_Name='{}',Mobile_Number='{}' WHERE Customer_ID='{}'"
            .format(new_name, new_number, customer_id_filter))
        cn.commit()
        print("Updated Successfully!")


# Starts from here
print("Accessing Billingram Database.....")
print("Authentication required!")

# LOGIN PROMPT
while True:
    try:
        cn = sqltor.connect(host='remotemysql.com',
                            user='AtRLZhnHtV',
                            passwd='SdjF2OD1Bd',
                            port='3306',
                            database='AtRLZhnHtV')
        cur = cn.cursor()
        if cn.is_connected():
            print("Logged In.....")
            break
    except sqltor.errors.DatabaseError:
        print("Invalid Credentials! Try Again.")
# Billingram Menu
print("=" * 50)
print("UNNAMED SUPERMARKET")
print("TAGLINE")
while True:
    print("[Billingram]-V.1.0")
    print("1. New Invoice")
    print("2. Search Invoice")
    print("3. Customer Database")
    print("4. Exit")
    choice = int(input("Enter your choice(1/2/3/4):"))
    # New Invoice
    if choice == 1:
        while True:
            customer_name = input("Enter customer name:")
            mobile_number = input("Enter mobile number:")
            if mobile_number.isdigit() and len(mobile_number) == 10:
                new_invoice(customer_name, mobile_number)
                break
            else:
                print('Enter mobile number correctly!')
                continue

    if choice == 2:
        print("1. By invoice id")
        print("2. By customer name, mobile number and date of billing")
        choice2 = int(input("Enter your choice(1/2):"))
        if choice2 == 1:
            invoice_id_to_find = input("Enter invoice id:")
            search_invoice_by_invoice_id(invoice_id_to_find)
        else:
            customer_name = input("Enter customer name:")
            mobile_number = input("Enter mobile number:")
            date_billing = input("Enter date of billing:")
            search_invoice_by_customer_id(
                customer_name, mobile_number, date_billing)

    if choice == 3:
        print("Welcome to Customer Database!")
        print("Enter Customer Details")
        customer_name = input("Enter customer name:")
        mobile_number = input("Enter mobile number:")
        customer_data(customer_name, mobile_number)

        cur.execute(
            "select * from Customer_Data WHERE (Name = '{}' AND Mobile_Number = '{}') "
            .format(customer_name, mobile_number))
        if_customer_exists = cur.fetchall()
        if len(if_customer_exists) == 0:
            pass
        else:
            modify_maybe = input(
                "Do you want to modify customer details?(Y/N):")
            if modify_maybe == 'Y':
                print("Please enter new details of the customer:")
                while True:
                    new_name = input("Enter Name:")
                    new_number = input("Enter Mobile Number:")
                    if new_number.isdigit() and len(new_number) == 10:
                        modify_data(customer_name, mobile_number,
                                    new_name, new_number)
                        break
                    else:
                        print("Enter mobile number correctly!")
                        continue

    if choice == 4:
        break
