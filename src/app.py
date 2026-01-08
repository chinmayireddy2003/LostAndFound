from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key_for_session"

# ---------------- DATABASE CONNECTION ----------------
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_connection():
    db_path = os.path.join(BASE_DIR, "database", "lost_found.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- HOME / LOGIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password ❌")

    return render_template("login.html")

# ---------------- REGISTER PAGE ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
                (name, email, password, "user")
            )
            conn.commit()
            flash("Registration successful 🎉 Please login.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Email already exists ❌")
        finally:
            conn.close()

    return render_template("register.html")

# ---------------- DASHBOARD (MAIN PAGE) ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------------- LOST ITEM PAGE ----------------
@app.route("/lost-item", methods=["GET", "POST"])
def lost_item():
    if request.method == "POST":
        item_name = request.form.get("item_name")
        description = request.form.get("description")
        location = request.form.get("location")
        lost_date = request.form.get("lost_date")
        email = request.form.get("email")
        phone = request.form.get("phone")  # ✅ SAFE access

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO lost_items
            (item_name, description, location, lost_date, user_email, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (item_name, description, location, lost_date, email, phone))

        conn.commit()
        conn.close()

        flash("Lost item reported successfully ✅")
        return redirect(url_for("dashboard"))

    return render_template("lost_item.html")


# ---------------- VIEW LOST ITEMS ----------------
@app.route("/lost-items")
def view_lost_items():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lost_items")
    items = cursor.fetchall()
    conn.close()

    return render_template("view_lost_items.html", items=items)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    flash("Logged out successfully 👋")
    return redirect(url_for("login"))

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
