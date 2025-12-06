def product_details(p_id, name, quantity, price):
    result = (
        f"product ID: {p_id}\n"
        f"product Name: {name}\n"
        f"product quantity: {quantity}\n"
        f"price: {price}"
    )
    return result
if __name__ == "__main__":
    p_id = "P1001"
    name = "Laptop"
    quantity = 10
    price = 75000
    print(product_details(p_id, name, quantity, price))
