from services.comic_service import ComicService
from services.rental_service import RentalService


class ComicController:

    def __init__(self, view=None):

        self.view = view
        self.comic_service = ComicService()
        self.rental_service = RentalService()

    # CREATE
    def add_comic(self):

        data = self.view.input_comic()
        self.comic_service.add_comic(*data)

        self.view.show_message("Thêm truyện thành công.")

    # READ
    def show_comics(self):

        comics = self.comic_service.get_all_comics()
        self.view.display_comics(comics)

    # UPDATE
    def update_comic(self):

        data = self.view.input_comic()

        if not data[0]:
            self.view.show_message("Chọn truyện cần sửa!")
            return

        self.comic_service.update_comic(*data)
        self.view.show_message("Cập nhật thành công.")

    # DELETE
    def delete_comic(self):

        comic_id = self.view.input_delete_id()

        if not comic_id:
            self.view.show_message("Chọn truyện cần xóa!")
            return

        self.comic_service.delete_comic(comic_id)
        self.view.show_message("Xóa thành công.")

    # SEARCH
    def search_comic(self):

        keyword = self.view.input_search_keyword()
        comics = self.comic_service.search_comic(keyword)

        self.view.display_comics(comics)