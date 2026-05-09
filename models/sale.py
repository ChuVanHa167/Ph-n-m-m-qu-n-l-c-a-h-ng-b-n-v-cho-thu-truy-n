class Sale:

    def __init__(
        self,
        sale_id,
        customer_id,
        comic_id,
        quantity,
        total_price,
        sale_date
    ):

        self.sale_id = sale_id

        self.customer_id = customer_id

        self.comic_id = comic_id

        self.quantity = quantity

        self.total_price = total_price

        self.sale_date = sale_date

    def __str__(self):

        return (
            f"\nSale ID: {self.sale_id}"
            f"\nKhách hàng: {self.customer_id}"
            f"\nTruyện: {self.comic_id}"
            f"\nSố lượng: {self.quantity}"
            f"\nTổng tiền: {self.total_price}"
            f"\nNgày bán: {self.sale_date}"
        )