#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Reading the Inventory
fd = open("Invent.txt",'w')
fd.close()


# In[12]:


fd = open('Invent.txt','r')
products = fd.read().split('\n')
fd.close()


# In[13]:


for i in products:
    print(i)
    


# In[31]:


# Noting the time of transaction
import time

#Taking the user input
ui_username = input("Enter your Name :")
ui_phone = input("Enter your Phone No :")
ui_mail = input("Enter your Mail :")
ui_prod_id = input("Enter product id :")
ui_prod_qn = input("Enter product Quantity :")
updated_product_lst = []

#Going through each product detail
for product in products:
    prod_details = product.split(',')
    if(prod_details[0] == ui_prod_id):
        
        # Checking if the product exists or not
        if(int(ui_prod_qn)<= int(prod_details[3])):
            #if we are having enough quantity or not
            print("-------------------------")
            print("Product Name  :", prod_details[1])
            print("Price  :", prod_details[2])
            print("Quantity :", ui_prod_qn)
            print("-------------------------")
            print("Billing Amount  :" , int(ui_prod_qn) * int(ui_prod_qn))
            print("-------------------------")
            
            #updating our inventory list
            prod_details[3] = str(int(prod_details[3]) -int( ui_prod_qn))
            
            #Generating sales in Sales.txt
            fd = open("Sales.txt",'a')
            sales_detail = ui_username+ ","+ ui_phone+ ","+ui_mail+ ","+ui_prod_id+ ","+ui_prod_qn+ ","+ str(int(ui_prod_qn) * int(prod_details[2]))+ ","+time.ctime()+"\n"
            fd.write(sales_detail)
            fd.close()
            
        else:
        #if we are having enough quantity or not
            print("Sorry , We're not having enough quantity .")
            print("We're having only" , prod_details[3],'quantity .')
            print("Would you like to purchase it ?")
            ch = input("Press Y/N")
            if(ch== 'Y' or ch=='y'):
                # if you want to purchase with remaing stock
                print("-------------------------")
                print("Product Name  :", prod_details[1])
                print("Price  :", prod_details[2])
                print("Quantity :", prod_details[3])
                print("-------------------------")
                print("Billing Amount  :" , int(prod_details[3]) * int(ui_prod_qn))
                print("-------------------------")
                
                #updating our inventory list
                prod_details[3] = '0'
            else:
                print("Thanks")
                
            
    #updating my inventory list        
    updated_product_lst.append(prod_details)
import os
file_path = 'Invent.txt'

#updating my inventory string and file
fd = open("Invent.txt",'w')
for i in updated_product_lst:
    prod = i[0]+","+i[1]+"," +i[2]+","+i[3]+ '\n'
    fd.write(prod)
fd.close()
print("-------------------------")
print("inventory Updated")

        
    
        
        


# In[27]:





# In[28]:





# In[ ]:




