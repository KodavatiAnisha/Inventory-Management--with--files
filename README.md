# Inventory-Management-System-Files-
The Inventory Management System is a Python-based console application designed to efficiently manage inventory, track sales, and handle customer interactions. Leveraging file handling capabilities, this system ensures accurate and organized data management, making it an essential tool for any retail or wholesale business.
'''
# Inventory Management and Billing System

This is a simple inventory management and billing system implemented in Python. The system reads product data from a text file, processes sales, and updates inventory accordingly. It also generates sales records and stores them in a separate file.

## Features

- *Load Inventory*: Reads inventory data from a text file.
- *Save Inventory*: Writes updated inventory data back to the text file.
- *Billing Process*: Generates bills for customer purchases and updates inventory.
- *Sales Record*: Maintains a record of sales in a separate file.

## File Structure

The inventory.txt file should have the following structure:


1,chocolate,10,100
2,biscuits,20,100
3,veggies,40,1000


Each line represents a product with the following fields:
- Product ID
- Product Name
- Product Price
- Product Quantity

## Usage

### Prerequisites

- Python 3.x

### Running the System

1. *Reading Inventory*: Reads the inventory from a text file and stores it in a list.

python
fd = open("inventory.txt", "r")
products = fd.read().split('\n')
fd.close()


2. *User Input*: Collects user information and desired product details.

python
import time

user_name = input("Enter your name: ")
user_phno = input("Enter your phone number: ")
uid = input("Enter product ID: ")
quantity = input("Enter product quantity: ")


3. *Processing Sales*: Processes the sale, updates inventory, and generates a sales record.

python
updated_products = []

for product in products:
    product_details = product.split(",")

    if product_details[0] == uid:
        if int(quantity) <= int(product_details[3]):
            print('_' * 30)
            print("Product Name:", product_details[1])
            print("Product ID  :", uid)
            print("Quantity    :", product_details[3])
            print("Price       :", product_details[2])
            print("Bill amount :", int(quantity) * int(product_details[2]))
            print('_' * 30)

            product_details[3] = str(int(product_details[3]) - int(quantity))

            fd = open("sales.txt", "a")
            sales_details = f"{user_name},{user_phno},{product_details[1]},{uid},{quantity},{int(quantity) * int(product_details[2])},{time.ctime()}\n"
            fd.write(sales_details)
            fd.close()
        else:
            print("Sorry, we do not have enough quantity.")
            print("We only have", product_details[3], "quantity.")
            ch = input("Would you like to purchase it? Enter Y/N: ")

            if ch in ('y', 'Y'):
                print('_' * 30)
                print("Product Name:", product_details[1])
                print("Product ID  :", uid)
                print("Quantity    :", product_details[3])
                print("Price       :", product_details[2])
                print("Bill amount :", int(product_details[3]) * int(product_details[2]))
                print('_' * 30)

                fd = open("sales.txt", "a")
                sales_details = f"{user_name},{user_phno},{product_details[1]},{uid},{product_details[3]},{int(product_details[3]) * int(product_details[2])},{time.ctime()}\n"
                fd.write(sales_details)
                fd.close()

                product_details[3] = '0'
            else:
                print('Thank you!')

    updated_products.append(product_details)

lst = [','.join(i) + "\n" for i in updated_products]
lst[-1] = lst[-1].strip()

fd = open("inventory.txt", "w")
fd.writelines(lst)
fd.close()

print("Inventory updated")


### Example Output

The example code will print the bill details and update the inventory in the inventory.txt file. It will also append the sale details to the sales.txt file.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.


### Instructions for Pushing to GitHub

1. Initialize a git repository:
   bash
   git init
   

2. Add the files to the repository:
   bash
   git add .
   

3. Commit the changes:
   bash
   git commit -m "Initial commit"
   

4. Add the remote repository 
   bash
   git remote add origin https://github.com/KodavatiAnisha/Inventory-Management--with--files/tree/main
   

5. Push the changes to GitHub:
   bash
   git push -u origin master
   ```

This README.md provides a clear overview of the project, its features, and how to use it, along with instructions for contributing and the license information.
