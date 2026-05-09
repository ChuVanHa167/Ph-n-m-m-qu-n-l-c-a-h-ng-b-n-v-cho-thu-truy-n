from repositories.customer_repository import (
    CustomerRepository
)

from models.customer import Customer


class CustomerService:

    def __init__(self):

        self.repository = CustomerRepository()

    # CREATE
    def add_customer(
        self,
        customer_id,
        name,
        phone,
        email,
        address
    ):

        customer = Customer(
            customer_id,
            name,
            phone,
            email,
            address
        )

        self.repository.add(customer)

    # READ
    def get_all_customers(self):

        return self.repository.get_all()

    # UPDATE
    def update_customer(
        self,
        customer_id,
        name,
        phone,
        email,
        address
    ):

        customer = Customer(
            customer_id,
            name,
            phone,
            email,
            address
        )

        self.repository.update(customer)

    # DELETE
    def delete_customer(self, customer_id):

        self.repository.delete(customer_id)

    # SEARCH
    def search_customer(self, keyword):

        return self.repository.search_by_name(
            keyword
        )