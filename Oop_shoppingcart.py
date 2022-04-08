class ShoppingCart:
    def __init__(self):
        self.cart_list = []

    def format_cart(self):
        for i in self.cart_list:
            for k, v in i.items():
                print(f"{k.title()}: {v}")
            print('\n')

    def run(self):
        print("Select the items you want to add to your cart...")

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

                self.cart_list.append(item_list)

            if decision == 'n':
                done = True

        self.format_cart()

cart = ShoppingCart
cart.run(ShoppingCart())