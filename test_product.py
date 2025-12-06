
from product import product_details

def test_product_details():
    expected_output = (
        "product ID: {p_id}\n"
        "product Name: {name}\n"
        "product quantity: {quantity}\n"
        "price: {price}"
    )

    assert product_details("p1001", "Laptop", 10,75000) == expected_output