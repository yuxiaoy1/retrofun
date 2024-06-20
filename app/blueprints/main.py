from flask import Blueprint, render_template, request

from app.extensions import db
from app.models import Order

main = Blueprint("main", __name__)


@main.get("/")
def index():
    return render_template("index.html")


@main.get("/api/orders")
def get_orders():
    start = request.args.get("start")
    length = request.args.get("length")
    sort = request.args.get("sort")
    search = request.args.get("search")

    total = db.session.scalar(Order.total_orders(search))
    orders = db.session.execute(Order.paginated_orders(start, length, sort, search))

    data = [{**order[0].to_dict(), "total": order[1]} for order in orders]

    return {"data": data, "total": total}
