# program 1:welcome

def welcomemycafe():
    print("welcome my fresh juice cafe")

welcomemycafe()



# program 2: fun with para

def juice_order(juice, quantity):
    print("juice:", juice)
    print("quantity:", quantity)

juice_order("Mango_juice", 2)


# program 3: fun with return value

def calculate_bill(price, quantity):
    return price*quantity

total = calculate_bill(80, 3)
print("Total bill:", total)


# program 4: default argu
def juice_menu(juice="orange juice"):
    print("today's special:", juice)

juice_menu()
juice_menu("watermelon juice")


# program 5: key argu
def juice_details(name, price):
    print("juice:", name)
    print("price:", price)

juice_details(price=90, name="pineapple juice")


# program 6: variables length argu

def available_juice(*juices):
    print("Available juices:")

    for juice in juices:
        print(juice)

available_juice("mango juice", "apple juice", "orange juice", "grape juice")


# program 7: list as fun argu

def display_juices(juice_list):
    for juice in juice_list:
        print(juice)

juices = ["mango juice", "apple juice", "orange juice"]
display_juices(juices)


# program 8: dic as fun argu

def display_prices(menu):
    for juice, price in menu.items():
        print(juice, ":", price)

juice_menu_dict = { "mango juice": 80, "apple juice": 100, "orange juice": 70}

display_prices(juice_menu_dict)


# program 9: loop and cond
def check_price(menu):
    for juice, price in menu.items():
        if price > 90:
            print(juice, "- premium juice")
        else:
            print(juice, "- regular juice")

juice_menu_dict = {"mango juice": 80, "apple juice": 100, "orange juice": 70}
check_price(juice_menu_dict)



# program 10: fresh juice cafe
def add_juice(cafe, juice, price):
    cafe[juice] = price

def display_cafe(cafe):
    print("\nfresh juice cafe menu")
    for juice, price in cafe.items():
        print(juice, "-", price)

cafe = {}

add_juice(cafe, "mango juice", 80)
add_juice(cafe, "apple juice", 100)
add_juice(cafe, "orange juice", 70)

display_cafe(cafe)

