import tkinter as tk
from tkinter import messagebox, ttk
from auth import Auth
from inventory import Inventory
from reports import Reports

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        self.auth = Auth()
        self.inventory = Inventory()
        self.reports = Reports()

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Register", command=self.register).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = self.auth.login(username, password)
        if success:
            messagebox.showinfo("Success", message)
            self.create_main_screen()
        else:
            messagebox.showerror("Error", message)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = self.auth.register(username, password)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def create_main_screen(self):
        self.clear_screen()
        tk.Button(self.root, text="Manage Products", command=self.manage_products).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.root, text="View Reports", command=self.view_reports).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Logout", command=self.create_login_screen).grid(row=0, column=2, padx=10, pady=10)
        self.display_products()

    def manage_products(self):
        self.clear_screen()
        tk.Button(self.root, text="Add Product", command=self.add_product_screen).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Edit Product", command=self.edit_product_screen).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Delete Product", command=self.delete_product_screen).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_screen).grid(row=1, column=0, columnspan=3, pady=10)
        self.display_products()

    def display_products(self):
        products = self.inventory.products
        if not products:
            tk.Label(self.root, text="No products available.").grid(row=2, column=0, columnspan=3, pady=10)
            return

        tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        
        for product_id, details in products.items():
            tree.insert("", tk.END, values=(product_id, details['name'], details['quantity'], details['price']))
        
        tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def add_product_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Product ID").grid(row=0, column=0, padx=10, pady=10)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Quantity").grid(row=2, column=0, padx=10, pady=10)
        self.product_quantity_entry = tk.Entry(self.root)
        self.product_quantity_entry.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Price").grid(row=3, column=0, padx=10, pady=10)
        self.product_price_entry = tk.Entry(self.root)
        self.product_price_entry.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Add", command=self.add_product).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Back", command=self.manage_products).grid(row=5, column=0, columnspan=2, pady=10)

    def add_product(self):
        product_id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        quantity = int(self.product_quantity_entry.get())
        price = float(self.product_price_entry.get())
        success, message = self.inventory.add_product(product_id, name, quantity, price)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
        self.manage_products()

    def edit_product_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Product ID").grid(row=0, column=0, padx=10, pady=10)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Quantity").grid(row=2, column=0, padx=10, pady=10)
        self.product_quantity_entry = tk.Entry(self.root)
        self.product_quantity_entry.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Price").grid(row=3, column=0, padx=10, pady=10)
        self.product_price_entry = tk.Entry(self.root)
        self.product_price_entry.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Update", command=self.edit_product).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Back", command=self.manage_products).grid(row=5, column=0, columnspan=2, pady=10)

    def edit_product(self):
        product_id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        quantity = int(self.product_quantity_entry.get())
        price = float(self.product_price_entry.get())
        success, message = self.inventory.edit_product(product_id, name, quantity, price)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
        self.manage_products()

    def delete_product_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Product ID").grid(row=0, column=0, padx=10, pady=10)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Delete", command=self.delete_product).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Back", command=self.manage_products).grid(row=2, column=0, columnspan=2, pady=10)

    def delete_product(self):
        product_id = self.product_id_entry.get()
        success, message = self.inventory.delete_product(product_id)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
        self.manage_products()

    def view_reports(self):
        self.clear_screen()
        summary = self.reports.sales_summary()
        row = 0
        for product_id, report in summary.items():
            tk.Label(self.root, text=f"Product ID: {product_id}").grid(row=row, column=0, padx=10, pady=10)
            tk.Label(self.root, text=f"Total Quantity Sold: {report['total_quantity']}").grid(row=row, column=1, padx=10, pady=10)
            tk.Label(self.root, text=f"Total Revenue: ${report['total_revenue']:.2f}").grid(row=row, column=2, padx=10, pady=10)
            row += 1
        tk.Button(self.root, text="Back", command=self.create_main_screen).grid(row=row, column=0, columnspan=3, pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
