from enum import Enum

class UserType(Enum):
    USER = "User"
    ADMIN = "Admin"

class Customer:
    customers = {}

    def __init__(self, customer_name: str, city: str):
        self.id = None  # ID should be assigned from the database or a unique generator
        self.customer_id = None  # This should be assigned separately
        self.customer_name = customer_name
        self.city = city

    def display_customer_details(self):
        print(f"Customer ID : {self.customer_id}")
        print(f"Customer Name : {self.customer_name}")
        print(f"City : {self.city}")

    @classmethod
    def get_customers(cls):
        return cls.customers

    @classmethod
    def set_customers(cls, customers):
        cls.customers = customers

    def __repr__(self):
        return f"Customer(CustomerId={self.customer_id}, Name={self.customer_name}, City={self.city})"

# Example usage:
if __name__ == "__main__":
    customer1 = Customer("John Doe", "New York")
    customer1.customer_id = "C12345"
    customer1.display_customer_details()
