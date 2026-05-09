class InventoryView:

    # =========================
    # INPUT
    # =========================
    def input_inventory(self):

        comic_id = input("ID truyện: ")

        quantity = int(
            input("Số lượng: ")
        )

        return comic_id, quantity

    # =========================
    # DISPLAY LOGS
    # =========================
    def display_logs(self, logs):

        if not logs:

            print("Không có log kho.")

            return

        for log in logs:

            print("\n==========")

            print(f"Log ID: {log['log_id']}")

            print(
                f"Comic ID: "
                f"{log['comic_id']}"
            )

            print(
                f"Hành động: "
                f"{log['action_type']}"
            )

            print(
                f"Số lượng: "
                f"{log['quantity']}"
            )

            print(
                f"Ghi chú: "
                f"{log['note']}"
            )

            print(
                f"Ngày: "
                f"{log['created_at']}"
            )

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, message):

        print(message)