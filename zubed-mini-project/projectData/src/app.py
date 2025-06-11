import csv

#LOADING COURIERS
with open('C:/Users/mzube/OneDrive/Documents/my-reps/zubed-mini-project/week1/data/couriers.txt','r') as file:
    courierReader=csv.DictReader(file)
    couriersList=[couriers for couriers in courierReader]
    print(couriersList)

#LOADING PRODUCTS
with open('C:/Users/mzube/OneDrive/Documents/my-reps/zubed-mini-project/week1/data/products.txt','r') as file:
    productReader=csv.DictReader(file)
    productsList=[products for products in productReader]
    print(productsList)

#LOADING ORDERS
with open('C:/Users/mzube/OneDrive/Documents/my-reps/zubed-mini-project/week1/data/orders.txt','r') as file:
    ordersReader=csv.DictReader(file)
    ordersList=[orders for orders in ordersReader]
    print(ordersList)

#ERROR MESSAGE
def error():
    print("Insufficient input, please try again.")

#ORDERS LIST WITH INDEX VALUES
def ordersListFunc():
    for orders in ordersList:
        print(ordersList.index(orders)+1,orders)

#VERTICAL PRODUCT LIST WITH NUMBERS
def productsListFunc():
    for products in productsList:
        print(productsList.index(products)+1,products)

#VERTICAL COURIERS LIST WITH NUMBERS
def couriersListFunc():
    for couriers in couriersList:
        print(couriersList.index(couriers)+1,couriers)

#MAIN MENU    
def main():
    while True:
        try:
            menu = input("\
Please select one of the following options:\
\n1-Exit App\
\n2-Print Product Menu\
\n3-Orders Menu\
\n4-Couriers Menu\n")
#
            if menu.strip() == '1':
                print('Exiting App')
                productsList
                with open('C:/Users/mzube/OneDrive/Documents/my-reps/zubed-mini-project/week1/data/products.txt','w',newline='') as file:
                    fieldnames=['product','price']
                    writer=csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(productsList)
                with open('C:/Users/mzube/OneDrive/Documents/my-reps/zubed-mini-project/week1/data/couriers.txt','w',newline='') as file:
                    fieldnames=['courier name','courier phone']
                    writer=csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(couriersList)
                with open('C:/Users/mzube/OneDrive/Documents/my-reps/zubed-mini-project/week1/data/orders.txt','w',newline='') as file:
                    fieldnames=['Customer Name','Customer Address','Customer Phone','Customer Courier','Status','Customer Product']
                    writer=csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(ordersList)
                break
            elif menu.strip()== '2':
                prodmenu()
            elif menu.strip() == '3':
                ordmenu()
            elif menu.strip() == '4':
                couriersMenu()
            elif int(menu.strip()) not in range(1,5):
                print('Insufficient input, please select a number in the list')
        except: error()
        

#PRODUCT MENU
def prodmenu():
    while True:
        try:
            pl=input('\
Please select one of the following options:\
\n1-Return to main menu\
\n2-Print Product List\
\n3-Create New Product\
\n4-Update Existing Product\
\n5-Delete Product\n')
            if pl.strip()== '1':
                print('Returning to main menu')
                break
                main()
            elif pl.strip()== '2':
                if not productsList:
                    print('There are currently no products ')
                else: productsListFunc()
            elif pl.strip() == '3':
                createProd()
            elif pl.strip() == '4':
                updateProd()
            elif pl.strip() == '5':
                deleteProd()
            elif int(pl.strip()) not in range(1,6):
                print('Insufficient input, please select a number in the list')
        except: print('Insufficient input, please input an integer') 

#ORDER MENU
def ordmenu():
    while True:
        try:
            om=input('\
Please select one of the following options:\
\n1-Return to Main Menu\
\n2-Print Orders Dictionary\
\n3-Create New Order\
\n4-Update Existing Order Status\
\n5-Update Existing Order\
\n6-Delete Order\n')
            if om.strip() == "1":
                break
                main()
            elif om.strip() == '2':
                if not ordersList:
                    print('There are no orders currently available')
                else:ordersListFunc()
            elif om.strip() == '3':
                createOrder()
            elif om.strip() == '4':
                if not ordersList:
                    print('There are currently no orders available')
                    ordmenu()
                else:updateOrdStatus()
            elif om.strip() == '5':
                if not ordersList:
                    print('There are currently no orders available')
                    ordmenu()
                else:updateOrd()
            elif om.strip() == '6':
                deleteOrd()
            elif int(om.strip()) not in range(1,7):
                print('Insufficient input, please select a number in the list')
        except: print('Insufficient input, please input an integer') 

#COURIERS MENU
def couriersMenu():
    while True:
        #try:
            couriersMenu = input("\
Please select one of the following options:\
\n1-Return to Main Menu\
\n2-Print Couriers List\
\n3-Create New Courier\
\n4-Update Existing Courier\
\n5-Delete Courier\n")
            if couriersMenu.strip() == '1':
                print('Returning to Main Menu')
                break
                main()
            elif couriersMenu.strip()== '2':
                if not couriersList:
                    print('No couriers currently available')
                else: couriersListFunc()
            elif couriersMenu.strip() == '3':
                createCourier()
            elif couriersMenu.strip() == '4':
                updateCourier()
            elif couriersMenu.strip() == '5':
                deleteCourier()   
            elif int(couriersMenu.strip()) not in range(1,6):
                print('Insufficient input, please select a number in the list')
        #except: print('Insufficient input, please input an integer value') 

#CREATE PRODUCTS
def createProd():
    productsListFunc()
    try:
        newProduct=input('Please enter a new product\n')
        if newProduct in productsList:
            print('This item is already in the menu')
            return
        elif not newProduct:
            print('Please input a product')
            return
        newPrice=float(input('Please enter the price of this product\n'))
        if not newPrice:
            print('Please input a number value')
        else:
            productsDict={'product':newProduct,'price':f'£{newPrice:.2f}'}
        productsList.append(productsDict)
        productsListFunc()
    except: print('Insufficient input, please input an integer') 


class createProducts:
    def __init__(self,product,price):
        self.product=product
        self.price=price

#UPDATE PRODUCT
def updateProd():
    productsListFunc()
    try: 
        prodUpd=input("Which product do you want to update? Please select a number:\n")
        if not prodUpd:
            print('Please select a product')
            return
        selectNoP=int(input('Would you like to update product or price?\nPlease select a number\n1. Product\n2. Price\n'))
        if selectNoP==1:
            productsList[int(prodUpd)-1]['product']=input('What would you like to update the product to?\n')
        elif selectNoP==2:
            productsList[int(prodUpd)-1]['price']=f'£{input('What would you like to update the price to?\n')}'
        print(productsList[int(prodUpd)-1]) 
    except: print('Insufficient input, please input an integer value')

#DELETE PRODUCT            
def deleteProd():
    productsListFunc()
    try:
        delete = input('Which product do you want to remove? Please select a number:\n')
        if not delete:
            print('Insufficient input, please select an integer')
            return
        else:
            del productsList[int(delete)-1] 
            print('Here is your updated list:')
            productsListFunc()
    except: error()

#CREATE ORDER
def createOrder():
    #try:
        try:
            customerName = input('Please enter a name:\n')
            val=str(customerName)
            if not customerName:
                print('Insufficient input, please enter a name')
                return
        except ValueError:
            print('Insufficient input, only letters accepted')
            return
        customerAdd = input('Please enter an address:\n')
        if not customerAdd:
            print('Insufficient input, please enter an address')
            return
        try:
            customerPhone = input('Please enter a phone number:\n')
            val=int(customerPhone)
            if not customerPhone:
                print('Insufficient input, please enter a phone number')
                return
        except ValueError:
            print('Insufficient input, letters not excepted')
            return
        couriersListFunc()
        courierChoice=input('Please select a courier\n')
        try:
            if not courierChoice:
                print('Insufficient input, please select a courier')
                return
        except ValueError:
            print('Insufficient input, only letters accepted')
            return
        productsListFunc()
        productChoice=input('Please select an item\n')
        try:
            if not productChoice:
                print('Insufficient input, please select a product')
                return
        except ValueError:
            print('Insufficient input, only letters accepted')
            return
        ordersDict={'Customer Name':customerName,'Customer Address':customerAdd,'Customer Phone':int(customerPhone),'Customer Courier':courierChoice, 'Status':'Preparing','Customer Product':productChoice}
        ordersList.append(ordersDict)
        print('Here is your order')
        ordersListFunc()
    #except: error()

#UPDATE EXISTING ORDER STATUS
def updateOrdStatus():
    try:
        ordersListFunc()
        customerUpd = input('Which one would you like to update the status of?\n')
        if not customerUpd:
            print('Insufficient input, please input an integer value')
        else:
            for i in ordersList:
                if int(customerUpd)-1 not in range(0,ordersList.index(i)+1):
                    print('Insufficient input, please select an integer within range')
                else:
                    selectUpd=input('What is the status of this order?\n')
                    ordersList[int(customerUpd)]['Status']=selectUpd
                    ordersListFunc()
    except:error()
    

#UPDATE EXISTING ORDER
def updateOrd():
    ordersListFunc()
    try:
        customerUpd = input('Which one would you like to update the status of?\n')
        if not customerUpd:
            print('Insufficient input, please input a value')
        else:
            for i in ordersList:
                if int(customerUpd)-1 not in range(0,ordersList.index(i)+1):
                    print('Insufficient input, please select an integer within range')
                elif int(customerUpd)-1 in range(0,ordersList.index(i)+1):
                    orderUpd=int(input('Which piece of info would you like to update\n1.Customer Name\n2.Customer Address\n3.Customer Phone\n4.Customer Product\n5.Customer Courier\n'))
                    if orderUpd == 1:
                        print(ordersList[customerUpd]['Customer Name'])
                        ordersList[customerUpd]['Customer Name']=input('Please input a new name\n')
                    elif orderUpd == 2:
                        print(ordersList[customerUpd]['Customer Address'])
                        ordersList[customerUpd]['Customer Address']=input('Please input a new address\n')
                    elif orderUpd == 3:
                        print(ordersList[customerUpd]['Customer Phone'])
                        ordersList[customerUpd]['Customer Phone']=input('Please input a new phone number\n')
                    elif orderUpd == 4:
                        productsListFunc()
                        ordersList[customerUpd]['Customer Product']=input('Please input a new product\n')
                    elif orderUpd == 5:
                        couriersListFunc()
                        ordersList[customerUpd]['Customer Courier']=input('Please input a new courier\n')
                    elif not orderUpd:
                        print('Insufficient input, please input an integer on the list')
                    ordersListFunc()
    except:error()
    
#DELETE ORDER
def deleteOrd():
    if not ordersList:
        print('There are currently no orders available')
        ordmenu()
    else:
        try:
            ordersListFunc()
            delete=input('Which order would you like to delete?\n')
            if not delete:
                print('Insufficient input, please select an integer')
                ordmenu()
            for orders in ordersList:
                if int(delete)-1 not in range(0,ordersList.index(orders)+1):
                    print(range(0,ordersList.index(orders)+1))
                    print('Insufficient input, please select an integer within the range')
                    ordmenu()
            else:
                del ordersList[int(delete)-1]
            print('Here is your updated list:')
            ordersListFunc()
        except:error()

#CREATE COURIER
def createCourier():
    courierName=input('Please enter a courier name\n')
    courierPhone=input('Please enter a courier phone number\n')
    couriersDict={'courier name':courierName,'courier phone':courierPhone}
    couriersList.append(couriersDict)
    couriersListFunc()   

#UPDATE COURIER
def updateCourier():
    couriersListFunc()
    #try: 
    courUpd=int(input("Which courier do you want to update? Please select a number:\n")) - 1
    selectCour=int(input('Would you like to update courier name or phone?\nPlease select a number\n1. Name\n2. Phone\n'))
    if selectCour==1:
        couriersList[courUpd]['courier name']=input('What would you like to update the name to?\n')
    if selectCour==2:
        couriersList[courUpd]['courier phone']=input('What would you like to change the phone to\n')
    print('Here is your updated entry:')
    print(couriersList[courUpd])
    #except: error()

#DELETE COURIER
def deleteCourier():
    try:
        couriersListFunc()
        delete=input('Which courier do you want to delete? Please select a number\n')
        del couriersList[int(delete)-1]
        print('Here is your updated list:')
        couriersListFunc()
    except:error()

main()