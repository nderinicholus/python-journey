from datetime import date
products = [
    {"name": "Laptop", "price": 85000, "quantity": 1},
    {"name": "Phone", "price": 60000, "quantity": 2},
    {"name": "Headphones", "price": 4000, "quantity": 3},
]


def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"] * product["quantity"]
    return total


calculate_total(products)


def apply_discount(total, percent):
    discount = total * (percent / 100)
    return int(total - discount)


def show_receipt(products, discount_percent):
    print(f"====== RECEIPT ======")
    print(f"Date: {date.today()}")
    print()
    for product in products:
        name = product["name"]
        quantity = product["quantity"]
        line_total = product["price"] * product["quantity"]
        print(f"{name:<12} x{quantity} KES {line_total:,}")
    print("---------------------")
    subtotal = calculate_total(products)
    final = apply_discount(subtotal, discount_percent)
    print(f"Subtotal: KES {subtotal:,}")
    print(f"Discount: {discount_percent}% off")
    print(f"Total: KES {final:,}")
    print("===================")


show_receipt(products, 10)
