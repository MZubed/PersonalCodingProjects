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
                print('prodmenu')
                #prodmenu()
            elif menu.strip() == '3':
                print('ordmenu')
                #ordmenu()
            elif menu.strip() == '4':
                print('couriersMenu')
                #couriersMenu()
            elif int(menu.strip()) not in range(1,5):
                print('Insufficient input, please select a number in the list')
        except: print('error')