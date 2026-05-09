from services.inventory_service import (
    InventoryService
)


class InventoryController:

    def __init__(self, view):

        self.view = view

        self.inventory_service = (
            InventoryService()
        )

    # =========================
    # IMPORT
    # =========================
    def import_stock(self):

        comic_id, quantity = (
            self.view.input_inventory()
        )

        result = (
            self.inventory_service
            .import_comic_stock(
                comic_id,
                quantity
            )
        )

        self.view.show_message(result)

    # =========================
    # EXPORT
    # =========================
    def export_stock(self):

        comic_id, quantity = (
            self.view.input_inventory()
        )

        result = (
            self.inventory_service
            .export_comic_stock(
                comic_id,
                quantity
            )
        )

        self.view.show_message(result)

    # =========================
    # MOVE DISPLAY
    # =========================
    def move_to_display(self):

        comic_id, quantity = (
            self.view.input_inventory()
        )

        result = (
            self.inventory_service
            .move_comic_to_display(
                comic_id,
                quantity
            )
        )

        self.view.show_message(result)

    # =========================
    # VIEW LOGS
    # =========================
    def show_logs(self):

        logs = (
            self.inventory_service
            .get_inventory_logs()
        )

        self.view.display_logs(logs)