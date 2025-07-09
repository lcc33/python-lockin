# Notes App (Python + Flask)

A beautiful, minimal note-taking web app built with Flask and vanilla JavaScript.

## ✨ Features

- User signup & login with hashed passwords
- Create and delete notes
- Clean, responsive UI (mobile friendly)
- Session-based authentication
- JSON file-based storage for simplicity
- Custom 404 page

## 📂 Project Structure

```
notes-app/
├── app.py
├── data/
│   └── users.json
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── sign.html
│   ├── notes.html
│   └── 404.html
├── static/
│   └── image.png
└── README.md
```

## ⚙️ Installation & Run

```bash
git clone https://github.com/yourusername/notes-app.git
cd notes-app
pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

## 📦 Dependencies
- Flask
- Werkzeug (for password hashing)

Install with:
```bash
pip install Flask Werkzeug
```

## 🌟 Screenshots
- Landing page with call-to-action
- Signup & login forms
- Notes dashboard with create & delete

## 🚀 Deployment
You can deploy easily on:
- [Vercel + Flask](https://vercel.com/)
- [Render](https://render.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)

## 🧰 Future improvements
- Switch to database (e.g., SQLite / PostgreSQL)
- Add edit note functionality
- User profile & settings
- Improved alert system & UI polish

## 👤 Author
Made by **Kindra**

- Portfolio: [muhammadev.vercel.app](https://muhammadev.vercel.app)
- GitHub: [lcc33](https://github.com/lcc33)
- LinkedIn: [muhammad-147648327](https://www.linkedin.com/in/muhammad-147648327)

Feel free to ⭐️ star the repo if you like it!

---

📌 *Built as part of a 15-day Python + Flask challenge ✏️*
