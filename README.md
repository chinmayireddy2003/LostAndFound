📦 Lost & Found Management System

A full-stack web application built using Python (Flask) and SQLite that allows users to report and track lost items. The system includes user authentication, an interactive dashboard, and a clean, modern UI.

🚀 Features

User Registration and Login

Secure session handling

Report lost items with details and contact information

View all reported lost items

Responsive and attractive UI using HTML & CSS

SQLite database for persistent storage

Clean project structure suitable for real-world applications

🛠️ Tech Stack

Backend: Python, Flask

Database: SQLite

Frontend: HTML, CSS

Tools: VS Code, Git, GitHub

📂 Project Structure
lost_and_found_project/
│
├── src/
│   ├── app.py
│   ├── create_tables.py
│
├── database/
│   └── lost_found.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── lost_item.html
│   └── view_lost_items.html
│
├── static/
│   └── style.css
│
├── README.md
└── .gitignore

⚙️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/lost-and-found-flask.git
cd lost-and-found-flask

2️⃣ Install dependencies
pip install flask

3️⃣ Create database tables
python src/create_tables.py

4️⃣ Run the application
python src/app.py

5️⃣ Open in browser
http://127.0.0.1:5000

🧪 Sample Use Case

Register a new user

Log in to the dashboard

Report a lost item

View lost items submitted by users

📌 Future Enhancements

Auto-fill user details from session

Search and filter lost items

Admin panel for managing reports

Password hashing and validation

Email notifications

👤 Author

Chinmayi Reddy
Python & Data Analytics Enthusiast

⭐ GitHub Tip

If you like this project, don’t forget to ⭐ the repository!
