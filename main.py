# Main Program
from datetime import datetime
import mysql.connector as sqltor
from prettytable import PrettyTable
from prettytable import from_db_cursor
import math


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
    invoice_id = invoice_id_gen()
    cur.execute("select curdate()")
    curdate = cur.fetchone()
    date_of_billing = curdate[0]
    cur.execute(
        "select * from Invoice_List WHERE (Name = '{}' AND Mobile_Number = '{}') "
        .format(customer_name, mobile_number))
    if_customer_exists = cur.fetchall()
    # If customer is new
    if len(if_customer_exists) == 0:
        customer_id = customer_id_gen()
        cur.execute(
            "insert into Customer_Data VALUES('{}','{}','{}','{}')".format(
                customer_id, customer_name, mobile_number, date_of_billing))
        cn.commit()
    # If customer is old
    else:
        cur.execute(
            "select * from Customer_Data WHERE (Name='{}' AND Mobile_Number='{}')".
            format(customer_name, mobile_number))
        data = cur.fetchall()
        customer_id = data[0][0]
    # Invoice Generation
    ans = 'y'
    i = 0
    cur.execute("show tables like '{}'".format(invoice_id))
    result = cur.fetchall()
    if len(result) != 0:
        cur.execute("drop table {}".format(invoice_id))
    cur.execute(
        "create table {inv}(SN integer primary key,Item_Name varchar(20),Price_Per_Unit decimal(30,2),Quantity integer, `Discount(%)` decimal(7,2), Price decimal(50,2))"
        .format(inv=invoice_id))
    while ans == 'y':
        i += 1
        Sno = i
        while True:
            item_name = input("Item Name:")
            if len(item_name) <= 20:
                break
            print('Enter item name under 20 characters long!')
        # adding validation for price
        while True:
            try:
                price_per_unit = (input("Enter Price of the item:"))
                if len(price_per_unit) <= 27:
                    price_per_unit = float(price_per_unit)
                    break
                print("Enter price under 27 characters long!")
            except ValueError:
                print('Enter a valid price i.e., a number')
        # adding validation for final amount for that item
        while True:
            try:
                quantity = int(input("Enter quantity:"))
                if 2147483647 >= quantity >= 0:
                    price = price_per_unit * quantity
                    break
                print('Enter quantity under 2147483647 and greater than 0!')
            except ValueError:
                print('Enter a valid quantity i.e., a number')

        # adding discount
        while True:
            discount = input(
                'Enter discount in %(leave empty for no discount): ')
            if discount == "":
                disc = 0
                break
            else:
                try:
                    disc = float(discount)
                    if 0 <= disc <= 100:
                        disc_amount = (disc/100)*price
                        price = price-disc_amount
                        break
                    print('Enter a positive discount value <=100%!')
                except ValueError:
                    print('Enter a valid discount in float or integer')

        cur.execute("INSERT INTO {inp} VALUES({},'{}',{},{}, {},{})".format(
            Sno, item_name, price_per_unit, quantity, disc, price, inp=invoice_id))
        cn.commit()
        ans = input("Do you want to add more items(y/n):")
    cur.execute("select * from {inp}".format(inp=invoice_id))
    inv_table = from_db_cursor(cur)
    inv_table.align["Price_Per_Unit"] = "r"
    inv_table.align["Price"] = "r"
    inv_table.title = invoice_id + "        " + \
        str(date_of_billing) + "        " + customer_name
    print(inv_table)
    cur.execute("select sum(Price) from {}".format(invoice_id))
    total_amount = cur.fetchall()[0][0]

    print("TOTAL AMOUNT: Rs.{}".format(total_amount))
    print("Thank You for shopping with us!")
    print("-" * 50)
    cur.execute(
        "insert into Invoice_List VALUES('{}','{}','{}','{}','{}',{},{})".
        format(invoice_id, customer_id, date_of_billing, customer_name, mobile_number, i, total_amount))
    cn.commit()


def search_invoice_by_invoice_id():
    while True:
        print("-" * 50)
        print("SEARCH INVOICE BY INVOICE ID")
        print("............................")
        invoice_id_to_find = input(
            "Enter invoice id: ")
        if invoice_id_to_find == "back":
            break
        stmt = "SHOW TABLES LIKE '{}'".format(invoice_id_to_find)
        cur.execute(stmt)
        result = cur.fetchone()
        if result:
            cur.execute(
                "select * from Invoice_List where (Invoice_ID = '{}')".format(invoice_id_to_find))
            x = cur.fetchall()
            invoice_id_for_title = x[0][0]
            name = x[0][3]
            date = x[0][2]
            total_amount = x[0][6]
            cur.execute("select * from {}".format(invoice_id_to_find))
            to_print = from_db_cursor(cur)
            to_print.title = invoice_id_for_title + "        " + \
                str(date) + "        " + name
            print(to_print)
            print(f"TOTAL AMOUNT: {total_amount}")
            # print("-"*25)
            continue
        print("No such invoice id exists!")
        # print("-"*25)


def search_invoice_by_customer_id():
    while True:
        print("-"*25)
        print("SEARCH INVOICE BY NAME, MOBILE NUMBER AND DATE OF BILLING")
        print(".........................................................")
        customer_name = input("Enter customer name:")
        if customer_name == "back":
            break
        while True:
            mobile_number = input("Enter mobile number:")
            if len(mobile_number) == 10 and mobile_number.isdigit():
                break
            print("Enter valid mobile number!")
        while True:
            date_billing = input("Enter date of billing:")
            try:
                if date_billing != datetime.strptime(date_billing, "%Y-%m-%d").strftime('%Y-%m-%d'):
                    raise ValueError
                break
            except ValueError:
                print("Enter date in the format YYYY-MM-DD, don't forget zeroes!")
                continue
        cur.execute(
            "select * from Invoice_List WHERE (Name = '{}' AND Mobile_Number = '{}' AND Date_of_Billing = '{}') "
            .format(customer_name, mobile_number, date_billing))
        if_invoice_exists = cur.fetchall()
        if len(if_invoice_exists) == 0:
            print("No customer with these credentials yet!")
        else:
            for each_invoice in if_invoice_exists:
                invoice_id_to_find = each_invoice[0]
                name = each_invoice[3]
                date = each_invoice[2]
                total_amount = each_invoice[6]
                cur.execute("select * from {}".format(invoice_id_to_find))
                to_print = from_db_cursor(cur)
                to_print.title = invoice_id_to_find + "        " + \
                    str(date) + "        " + name
                print(to_print)
                print(f"TOTAL AMOUNT: {total_amount}")
                # print("-"*25)


def customer_data(customer_name, mobile_number):
    cur.execute(
        "select * from Customer_Data WHERE (Name = '{}' AND Mobile_Number = '{}') "
        .format(customer_name, mobile_number))
    if_customer_exists = cur.fetchall()
    if len(if_customer_exists) == 0:
        print("No customer with these credentials yet!")
    else:
        customer_id_filter = if_customer_exists[0][0]
        cur.execute(
            "select * from Invoice_List WHERE(Customer_ID='{}')".format(customer_id_filter))
        no_of_purchases = str(len(cur.fetchall()))
        cur.execute(
            "select SUM(Total_Amount) 'Total Amount Spent' FROM Invoice_List WHERE Customer_ID='{}'"
            .format(customer_id_filter))
        total_spent = str(cur.fetchone()[0])
        customer_data_table = PrettyTable()
        customer_data_table.title = customer_id_filter
        customer_data_table.field_names = [
            "Customer Id", "Customer Name", "Mobile Number", "Date of First Buy", "Number of Purchases",
            "Total Amount Spent"]
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
        "Do you want to implement these changes in Customer Database?(y/n):")

    if if_prompt == 'y':
        cur.execute(
            "UPDATE Customer_Data SET Name='{}',Mobile_Number='{}' WHERE Customer_ID='{}'"
            .format(new_name, new_number, customer_id_filter))
        cn.commit()
        cur.execute(
            "UPDATE Invoice_List SET Name='{}',Mobile_Number='{}' WHERE Customer_ID='{}'"
            .format(new_name, new_number, customer_id_filter))
        cn.commit()
        print("Updated Successfully!")
        # print("-" * 25)
    # else:
        # print("-" * 25)


        # Starts from here
print("Accessing Database.....")
print("Authentication required!")

# LOGIN PROMPT
while True:
    try:
        user_name = input("Enter username:")
        password = input("Enter password:")
        while True:
            port_number = input("Enter port number:")
            if port_number.isdigit():
                break
            print("Enter a valid port number!")
        print("Connecting to MySQL Database......")
        cn = sqltor.connect(charset='latin1',
                            host='localhost',
                            user=user_name,
                            passwd=password,
                            port=port_number,
                            database='billingram')
        cur = cn.cursor()
        if cn.is_connected():
            print("Logged In.....")
            break
    except sqltor.errors.DatabaseError:
        print("Invalid Credentials! Try Again.")
# Billingram Menu
print("-" * 50)

while True:
    print("Billingram 1.0.0")
    print("-" * 25)
    print("New Invoice/Search Invoice/Customer DataBase/Exit")

    choice = input("Enter your choice(n/s/c/e):")
    # New Invoice
    if choice == "n":
        while True:
            # print("-" * 25)
            print("NEW INVOICE")
            print("...........")
            while True:
                customer_name = input("Enter customer name:")
                if len(customer_name) <= 50:
                    break
                print("Enter a name under 50 characters long!")
            if customer_name == "back":
                print("-" * 25)
                break
            while True:
                mobile_number = input("Enter mobile number:")
                if mobile_number.isdigit() and len(mobile_number) == 10:
                    break
                print('Enter mobile number correctly!')
            new_invoice(customer_name, mobile_number)

    if choice == "s":
        while True:
            print("-" * 25)
            print("SEARCH INVOICE")
            print(".............")
            print("By Invoice Id/By Name,Mobile Number, Date")
            choice2 = input("Enter your choice(i/d):")
            if choice2 == "back":
                break
            if choice2 == "i":
                search_invoice_by_invoice_id()
            elif choice2 == "d":
                search_invoice_by_customer_id()
            else:
                print("Enter a valid choice!")

    if choice == "c":
        while True:
            print("-" * 25)
            print("CUSTOMER DATABASE")
            print(".................")
            customer_name = input("Enter customer name:")
            if customer_name == "back":
                break
            while True:
                mobile_number = input("Enter mobile number:")
                if mobile_number.isdigit() and len(mobile_number) == 10:
                    break
                print('Enter mobile number correctly!')
            customer_data(customer_name, mobile_number)

            cur.execute(
                "select * from Customer_Data WHERE (Name = '{}' AND Mobile_Number = '{}') "
                .format(customer_name, mobile_number))
            if_customer_exists = cur.fetchall()
            if len(if_customer_exists) == 0:
                continue
            else:
                modify_maybe = input(
                    "Do you want to modify customer details?(y/n):")
                if modify_maybe == 'y':
                    print("Please enter new details of the customer:")
                    while True:
                        new_name = input("Enter new Name:")
                        if len(new_name) <= 50:
                            break
                        print("Enter a name under 50 characters long!")
                    while True:
                        new_number = input("Enter new Mobile Number:")
                        if new_number.isdigit() and len(new_number) == 10:
                            break
                        print("Enter mobile number correctly!")
                    modify_data(customer_name, mobile_number,
                                new_name, new_number)

    if choice == "e":
        break
