class Customer:

    def __init__(
        self,
        customer_id,
        name,
        phone,
        email,
        address
    ):

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):

        return (
            f"\nID: {self.customer_id}"
            f"\nTên: {self.name}"
            f"\nSĐT: {self.phone}"
            f"\nEmail: {self.email}"
            f"\nĐịa chỉ: {self.address}"
        )