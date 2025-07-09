from flask import Flask, session, request, render_template, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

app = Flask(__name__)
app.secret_key = "aizensosuke"

USERS_FILE = os.path.join("data", "users.json")


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return []


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/notes", methods=["GET", "POST"])
def api_notes():
    if "username" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    username = session["username"]
    users = load_users()

    if request.method == "GET":
        for user in users:
            if user["username"] == username:
                return jsonify(user.get("notes", []))
        return jsonify([])

    if request.method == "POST":
        if not request.is_json:
            return jsonify({"message": "Invalid request format"}), 400

        data = request.get_json()
        note = data.get("note", "").strip()

        if not note:
            return jsonify({"message": "Note cannot be empty"}), 400

        for user in users:
            if user["username"] == username:
                user.setdefault("notes", []).append(note)
                break

        save_users(users)
        return jsonify({"message": "Note created"}), 201


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()

        if not username or not password:
            return jsonify({"message": "Username and password required"}), 400

        users = load_users()

        if any(user["username"] == username for user in users):
            return jsonify({"message": "Username already taken"}), 409

        password_hash = generate_password_hash(password)
        users.append({"username": username, "password": password_hash, "notes": []})
        save_users(users)

        return jsonify({"message": "Signup successful"}), 200

    return render_template("sign.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()

        users = load_users()
        for user in users:
            if user["username"] == username and check_password_hash(user["password"], password):
                session["username"] = username
                return jsonify({"message": "Login successful"}), 200

        return jsonify({"message": "Invalid credentials"}), 401

    return render_template("login.html")


@app.route("/notes")
def notes():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("notes.html", user=session["username"])


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/notes/<int:note_index>", methods=["DELETE"])
def delete_note(note_index):
    if "username" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    users = load_users()
    username = session["username"]

    for user in users:
        if user["username"] == username:
            try:
                user["notes"].pop(note_index)
                save_users(users)
                return jsonify({"message": "Note deleted"})
            except IndexError:
                return jsonify({"message": "Invalid index"}), 400

    return jsonify({"message": "User not found"}), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    app.run(debug=True)
