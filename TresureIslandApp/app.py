from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].strip()
        return redirect(url_for("choose_key", name=name))
    return render_template("index.html")


@app.route("/choose_key/<name>", methods=["GET", "POST"])
def choose_key(name):
    if request.method == "POST":
        key_choice = request.form.get("choice")  # Matches "name=choice" in game.html
        if key_choice == "scarlet":
            return redirect(url_for("scarlet_key_storyline", name=name, key="scarlet"))
        elif key_choice == "emerald":
            return redirect(url_for("emerald_key_storyline", name=name, key="emerald"))
        elif key_choice == "golden":
            return render_template("game.html", message="You've been struck by lightning and died. Game Over!",
                                   choices=None, next_url=url_for("restart"))
        else:
            return render_template("game.html", message="Invalid choice. The End.", choices=["Restart Game"])
    message = (f"Hello {name}, you stumbled upon a box with three keys: Scarlet, Emerald, and Golden. Each key has "
               f"special powers.")
    choices = ["scarlet", "emerald", "golden"]  # Matches buttons in game.html
    return render_template("game.html", message=message, choices=choices)


@app.route("/scarlet_key_storyline/<name>/<key>", methods=["GET", "POST"])
def scarlet_key_storyline(name, key):
    if request.method == "POST":
        river_choice = request.form.get("choice")
        if river_choice == "swim":
            return render_template("game.html", message="You were eaten by hidden piranhas. Game Over!", choices=None,
                                   next_url=url_for("restart"))
        elif river_choice == "wait":
            message = (
                "You waited for Scarlet to return under a tree nearby. Hours passed by, and you fell asleep. "
                "You woke up at the voice of Scarlet calling your name. "
                "Scarlet says: 'Thanks for patiently waiting. Here's a scroll containing the secret code.' "
                "'I am the bravest at heart.'"
            )
            return redirect(url_for("fairyland_storyline", name=name, key=key))
    message = "You find yourself in front of a river. Do you want to wait for a boat or swim?"
    choices = ["swim", "wait"]
    return render_template("game.html", message=message, choices=choices)


@app.route("/emerald_key_storyline/<name>/<key>", methods=["GET", "POST"])
def emerald_key_storyline(name, key):
    if request.method == "POST":
        direction_choice = request.form.get("choice")
        if direction_choice == "r":
            return redirect(url_for("fairyland_storyline", name=name, key=key))
        elif direction_choice == "l":
            return render_template("game.html",
                                   message="You encounter hungry vampires who take your key and push you over a "
                                           "cliff. Game Over!",
                                   choices=None, next_url=url_for("restart"))
    message = "You come to a fork in the road. Do you go left or right?"
    choices = ["l", "r"]
    return render_template("game.html", message=message, choices=choices)


@app.route("/fairyland_storyline/<name>/<key>", methods=["GET", "POST"])
def fairyland_storyline(name, key):
    # Expected password from the scroll
    expected_password = "i am the bravest at heart"

    if request.method == "POST":
        # Get the user-entered password
        entered_password = request.form.get("password", "").strip().lower()

        if entered_password == expected_password:
            # Password matches, proceed to lion encounter
            return redirect(url_for("lion_encounter", name=name, key=key))
        else:
            # Password is wrong, end game
            return render_template("game.html", message="Wrong code. Arrows fire at you. Game Over!", choices=None,
                                   next_url=url_for("restart"))

    # Display the password prompt if it's a GET request
    message = "Welcome to Fairyland. Enter the secret code."
    return render_template("game.html", message=message, input_field="password")


@app.route("/lion_encounter/<name>/<key>", methods=["GET", "POST"])
def lion_encounter(name, key):
    if request.method == "POST":
        has_key = request.form.get("choice")
        if has_key == "y":
            if key == "scarlet":
                return render_template("game.html",
                                       message="The lion allows you to pass but you encounter a ferocious Taurus and "
                                               "die. Game Over!",
                                       choices=None, next_url=url_for("restart"))
            elif key == "emerald":
                return render_template("game.html",
                                       message="The lion guides you to the treasure. YOU WIN! Congratulations!",
                                       choices=None, next_url=url_for("restart"))
        else:
            return render_template("game.html", message="The lion eats you. Game Over!", choices=["Restart Game"])
    message = "You encountered a lion guarding the entrance to a cave. Do you have the key?"
    choices = ["y", "n"]
    return render_template("game.html", message=message, choices=choices)


@app.route("/restart", methods=["GET"])
def restart():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
