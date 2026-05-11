from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.customer_service import CustomerService

customer_bp = Blueprint(
    "customer",
    __name__
)

customer_service = CustomerService()


# =========================
# PAGE
# =========================
@customer_bp.route("/customers")
def customers():

    keyword = request.args.get(
        "keyword",
        ""
    )

    if keyword:

        customers = (
            customer_service.search_customer(
                keyword
            )
        )

    else:

        customers = (
            customer_service.get_all_customers()
        )

    return render_template(
        "customers.html",
        customers=customers
    )


# =========================
# AUTO ID
# =========================
def generate_customer_id():

    customers = (
        customer_service.get_all_customers()
    )

    max_id = 0

    for customer in customers:

        try:

            number = int(
                str(customer.customer_id)
                .replace("KH", "")
            )

            if number > max_id:
                max_id = number

        except:
            pass

    return f"KH{max_id + 1}"


# =========================
# ADD
# =========================
@customer_bp.route(
    "/customers/add",
    methods=["POST"]
)
def add_customer():

    customer_id = generate_customer_id()

    customer_service.add_customer(
        customer_id,
        request.form["name"],
        request.form["phone"],
        request.form["email"],
        request.form["address"]
    )

    return redirect(
        url_for("customer.customers")
    )


# =========================
# UPDATE
# =========================
@customer_bp.route(
    "/customers/update",
    methods=["POST"]
)
def update_customer():

    customer_service.update_customer(
        request.form["customer_id"],
        request.form["name"],
        request.form["phone"],
        request.form["email"],
        request.form["address"]
    )

    return redirect(
        url_for("customer.customers")
    )


# =========================
# DELETE
# =========================
@customer_bp.route(
    "/customers/delete/<customer_id>"
)
def delete_customer(customer_id):

    customer_service.delete_customer(
        customer_id
    )

    return redirect(
        url_for("customer.customers")
    )