from repositories.inventory_repository import (
    InventoryRepository
)

from repositories.comic_repository import (
    ComicRepository
)


class InventoryService:

    def __init__(self):

        self.inventory_repository = (
            InventoryRepository()
        )

        self.comic_repository = (
            ComicRepository()
        )

    # =========================
    # NHẬP KHO
    # =========================
    def import_comic_stock(
        self,
        comic_id,
        quantity
    ):

        comic = (
            self.comic_repository
            .find_by_id(comic_id)
        )

        if comic is None:
            return "Không tìm thấy truyện."

        self.inventory_repository.import_stock(
            comic_id,
            quantity
        )

        self.inventory_repository.add_inventory_log(
            comic_id,
            "IMPORT",
            quantity,
            "Nhập thêm hàng vào kho"
        )

        return "Nhập kho thành công."

    # =========================
    # XUẤT KHO
    # =========================
    def export_comic_stock(
        self,
        comic_id,
        quantity
    ):

        comic = (
            self.comic_repository
            .find_by_id(comic_id)
        )

        if comic is None:
            return "Không tìm thấy truyện."

        if comic.stock_quantity < quantity:

            return "Không đủ hàng trong kho."

        self.inventory_repository.export_stock(
            comic_id,
            quantity
        )

        self.inventory_repository.add_inventory_log(
            comic_id,
            "EXPORT",
            quantity,
            "Xuất hàng khỏi kho"
        )

        return "Xuất kho thành công."

    # =========================
    # CHUYỂN RA KỆ
    # =========================
    def move_comic_to_display(
        self,
        comic_id,
        quantity
    ):

        comic = (
            self.comic_repository
            .find_by_id(comic_id)
        )

        if comic is None:
            return "Không tìm thấy truyện."

        if comic.stock_quantity < quantity:

            return "Kho không đủ số lượng."

        self.inventory_repository.move_to_display(
            comic_id,
            quantity
        )

        self.inventory_repository.add_inventory_log(
            comic_id,
            "MOVE_TO_DISPLAY",
            quantity,
            "Chuyển truyện từ kho ra kệ"
        )

        return "Chuyển truyện ra kệ thành công."

    # =========================
    # XEM LOG
    # =========================
    def get_inventory_logs(self):

        return (
            self.inventory_repository
            .get_logs()
        )