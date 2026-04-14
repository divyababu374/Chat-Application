# 💬 WhatsApp-Style Chat Application (Python)

A real-time **2-person chat application** built using **Python, Socket Programming, Tkinter GUI, and SQLite Database**.
This project simulates a **WhatsApp-like interface** with chat bubbles, message history, and persistent storage.

---

## 🚀 Features

* 👥 Real-time communication between **two users**
* 💬 **WhatsApp-style UI** (chat bubbles left/right)
* 🟢 Clean **dark theme interface**
* 🕒 Message timestamps
* 📜 Scrollable chat window
* 💾 **SQLite database integration**
* 🔁 Chat history loads automatically on restart
* ⚡ Lightweight and runs locally

---

## 🛠️ Technologies Used

* **Python**
* **Socket Programming**
* **Tkinter (GUI)**
* **SQLite (Database)**

---

## 📁 Project Structure

```
chat_app/
 ├── server.py        # Handles connections and message routing
 ├── client.py        # GUI chat application
 └── database.py      # Database operations (SQLite)
```

---

## ▶️ How to Run

### 1️⃣ Start the Server

```bash
python server.py
```

---

### 2️⃣ Run Two Clients (IMPORTANT)

Open **two separate terminals**:

```bash
python client.py
```

* Terminal 1 → Enter name (e.g., Divya)
* Terminal 2 → Enter name (e.g., Friend)

---

## 🎯 Output

* Messages sent by one user appear instantly on the other side
* Chat bubbles aligned left/right (WhatsApp style)
* Messages are stored in `chat.db`
* Old chats reload automatically when app restarts

---

## 🗄️ Database

* Database file: `chat.db`
* Automatically created when server runs
* Stores:

  * Sender name
  * Message content

---

## ⚠️ Important Notes

* Only supports **2 users at a time**
* Server must be running before starting clients
* Both clients should be opened simultaneously
* Runs on local system (`127.0.0.1`)

---

## 📌 Future Improvements

* Multi-user chat support
* User authentication (login/signup)
* Profile pictures
* File/image sharing
* Online/offline status
* Web-based version (React + Flask)

---

## 👩‍💻 Author

Developed by **Divya**
B.Sc Computer Science 

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
 
