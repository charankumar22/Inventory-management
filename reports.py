import json
import os
from datetime import datetime

class Reports:
    def __init__(self, sales_file='data/sales.json'):
        self.sales_file = sales_file
        self.sales = self.load_sales()

    def load_sales(self):
        if not os.path.exists(self.sales_file):
            return []
        with open(self.sales_file, 'r') as file:
            return json.load(file)

    def save_sales(self):
        with open(self.sales_file, 'w') as file:
            json.dump(self.sales, file, indent=4)

    def add_sale(self, product_id, quantity, price):
        sale = {
            "product_id": product_id,
            "quantity": quantity,
            "price": price,
            "timestamp": datetime.now().isoformat()
        }
        self.sales.append(sale)
        self.save_sales()
        return True, "Sale recorded successfully."

    def sales_summary(self):
        summary = {}
        for sale in self.sales:
            product_id = sale['product_id']
            if product_id not in summary:
                summary[product_id] = {
                    "total_quantity": 0,
                    "total_revenue": 0.0
                }
            summary[product_id]['total_quantity'] += sale['quantity']
            summary[product_id]['total_revenue'] += sale['quantity'] * sale['price']
        return summary

# Example usage
if __name__ == "__main__":
    reports = Reports()
    print(reports.add_sale("001", 2, 2.99))
    print(reports.sales_summary())
