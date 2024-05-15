from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item, quantity in order_ingredients.items():
        if quantity > resources[item]:
            return False, f"Sorry there is not enough {item}."
    return True, ""

def process_coins(drink_cost):
    """Returns the total calculated from coins inserted."""
    quarters = int(request.form.get('quarters', 0))
    dimes = int(request.form.get('dimes', 0))
    nickles = int(request.form.get('nickles', 0))
    pennies = int(request.form.get('pennies', 0))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total >= drink_cost:
        change = round(total - drink_cost, 2)
        message = f"Here is ${change} in change."
        global profit
        profit += drink_cost
        return True, message
    else:
        return False, "Sorry that's not enough money. Money refunded."

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item, quantity in order_ingredients.items():
        resources[item] -= quantity
    return f"Here is your {drink_name} ☕️. Enjoy!"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', resources=resources, profit=profit)

@app.route('/order', methods=['POST'])
def order():
    drink_name = request.form['drink']
    drink = MENU[drink_name]

    sufficient, message = is_resource_sufficient(drink["ingredients"])
    if not sufficient:
        return jsonify({'status': 'error', 'message': message})

    transaction_successful, message = process_coins(drink["cost"])
    if not transaction_successful:
        return jsonify({'status': 'error', 'message': message})

    coffee_message = make_coffee(drink_name, drink["ingredients"])
    return jsonify({'status': 'success', 'message': coffee_message})

if __name__ == '__main__':
    app.run(debug=True)