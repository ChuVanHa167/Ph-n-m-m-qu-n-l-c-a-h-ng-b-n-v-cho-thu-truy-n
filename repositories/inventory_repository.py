from config.database import (
    ThreadSafeDatabase
)


class InventoryRepository:

    def __init__(self):

        # self.db = Database()
        self.connection = (
            ThreadSafeDatabase
            .get_thread_connection()
        )

        self.cursor = (
            ThreadSafeDatabase
            .get_thread_cursor()
        )

    # =========================
    # NHẬP KHO
    # =========================
    def import_stock(
        self,
        comic_id,
        quantity
    ):

        query = """
            UPDATE comics
            SET stock_quantity =
                stock_quantity + ?
            WHERE comic_id = ?
        """

        self.cursor.execute(
            query,
            (quantity, comic_id)
        )

        self.connection.commit()

    # =========================
    # XUẤT KHO
    # =========================
    def export_stock(
        self,
        comic_id,
        quantity
    ):

        query = """
            UPDATE comics
            SET stock_quantity =
                stock_quantity - ?
            WHERE comic_id = ?
        """

        self.cursor.execute(
            query,
            (quantity, comic_id)
        )

        self.connection.commit()

    # =========================
    # CHUYỂN TỪ KHO RA KỆ
    # =========================
    def move_to_display(
        self,
        comic_id,
        quantity
    ):

        query = """
            UPDATE comics
            SET
                stock_quantity =
                    stock_quantity - ?,

                quantity =
                    quantity + ?

            WHERE comic_id = ?
        """

        self.cursor.execute(
            query,
            (
                quantity,
                quantity,
                comic_id
            )
        )

        self.connection.commit()

    # =========================
    # LOG KHO
    # =========================
    def add_inventory_log(
        self,
        comic_id,
        action_type,
        quantity,
        note
    ):

        query = """
            INSERT INTO inventory_logs (
                comic_id,
                action_type,
                quantity,
                note
            )
            VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(
            query,
            (
                comic_id,
                action_type,
                quantity,
                note
            )
        )

        self.connection.commit()

    # =========================
    # XEM LOG
    # =========================
    def get_logs(self):

        query = """
            SELECT * FROM inventory_logs
            ORDER BY created_at DESC
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()