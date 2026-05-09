class ComicView:

    # =========================
    # INPUT CREATE / UPDATE
    # =========================
    def input_comic(self):

        comic_id = input("ID: ")
        title = input("Tên truyện: ")
        author = input("Tác giả: ")
        genre = input("Thể loại: ")

        price = float(input("Giá bán: "))
        rental_price = float(input("Giá thuê: "))

        quantity = int(
            input("Số lượng trưng bày: ")
        )

        stock_quantity = int(
            input("Số lượng trong kho: ")
        )

        return (
            comic_id,
            title,
            author,
            genre,
            price,
            rental_price,
            quantity,
            stock_quantity
        )

    # =========================
    # DISPLAY
    # =========================
    def display_comics(self, comics):

        if not comics:
            print("Không có truyện.")
            return

        for comic in comics:
            print(comic)
            print("-" * 40)

    # =========================
    # DELETE
    # =========================
    def input_delete_id(self):
        return input("Nhập ID cần xóa: ")

    # =========================
    # SEARCH
    # =========================
    def input_search_keyword(self):
        return input("Nhập tên truyện: ")

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, message):
        print(message)