from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to ExpenseFlow Platform!"


@app.route("/about")
def about():
    return jsonify({
        "developer": "Anurag Garg",
        "project": "ExpenseFlow Platform",
        "purpose": "Learning Backend, DevOps and Cloud",
        "status": "Development",
        "goal": "Become a DevOps Engineer",
        "learning": "Flask Backend Development"
    })


@app.route("/contact")
def contact():
    return "Contact: backend-team@expenseflow.local"


expenses = {
    1: {
        "expense_id": 1,
        "amount": 500,
        "category": "Food",
        "description": "Pizza with friends",
        "payment_method": "UPI",
        "expense_type": "Personal",
        "priority": "Need",
        "status": "Paid"
    },
    2: {
        "expense_id": 2,
        "amount": 1500,
        "category": "Shopping",
        "description": "Shopping with brother",
        "payment_method": "UPI",
        "expense_type": "Personal",
        "priority": "Want",
        "status": "Paid"
    },
    3: {
        "expense_id": 3,
        "amount": 700,
        "category": "Travel",
        "description": "Travel from Bhopal to Indore",
        "payment_method": "Cash",
        "expense_type": "Personal",
        "priority": "Need",
        "status": "Paid"
    }
}


@app.route("/expense/<int:expense_id>")
def expense(expense_id):

    expense_data = expenses.get(expense_id)

    if expense_data is None:
        return jsonify({"error": "Expense not found"}), 404

    return jsonify(expense_data)


@app.route("/expenses")
def all_expenses():

    return jsonify(list(expenses.values()))


if __name__ == "__main__":
    app.run(debug=True)