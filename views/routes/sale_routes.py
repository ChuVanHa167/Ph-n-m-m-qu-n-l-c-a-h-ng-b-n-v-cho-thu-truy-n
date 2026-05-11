from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.sale_service import (
    SaleService
)

sale_bp = Blueprint(
    "sale",
    __name__
)

sale_service = SaleService()


# =========================
# PAGE
# =========================
@sale_bp.route("/sales")
def sales():

    sales_data = (
        sale_service.get_all_sales()
    )

    revenue = (
        sale_service.get_total_revenue()
    )

    return render_template(
        "sales.html",
        sales=sales_data,
        revenue=revenue
    )


# =========================
# SELL
# =========================
@sale_bp.route(
    "/sales/add",
    methods=["POST"]
)
def add_sale():

    sale_service.sell_comic(
        request.form["customer_id"],
        request.form["comic_id"],
        int(request.form["quantity"])
    )

    return redirect(
        url_for("sale.sales")
    )