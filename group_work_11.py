print("ONLINE FOOD DELIVERY SYSTEM")
from collections import deque
restaurants=[
    {"RestaurantId": 1001, "RestaurantName": "PIZZA PALACE", "Menu": {"Pepperoni Pizza": 12, "Soda":1}}, 
    {"RestaurantId": 1002, "RestaurantName": "BURGER HOUSE", "Menu": {"Cheeseburger": 8, "Special Omlette": 10.}},
    {"RestaurantId": 1003, "RestaurantName": "LA TARTE",     "Menu": {"Donuts with cream":0.3, "Cake": 0.1}},
    {"RestaurantId": 1004, "RestaurantName": "AUBINASOM",    "Menu": {"Chips":1, "Pain Chocolat":0.2}},
    {"RestaurantId": 1005, "RestaurantName": "HEAVEN",       "Menu": {"Rice With Meat":0.8, "Tea":0.5}},
    {"RestaurantId": 1006, "RestaurantName": "EDEN CAFE",    "Menu": {"Coffe":2, "Smoothie":3}},
    {"RestaurantId": 1007, "RestaurantName": "GOOD LIFE",    "Menu": {"Pepperoni Pizza":11, "Milk":0.5}},
    {"RestaurantId": 1008, "RestaurantName": "144",          "Menu": {"Burger":8, "Baked Soda Bread":3}},
    {"RestaurantId": 1009, "RestaurantName": "SWEET FAST FOOD", "Menu": {"Ceaser Salad":12, "Margherita Pizza":10}},
    {"RestaurantId": 1010, "RestaurantName": "URUMURI",      "Menu": {"Spaghetti Carbonara": 12, "Beef Stroganoff": 20}},
    {"RestaurantId": 1011, "RestaurantName": "FRESH DISHES", "Menu": {"Pad Thai": 12, "Chicken Parmesan": 15}},
    {"RestaurantId": 1012, "RestaurantName": "KITCHEN WORKS","Menu": {"Shrimp Scampi": 18, "Grilled Salmon": 20}},
    {"RestaurantId": 1013, "RestaurantName": "FOODIE LIFE",  "Menu": {"Lamb Chops": 30, "Fish And Chips": 20}},
    {"RestaurantId": 1014, "RestaurantName": "CHIPOTLE",     "Menu": {"Burrito": 10, "Chicken Tikka Masala": 17}},
    {"RestaurantId": 1014, "RestaurantName": "BURGER KING",  "Menu": {"Hamburger": 9, "Pepperoni Pizza": 15}},
    {"RestaurantId": 1015, "RestaurantName": "OCEAN LIFE",   "Menu": {"Sushi Rolls": 18, "Cheeseburger": 12}},
    {"RestaurantId": 1016, "RestaurantName": "COOKVIE",      "Menu": {"Steak Frites": 20, "Eggplant Parmesan": 15}},
    {"RestaurantId": 1017, "RestaurantName": "FRESH MENU",   "Menu": {"Lobster Bisque": 17, "French Onion Soup": 14}},
    {"RestaurantId": 1018, "RestaurantName": "KFC",          "Menu": {"Chicken Wings": 12, "Buffalo Wings": 12}},
    {"RestaurantId": 1019, "RestaurantName": "FRIES",        "Menu": {"BBQ Ribs": 18, "Fried Fish": 8}},
    {"RestaurantId": 1020, "RestaurantName": "FOOD CORNER",  "Menu": {"Vegetable StirFry": 15, "Crab Cakes": 20}},
    {"RestaurantId": 1021, "RestaurantName": "ROLEX STORE",  "Menu": {"Rolex with chips": 2, "Regular Rolex": 1.5}},
    {"RestaurantId": 1022, "RestaurantName": "PASTA PLACE",  "Menu": {"Pasta primavera": 12, "Moussaka":17}},
]
orderqueue=deque()
modificationstack=[]
def showrestaurants():
    print("\nAvailable restaurants and Menus:")
    for restaurant in restaurants:
        print(f"{restaurant['RestaurantName']}:")
        for item, price in restaurant['Menu'].items():
            print(f"  {item} - ${price:.2f}")
    print("\n")    
def placeorder(RestaurantId, item):
    restaurant=next((r for r in restaurants if r['RestaurantId']==RestaurantId), None)
    if  restaurant and item in restaurant['Menu']:
        order={
               "RestaurantName": restaurant['RestaurantName'], 
               "item":item, 
               "price": restaurant['Menu'][item]
        } 
        orderqueue.append(order)
        print(f"\nOrder Placed:  {item} from {restaurant['RestaurantName']} at ${restaurant['Menu'][item]:.2f}\n")
    else:
         print("Invalid Restaurant or item.")
    
def modifylastorder(newitem):
    if orderqueue:
        lastorder = orderqueue.pop() 
        restaurant = next((r for r in restaurants if r['RestaurantName'] == lastorder['RestaurantName']), None)
        
        if restaurant and newitem in restaurant['Menu']: 
            lastorder['item'] = newitem 
            lastorder['price'] = restaurant['Menu'][newitem]
            modificationstack.append(lastorder)
            print(f"Order modified. New item: {newitem} from {lastorder['RestaurantName']} at ${lastorder['price']:.2f}")
        else:
            print(f"Ooops!!!. {newitem} is not on the menu of {lastorder['RestaurantName']}.")
            orderqueue.append(lastorder) 
    else:
        print("No orders to modify.")

def vieworders():
    if orderqueue:
        print("\nCurrent orders in Queue:")
        for order in orderqueue:
            print(f"  {order['item']} from {order['RestaurantName']} at ${order['price']:.2f}")
    else:
        print("\nNo current orders.")
def viewmodifications():
    if modificationstack:
        print("\nModifications (Last one handled first):")
        for mod in modificationstack:
            print(f"{mod['item']} from {mod['RestaurantName']} at ${mod['price']:.2f}")
    else:
        print("\nNo modifications available.")
def menu():
    while True:
        print("\n1. Show available Restaurants and Menus.")
        print("2. Place order.")
        print("3. Modify last order.")
        print("4. View current Orders.")
        print("5. View modifications.")
        print("6. EXIT.")
        choice=input("\nChoose an option (1 up to 6):")
        if choice=='1':
            showrestaurants()
        elif choice=='2':
            try:
                RestaurantId=int(input("\nEnter Restaurant ID:"))
                item=input("Enter Menu item:")
                placeorder(RestaurantId, item)
            except ValueError:
                print("Invalid input. please try again.")
        elif choice=='3':
            newitem=input("\nEnter new item for last order:")
            modifylastorder(newitem)
        elif choice=='4':
            vieworders()
        elif choice=='5':
            viewmodifications()
        elif choice=='6':
            print("\nExiting the system. Have a good time!!!")
            break
        else:
            print("\nInvalid option. Please select a valid option.")
menu()