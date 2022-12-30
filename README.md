# Inventory Manager <br />

## Table of Contents <br />
- [Inventory Manager <br />](#inventory-manager)
  * [Table of Contents <br />](##table-of-contents)
  * [Description <br/>](##description)
  * [Getting Started <br />](#'getting-started)
    + [Prerequisites <br />](###prerequisites)
    + [Installation <br />](###installation)
  * [Usage <br />](##usage)

## Description <br/>
This project is an shoe inventory management program built with Python. It stores data such as SKU codes, product names etc. on a text file and allows users to read and edit inventory data.

## Getting Started <br />
To get a local copy of this program running on your machine, follow the steps below.

### Prerequisites <br />
* Python 3.9
> You can install Python 3.9 here: https://www.python.org/downloads/release/python-390/

* PyCharm (Optional)
> You can install PyCharm here: https://www.jetbrains.com/pycharm/download/

### Installation <br />
1. Download the inventory.py and inventory.txt files located in this project onto your local machine
> NOTE: Do not rename either of these files.
2. Place both files in a new folder
3. Run the inventory.py file either using IDLE Shell or PyCharm (as stated above)

## Usage <br />
This inventory manager has 7 different commands to choose from, as shown in the menu:

![Menu](/img/menu.png)

The **restock** command allows you to restock the product which has the lowest stock in the inventory. Enter the quantity of product you would like to restock and the
program will update the inventory accordingly.

![Restock](/img/restock.png)

The **search** command allows you to discover information about a certain product using its SKU code.

![Search](/img/search.png)

The **sale** command will display the latest product on sale.

![Sale](/img/sale.png)

The **view** command will display the entire inventory.

![View](/img/view.png)

The **value** command will display the value of each product in the inventory.

![Value](/img/value.png)

The **add** command will allow you to add a new product to the inventory. You must enter the country, SKU Code, product name, cost & quantity as shown below.

![Add](/img/add.png)

The **quit** command will exit the program.
