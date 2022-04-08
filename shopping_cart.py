# Build a shopping cart

def format_cart():
    for i in cart:
        for k, v in i.items():
            print(f"{k.title()}: {v}")
        print('\n')


def cart ():
    cart_list = []

    done = False
    while not done:
        decision = input("Would you like to add to your cart?  Y/N? ").lower()

        if decision == 'y':
            item = input("What would you like to put in your list? ")
            qnty = int(input("How much would you like to add? "))

            item_list = {
                'item': item,
                'quantity': qnty
            }

            cart_list.append(item_list)

        if decision == 'n':
            done = True

    format_cart(cart_list)

cart()


