class CustomerView:

    # =========================
    # INPUT
    # =========================
    def input_customer(self):

        customer_id = input("ID khách: ")

        name = input("Tên khách: ")

        phone = input("SĐT: ")

        email = input("Email: ")

        address = input("Địa chỉ: ")

        return (
            customer_id,
            name,
            phone,
            email,
            address
        )

    # =========================
    # DISPLAY
    # =========================
    def display_customers(
        self,
        customers
    ):

        if not customers:

            print("Không có khách hàng.")

            return

        for customer in customers:

            print(customer)

            print("-" * 40)

    # =========================
    # DELETE
    # =========================
    def input_delete_id(self):

        return input(
            "Nhập ID khách cần xóa: "
        )

    # =========================
    # SEARCH
    # =========================
    def input_search_keyword(self):

        return input(
            "Nhập tên khách hàng: "
        )

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, message):

        print(message)