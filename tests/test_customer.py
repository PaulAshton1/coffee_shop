from customer import Customer
from coffee import Coffee

def test_create_order():
    c = Customer("Alex")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 4.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5
