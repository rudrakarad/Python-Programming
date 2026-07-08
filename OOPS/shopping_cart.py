
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to the cart successfully")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from the cart successfully")
        else:
            print(f"{item} not found in the cart")

    def view_cart(self):
        if not self.items:
            print("The cart is empty")
        else:
            for item in self.items:
                print(item)

obj = ShoppingCart()

obj.view_cart()
obj.add_item("Noodles")
obj.add_item("Tooth paste")
obj.add_item("Cold drinks")
obj.view_cart()
obj.remove_item("Cold drinks")
obj.view_cart()

    