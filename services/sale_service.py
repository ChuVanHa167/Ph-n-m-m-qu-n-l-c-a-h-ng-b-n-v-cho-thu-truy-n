from repositories.sale_repository import (
    SaleRepository
)

from repositories.comic_repository import (
    ComicRepository
)

from repositories.customer_repository import (
    CustomerRepository
)

from services.notification_service import (
    NotificationService
)

from observers.rental_observer import (
    RentalObserver
)


class SaleService:

    def __init__(self):

        self.sale_repository = (
            SaleRepository()
        )

        self.comic_repository = (
            ComicRepository()
        )

        self.customer_repository = (
            CustomerRepository()
        )

        self.notification_service = (
            NotificationService()
        )

        self.notification_service.add_observer(
            RentalObserver()
        )

    # =========================
    # BÁN TRUYỆN
    # =========================
    def sell_comic(self, customer_id, comic_id, quantity):

        customer = self.customer_repository.find_by_id(customer_id)
        if customer is None:
            return "Khách hàng không tồn tại."

        comic = self.comic_repository.find_by_id(comic_id)
        if comic is None:
            return "Truyện không tồn tại."

        if quantity <= 0:
            return "Số lượng không hợp lệ"

        if comic.quantity < quantity:
            return "Không đủ truyện trên kệ."

        try:
            total_price = comic.price * quantity

            self.sale_repository.create_sale(
                customer_id,
                comic_id,
                quantity,
                total_price
            )

            comic.quantity -= quantity
            self.comic_repository.update(comic)

            self.notification_service.notify(
                f"{customer.name} đã mua {quantity} {comic.title}"
            )

            return f"Bán thành công. Tổng tiền: {total_price}"

        except Exception as e:
            return f"Lỗi giao dịch: {str(e)}"

    # =========================
    # LỊCH SỬ BÁN
    # =========================
    def get_all_sales(self):

        return (
            self.sale_repository.get_all()
        )

    # =========================
    # DOANH THU
    # =========================
    def get_total_revenue(self):

        return (
            self.sale_repository
            .get_total_revenue()
        )