# 📝 Flask Notes App

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![GitHub](https://img.shields.io/badge/license-MIT-green)

A lightweight note-taking web app with persistent storage using JSON.

![Screenshot Preview](https://via.placeholder.com/800x400?text=Flask+Notes+App+Screenshot) *(Replace with actual screenshot)*

## ✨ Features
- **CRUD Operations**: Create, Read, Update, Delete notes
- **Persistent Storage**: Auto-saves to `notes.json`
- **Simple UI**: Clean HTML templates with minimal styling
- **Timestamps**: Tracks creation/modification times

## 🛠️ Project Structure
flask-notes-app/
├── flask_app.py # Main application logic
├── notes.json # Database (auto-generated)
├── templates/
│ ├── edit.html # Note editing interface
│ └── notes.html # Main interface with all notes

## 🚀 Quick Start
1. **Install dependencies**:
   ```bash
   pip install flask
2. Run the app:
  python flask_app.py
3. Access in browser:
  http://localhost:5000

🔧 Usage Guide
Action	How To
Add Note	Fill form at top of main page
Edit Note	Click "Edit" → Modify → Update
Delete Note	Click "Delete" button
