from services.customer_service import (
    CustomerService
)


class CustomerController:

    def __init__(self, view):

        self.view = view

        self.customer_service = (
            CustomerService()
        )

    # CREATE
    def add_customer(self):

        data = self.view.input_customer()

        self.customer_service.add_customer(
            *data
        )

        self.view.show_message(
            "Thêm khách hàng thành công."
        )

    # READ
    def show_customers(self):

        customers = (
            self.customer_service
            .get_all_customers()
        )

        self.view.display_customers(
            customers
        )

    # UPDATE
    def update_customer(self):

        data = self.view.input_customer()

        self.customer_service.update_customer(
            *data
        )

        self.view.show_message(
            "Cập nhật thành công."
        )

    # DELETE
    def delete_customer(self):

        customer_id = (
            self.view.input_delete_id()
        )

        self.customer_service.delete_customer(
            customer_id
        )

        self.view.show_message(
            "Xóa thành công."
        )

    # SEARCH
    def search_customer(self):

        keyword = (
            self.view.input_search_keyword()
        )

        customers = (
            self.customer_service
            .search_customer(keyword)
        )

        self.view.display_customers(
            customers
        )