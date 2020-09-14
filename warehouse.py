"""
        Program: Warehouse management system
        Author: Wes Ray
    Description:  Description:
        1 - Register new item
            id (auto generated)
            title (str)
            category (str)
            stock (int)
            price (float)
        2 - Display Catalog
        3 - Update Stock
        4 - Remove item from catalog
        5 - Print Total stock value
        6 - Report - out of stock
"""
# imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle

# global variables
catalog = []
data_file = 'warehouse.data'

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') # create/open a file to Write Binary
    pickle.dump(catalog, writer)
    writer.close() # close stream, release the file
    print("** Data serialized!")

def deserialize_catalog():
    try:
        global data_file
        reader = open(data_file, 'rb') # open file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        print("** Deserialized " + str(len(catalog)) + " items")
    
    except:
        print("Error, could not load data")

#fn

def register_item():
    try:
        print_header("Register New Item")
        title = input('Please provide the Title: ')
        cat = input('Please provide the Category: ')
        price = float(input('Please provide the Price: '))
        stock = int(input('Please provide the Stock: '))

        id = 1
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("You now have: " + str(how_many) + " items on the catalog")

    except ValueError:
        print("Error: Incorrect value, try again")
    except: 
        print("Error, Somthing went wrong")
    
def display_catalog():
    print_header("Your Current Catalog")
    # travel the list
    # # print the title
    for item in catalog:
        print_item(item)
        
    
def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if (item.stock == 0):
            print_item(item)

def total_stock_value():
    
    total = 0.0
    for item in catalog:
        total += item.price * item.stock

    print("Total value: " + str(total))

def list_of_categories():
    result = []
    num = 0
    print_header("List of Catagories")
    for item in catalog:
        if item.category not in result:
            result.append(item.category)
    for item in result:
        num += 1
        print(" Category "+ str(num) + item.rjust(30)) 


deserialize_catalog()
input("Press Enter to continue")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()

    opc = input("Please choose an option: ")

    # if comparisons
    if(opc == 'x'):
        break
    if(opc == '1'):
        register_item()
        serialize_catalog()
    elif(opc == '2'):
        display_catalog()

    # elif(opc == '3'): 
       
    # elif(opc == '4'):
        
    # elif(opc == '5'):

    elif(opc == '6'):
         display_out_of_stock() 
    elif(opc == '7'):
        total_stock_value()
    elif(opc == '8'):
        list_of_categories()
        
    
    

    else:
        print("Please choose a valid option")
    
    input("Press Enter to continue...")
    clear()

print('Good Bye!!')