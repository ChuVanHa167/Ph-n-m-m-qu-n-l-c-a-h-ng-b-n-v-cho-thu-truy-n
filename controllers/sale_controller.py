from services.sale_service import (
    SaleService
)


class SaleController:

    def __init__(self, view):

        self.view = view

        self.sale_service = (
            SaleService()
        )

    # =========================
    # SELL
    # =========================
    def sell_comic(self):

        customer_id, comic_id, quantity = (
            self.view.input_sale()
        )

        result = (
            self.sale_service.sell_comic(
                customer_id,
                comic_id,
                quantity
            )
        )

        self.view.show_message(result)

    # =========================
    # HISTORY
    # =========================
    def show_sales(self):

        sales = (
            self.sale_service
            .get_all_sales()
        )

        self.view.display_sales(
            sales
        )

    # =========================
    # REVENUE
    # =========================
    def show_revenue(self):

        revenue = (
            self.sale_service
            .get_total_revenue()
        )

        self.view.display_revenue(
            revenue
        )