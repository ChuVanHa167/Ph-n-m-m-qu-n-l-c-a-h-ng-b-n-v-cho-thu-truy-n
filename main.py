from flask import Flask, render_template

from config.database import Database

from services.dashboard_service import DashboardService

from views.routes.comic_routes import comic_routes
from views.routes.customer_routes import customer_bp
from views.routes.inventory_routes import inventory_bp
from views.routes.rental_routes import rental_bp
from views.routes.sale_routes import sale_bp

app = Flask(
    __name__,
    template_folder="views/templates",
    static_folder="views/static"
)

db = Database()
db.create_tables()

app.register_blueprint(comic_routes)
app.register_blueprint(customer_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(rental_bp)
app.register_blueprint(sale_bp)


@app.route("/")
def dashboard():
    service = DashboardService()

    return render_template(
        "dashboard.html",
        total_revenue=service.get_total_revenue(),
        total_comics=service.get_total_comics(),
        total_customers=service.get_total_customers(),
        chart_labels=service.get_sales_by_month()["labels"],
        chart_values=service.get_sales_by_month()["values"],
        ratio_data=service.get_ratio_data()
    )


if __name__ == "__main__":
    app.run(debug=True)