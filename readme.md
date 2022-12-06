# Billingram

Billingram is a bill generator and customer data managing software made with python.

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
4. Install prettytable library by running the following command in terminal
   `pip install prettytable`.
5. Clone the repository by running the following command in terminal
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

1. New invoice
2. Search invoice
3. View and edit customer data
4. Exit

Let's talk about each one by one.

#### New invoice

This option is used to generate a new invoice. It asks for the customer's name and phone number. Then it asks for Items, Quantity and Price of each item. After entering all the items, it asks for the discount and then generates the invoice.
It creates a new table in database for each invoice and stores the invoice data in that table. It also stores the customer data in the `customerdata` table. It also stores invoice number and date in the `invoicelist` table.

#### Search invoice

This option is used to search for an invoice. It asks for the invoice number and then displays the invoice.
Another way to look for an invoice is to enter customer name, phone number and date. It will display all the invoices of that customer on that date.

#### View and edit customer data

This option is used to view and edit customer data. It displays the data of the customer whose data you enter. It also displays the total amount of money spent by each customer. It also displays the total number of invoices generated for each customer.

## Contributing

To contribute to this project, fork this repository and make a pull request. I will review the changes and merge them if they are good. You can also open an issue if you find any bug or want to suggest a feature. I will try to fix the bug or add the feature as soon as possible.

## Social media

[![Twitter](https://img.shields.io/twitter/follow/GiuocoPianoSimp?style=social)](https://twitter.com/GiuocoPianoSimp)
[![Discord](https://img.shields.io/discord/947433833660317706?label=Discord&style=social)](https://discord.gg/nhzEgqwBwp)
[![YouTube](https://img.shields.io/youtube/channel/subscribers/UC9DloEs6b9xLwtQQTe0F32g?label=YouTube&style=social)](https://www.youtube.com/channel/UC9DloEs6b9xLwtQQTe0F32g)

If you like this project, please star this repository. Thank you. :smile:
