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
    def sell_comic(
        self,
        customer_id,
        comic_id,
        quantity
    ):

        # Kiểm tra khách
        customer = (
            self.customer_repository
            .find_by_id(customer_id)
        )

        if customer is None:

            return "Khách hàng không tồn tại."

        # Kiểm tra truyện
        comic = (
            self.comic_repository
            .find_by_id(comic_id)
        )

        if comic is None:

            return "Truyện không tồn tại."

        # Kiểm tra số lượng
        if comic.quantity < quantity:

            return (
                "Không đủ truyện "
                "trên kệ."
            )

        # Tính tiền
        total_price = (
            comic.price * quantity
        )

        # Tạo hóa đơn
        self.sale_repository.create_sale(
            customer_id,
            comic_id,
            quantity,
            total_price
        )

        # Trừ số lượng
        comic.quantity -= quantity

        self.comic_repository.update(comic)

        # Notification
        self.notification_service.notify(
            f"{customer.name} "
            f"đã mua "
            f"{quantity} "
            f"truyện "
            f"{comic.title}"
        )

        return (
            f"Bán truyện thành công. "
            f"Tổng tiền: {total_price}"
        )

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