from repositories.sale_repository import SaleRepository
from repositories.comic_repository import ComicRepository
from repositories.customer_repository import CustomerRepository


class DashboardService:

    def __init__(self):
        self.sale_repo = SaleRepository()
        self.comic_repo = ComicRepository()
        self.customer_repo = CustomerRepository()

    def get_total_revenue(self):
        return self.sale_repo.get_total_revenue()

    def get_total_comics(self):
        return len(self.comic_repo.get_all())

    def get_total_customers(self):
        return len(self.customer_repo.get_all())

    def get_sales_by_month(self):
        data = self.sale_repo.get_monthly_revenue()

        labels = [d["month"] for d in data]
        values = [d["revenue"] for d in data]

        return {
            "labels": labels,
            "values": values
        }

    def get_ratio_data(self):
        comics = len(self.comic_repo.get_all())
        customers = len(self.customer_repo.get_all())
        revenue = self.sale_repo.get_total_revenue()

        return {
            "comics": comics,
            "customers": customers,
            "revenue": revenue
        }