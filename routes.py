from flask import Blueprint, render_template, request
from math_ops import operations

calculator_bp = Blueprint("calculator", __name__)

@calculator_bp.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            op_key = request.form["operation"]

            if op_key in operations:
                result = operations[op_key]["func"](a, b)
            else:
                result = "Invalid operation."
        except ValueError:
            result = "Please enter valid numbers."

    return render_template("index.html", result=result, ops=operations)
