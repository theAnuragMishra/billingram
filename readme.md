<div align=center><h1>Billingram</h1>
<a href="https://twitter.com/GiuocoPianoSimp"><img src="https://img.shields.io/twitter/follow/GiuocoPianoSimp?style=social"></a>
<a href="https://discord.gg/nhzEgqwBwp"><img src="https://img.shields.io/discord/947433833660317706?label=Discord&style=social"></a>
<a href="https://www.youtube.com/channel/UC9DloEs6b9xLwtQQTe0F32g"><img src="https://img.shields.io/youtube/channel/subscribers/UC9DloEs6b9xLwtQQTe0F32g?label=YouTube&style=social"></a>
<p>
Billingram is a bill generator and customer data managing software made with python.
</p>
</div>

## Prerequisites

1. Python 3.6 or higher
2. mysql-connector-python library
3. prettytable library
4. mysql server

## Installation

1. Install python 3.6 or higher from [here](https://www.python.org/downloads/).
2. Install mysql server from [here](https://dev.mysql.com/downloads/mysql/).
3. Install mysql-connector-python library by running the following command in terminal:
   `pip install mysql-connector-python`.
4. Install prettytable library by running the following command in terminal:
   `pip install prettytable`.
5. Clone the repository by running the following command in terminal:
   `git clone https://github.com/theAnuragMishra/billingram.git`.
6. Open the `main.py` file in any text editor and change the `host`, `user`, `password` and `database` variables to your mysql server's credentials.
7. Open terminal in the directory where you cloned the repository and run the following command:
   `python billingram_installer.py`
   Enter charset = `latin1` and your mysql username and password when prompted.
8. Billingram is now installed. Run the following command to start the program:
   `python main.py`.

## Usage

### Note: Enter your mysql username and password when prompted

### There are four options available

![1671113871186](image/readme/1671113871186.png)

1. New invoice (n)
2. Search invoice (s)
3. View and edit customer data (c)
4. Exit (e)

Let's talk about each one by one.

#### New invoice

![1671114028390](image/readme/1671114028390.png)

This option is used to generate a new invoice. It asks for the customer's name and phone number.

![1671114080424](image/readme/1671114080424.png)

Note: Enter `back` as the customer name to go back to the main menu.

![1671114511688](image/readme/1671114511688.png)

Then it asks for Items, Quantity and Price of each item. After entering all the items, it asks for the discount and then generates the invoice.
It creates a new table in database for each invoice and stores the invoice data in that table. The table name is the invoice number.

![1671114271741](image/readme/1671114271741.png)

It also stores the customer data in the `customer_data` table and the invoice number and the date in the `invoice_list` table.

![1671114389844](image/readme/1671114389844.png)

![1671114409772](image/readme/1671114409772.png)

Note: If you enter the same customer name and phone number again, it will not create a new entry in the `customer_data` table. It will just update the total amount spent by that customer.

![1671114488296](image/readme/1671114488296.png)

#### Search invoice

There are two options to look for an invoice in the database:

![1671114578800](image/readme/1671114578800.png)

Note: Enter `back` as the invoice number to go back to the main menu.

![1671115773333](image/readme/1671115773333.png)

1. Search by invoice number (i)

   ![1671114675512](image/readme/1671114675512.png)

   Note: The invoice number is the name of the table in which the invoice data is stored and is of the format `invoicen` where n is the number of invoice.
   Note: Enter `back` as the invoice number to go back to the previous menu.

   ![1671115056943](image/readme/1671115056943.png)

2. Search by customer name, mobile number and date (d)

   ![1671114906742](image/readme/1671114906742.png)

   Note: It displays all the invoices of the customer whose name, mobile number and date you enter.
   Note: Enter `back` as the customer name to go back to the previous menu.

   ![1671115033660](image/readme/1671115033660.png)

#### View and edit customer data

This option is used to view and edit customer data. It displays the data of the customer whose data you enter.

![1671115113405](image/readme/1671115113405.png)

Note: Enter `back` as the customer name to go back to the main menu.

![1671115725560](image/readme/1671115725560.png)

It also gives you an option to edit the customer data.

![1671115134268](image/readme/1671115134268.png)

Press "n" to go back to the previous menu without editing. Press "y" to edit the customer data.

![1671115184139](image/readme/1671115184139.png)

After you're done editing, press "y" to save the changes. Press "n" to discard the changes.

![1671115207165](image/readme/1671115207165.png)

![1671115229352](image/readme/1671115229352.png)

`Mahi` is changed to `Mahii` and `4545454545` is changed to `4564564567` in both the tables, as desired.

## Contributing

To contribute to this project, fork this repository and make a pull request. I will review the changes and merge them if they are good. You can also open an issue if you find any bug or want to suggest a feature. I will try to fix the bug or add the feature as soon as possible.

If you like this project, please star this repository. Thank you. :smile:
