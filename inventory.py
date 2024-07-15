import json
import os

class Inventory:
    def __init__(self, product_file='data/products.json'):
        self.product_file = product_file
        self.products = self.load_products()

    def load_products(self):
        if not os.path.exists(self.product_file):
            return {}
        with open(self.product_file, 'r') as file:
            return json.load(file)

    def save_products(self):
        with open(self.product_file, 'w') as file:
            json.dump(self.products, file, indent=4)

    def add_product(self, product_id, name, quantity, price):
        if product_id in self.products:
            return False, "Product ID already exists."
        self.products[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.save_products()
        return True, "Product added successfully."

    def edit_product(self, product_id, name=None, quantity=None, price=None):
        if product_id not in self.products:
            return False, "Product ID does not exist."
        if name:
            self.products[product_id]['name'] = name
        if quantity is not None:
            self.products[product_id]['quantity'] = quantity
        if price is not None:
            self.products[product_id]['price'] = price
        self.save_products()
        return True, "Product updated successfully."

    def delete_product(self, product_id):
        if product_id not in self.products:
            return False, "Product ID does not exist."
        del self.products[product_id]
        self.save_products()
        return True, "Product deleted successfully."

    def low_stock_alerts(self, threshold=5):
        alerts = []
        for product_id, product in self.products.items():
            if product['quantity'] < threshold:
                alerts.append(product_id)
        return alerts

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    print(inventory.add_product("001", "Widget", 10, 2.99))
    print(inventory.edit_product("001", quantity=4))
    print(inventory.low_stock_alerts())
    #print(inventory.delete_product("001"))
