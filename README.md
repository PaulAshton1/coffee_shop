# Coffee Shop Management System

This project is a simple Python-based coffee shop management system. It models customers, coffees, and orders, and provides functionality to track orders, calculate statistics, and identify top customers.

## Features

- **Customer Management:**  
  Create customers with validated names and email addresses.

- **Coffee Management:**  
  Define coffee types with names and prices.

- **Order Tracking:**  
  Customers can place orders for coffees at specific prices. All orders are timestamped and tracked.

- **Statistics:**  
  - Count the number of orders for each coffee.
  - Calculate the average price paid for each coffee.
  - Identify the customer who orders a specific coffee the most ("aficionado").

## Project Structure

- [`coffee.py`](coffee.py): Defines the `Coffee` class.
- [`customer.py`](customer.py): Defines the `Customer` class.
- [`order.py`](order.py): Defines the `Order` class and manages all orders.
- [`debug.py`](debug.py): Example usage and debugging output.
- [`tests/`](tests/):  
  - [`test_coffee.py`](tests/test_coffee.py): Unit tests for coffee-related functionality.
  - [`test_customer.py`](tests/test_customer.py): Unit tests for customer-related functionality.

