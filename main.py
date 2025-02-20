from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app)

# Skins available for rotation
skins = {
    "Scout": {
        "Red": {
            "Cost": 250,
            "Name": "Red",
            "Tower": "Scout",
        },
        "Pink": {
            "Cost": 500,
            "Name": "Pink",
            "Tower": "Scout",
        },
        "Black": {
            "Cost": 500,
            "Name": "Black",
            "Tower": "Scout",
        },
        "Cowboy": {
            "Cost": 1000,
            "Name": "Cowboy",
            "Tower": "Scout",
        },
        #"Miku": {
        #    "Cost": 0,
        #    "Name": "Miku",
        #    "Tower": "Scout",
        #}
    },
    "Employee": {
        "Farm": {
            "Cost": 1000,
            "Name": "Farm",
            "Tower": "Employee",
        }
    }
}

# Stores the current daily shop
current_shop = {}
last_update = None  # Stores last update date


def update_shop():
    """Rotates skins daily and prints a message when updated."""
    global current_shop, last_update
    today = datetime.date.today()

    if last_update != today:  # Only update once per day
        # Flatten all skins into a single list
        all_skins = [
            skin for tower in skins.values() for skin in tower.values()
        ]

        # Ensure there are at least 3 skins
        if len(all_skins) >= 3:
            current_shop = random.sample(all_skins,
                                         3)  # Randomly select exactly 3 skins
        else:
            current_shop = all_skins  # If less than 3, return all

        last_update = today
        print(f"Shop updated! New skins: {current_shop}")


# Update the shop at startup
update_shop()


@app.route('/shop', methods=['GET'])
def shop():
    """Returns the current daily shop."""
    update_shop()  # Ensure shop is always up to date
    return jsonify(current_shop)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
