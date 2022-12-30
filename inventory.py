
# ======== Shoe Class ==========
class Shoe:

    # constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # method that returns the cost of the shoe
    def get_cost(self):
        return self.cost

    # method that returns quantity of the shoe
    def get_quantity(self):
        return self.quantity

    # returns string representation of object
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


# ============= Shoe list ===========
# This list will be used to store a list of shoe objects.
shoe_list = []

# ========== Functions ==============


def read_shoes_data():
    try:
        with open("inventory.txt", "r+") as f:
            next(f)  # skips first line of file
            # iterates through each line in file
            for line in f:
                data = line.strip().split(",")  # turns data in each line into a list

                # uses data to create a new shoe object and appends it to shoe_list
                new_shoe = Shoe(data[0], data[1], data[2], int(data[3]), int(data[4]))
                shoe_list.append(new_shoe)

    # presents error if inventory.txt file missing
    except FileNotFoundError:
        print(" >> ERROR: Inventory file missing!")


def capture_shoes(country, code, product, cost, quantity):
    # creates new shoe object and appends it to shoe list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)


def view_all():
    # iterates through shoe_list and prints string representation of each shoe object
    for shoe in shoe_list:
        # gets shoe data
        data = shoe.__str__().split(",")

        # prints string representation of shoe data
        print(f" >> Country: {data[0]}, Code: {data[1]}, Product: {data[2]}, Cost: ${data[3]}, Quantity: {data[4]}")


def re_stock(add_quantity):
    # list of shoe quantities
    quantities = [shoe.quantity for shoe in shoe_list]

    # gets index of shoe which has the lowest quantity
    shoe_index = quantities.index(min(quantities))

    # adds extra quantity to shoe quantity value
    shoe_list[shoe_index].quantity += add_quantity

    # adds updated shoe data to inventory.txt file
    with open("inventory.txt", "w+") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")  # writes header
        for shoe in shoe_list:
            shoe_data = f"{shoe.__str__()}\n"
            f.write(shoe_data)


def search_shoe(sku_code):
    # gets list of sku codes
    sku_codes = [shoe.code for shoe in shoe_list]

    # gets the index of shoe which matches the sku code
    sku_index = sku_codes.index(sku_code)

    # returns shoe object at that index
    return shoe_list[sku_index]


def value_per_item():
    # iterates through each shoe in shoe_list
    for shoe in shoe_list:
        # calculates and displays value of shoe
        value = shoe.get_cost()*shoe.get_quantity()
        print(f" >> {shoe.product} has a value of ${value}.")


def highest_qty():
    # list of shoe quantities
    quantities = [shoe.quantity for shoe in shoe_list]

    # gets index of shoe which has the highest quantity
    shoe_index = quantities.index(max(quantities))

    # gets shoe object at that index in shoe_list
    highest_shoe = shoe_list[shoe_index]

    # displays shoe for sale
    print(f" >> {highest_shoe.product} is for sale!")


# adds inventory to shoe_list
read_shoes_data()

# ========== Main Menu =============

while True:
    # displays menu and gets user input
    choice = input(''' ++++++++++++ MENU ++++++++++++
 >> restock - find shoe with lowest quantity and restock it
 >> search - search for a shoe
 >> sale - finds latest shoes on sale
 >> view - view entire inventory
 >> value - display value of inventory
 >> add - add new shoe to inventory
 >> quit - exit program

 >> Enter your choice: ''')

    if choice.lower() == 'restock':
        try:
            # gets quantity
            extra_quantity = int(input(" >> Enter quantity to restock: "))

            # restocks shoe with extra quantity
            re_stock(extra_quantity)

        # displays error if invalid quantity entered
        except TypeError:
            print(" >> You entered an invalid quantity. Please try again.")

    elif choice.lower() == 'search':
        # gets sku code from user and searches for shoe with matching code
        shoe_sku = input(" >> Enter the SKU code of the shoe: ")

        # gets corresponding shoe object
        found_shoe = search_shoe(shoe_sku)

        # gets shoe data
        data = found_shoe.__str__().split(",")

        # prints string representation of shoe data
        print(f" >> Country: {data[0]}, Code: {data[1]}, Product: {data[2]}, Cost: ${data[3]}, Quantity: {data[4]}")

    elif choice.lower() == 'sale':
        # displays shoes on sale
        highest_qty()

    elif choice.lower() == 'view':
        # displays all shoes
        view_all()

    elif choice.lower() == 'value':
        # displays value of each shoe
        value_per_item()

    elif choice.lower() == 'add':
        # gets country, code, product, cost and quantity from user, then adds that data to inventory
        shoe_country = input(" >> Enter country: ")
        shoe_code = input(" >> Enter SKU Code: ")
        shoe_product = input(" >> Enter name of product: ")
        shoe_cost = input(" >> Enter cost of shoe: ")
        shoe_quantity = input(" >> Enter quantity: ")

        capture_shoes(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)

    elif choice.lower() == 'quit':
        break

    # displays error if invalid choice entered
    else:
        print(" >> That is an invalid choice. Please try again.")

    print("\n")
