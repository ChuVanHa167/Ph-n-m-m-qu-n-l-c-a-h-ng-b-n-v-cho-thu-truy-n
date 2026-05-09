from repositories.rental_repository import (
    RentalRepository
)

from repositories.comic_repository import (
    ComicRepository
)

from repositories.customer_repository import (
    CustomerRepository
)

from repositories.inventory_repository import (
    InventoryRepository
)

from services.notification_service import (
    NotificationService
)

from observers.rental_observer import (
    RentalObserver
)


class RentalService:

    def __init__(self):

        self.rental_repository = (
            RentalRepository()
        )

        self.comic_repository = (
            ComicRepository()
        )

        self.customer_repository = (
            CustomerRepository()
        )

        self.inventory_repository = (
            InventoryRepository()
        )

        # Observer
        self.notification_service = (
            NotificationService()
        )

        self.notification_service.add_observer(
            RentalObserver()
        )

    # =========================
    # THUÊ TRUYỆN
    # =========================
    def rent_comic(
        self,
        customer_id,
        comic_id
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
        if comic.quantity <= 0:
            return "Không còn truyện trên kệ."
        if comic is None:

            return "Truyện không tồn tại."

        # Kiểm tra tồn kệ
        if comic.quantity <= 0:

            return (
                "Không còn truyện "
                "trên kệ."
            )

        # Tạo phiếu thuê
        self.rental_repository.create_rental(
            customer_id,
            comic_id,
            comic.rental_price
        )

        # Trừ số lượng kệ
        comic.quantity -= 1

        self.comic_repository.update(comic)

        # Notification
        self.notification_service.notify(
            f"{customer.name} "
            f"đã thuê truyện "
            f"{comic.title}"
        )

        return "Thuê truyện thành công."

    # =========================
    # TRẢ TRUYỆN
    # =========================
    def return_comic(
        self,
        rental_id
    ):

        rental = (
            self.rental_repository
            .find_by_id(rental_id)
        )

        if rental is None:

            return "Không tìm thấy phiếu thuê."

        if rental.status == "DA_TRA":

            return "Truyện đã trả rồi."

        # Update rental
        self.rental_repository.return_comic(
            rental_id
        )

        # Tăng lại số lượng kệ
        comic = (
            self.comic_repository
            .find_by_id(
                rental.comic_id
            )
        )

        comic.quantity += 1

        self.comic_repository.update(comic)

        self.notification_service.notify(
            f"Đã trả truyện "
            f"{comic.title}"
        )

        return "Trả truyện thành công."

    # =========================
    # XEM LỊCH SỬ
    # =========================
    def get_all_rentals(self):

        return (
            self.rental_repository
            .get_all()
        )