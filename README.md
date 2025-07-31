# 📝 Flask Notes App

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![GitHub](https://img.shields.io/badge/license-MIT-green)

A lightweight note-taking web app with persistent storage using JSON.

## ✨ Features
- **CRUD Operations**: Create, Read, Update, Delete notes
- **Persistent Storage**: Auto-saves to `notes.json`
- **Simple UI**: Clean HTML templates with minimal styling
- **Timestamps**: Tracks creation/modification times

## 🛠️ Project Structure
- `flask_app.py` - Main Flask application  
- `notes.json` - JSON database (auto-created)  
- `templates/` - HTML templates  
  - `edit.html` - Edit note page  
  - `notes.html` - Main page with all notes  

## 🚀 Quick Start
# 1. Install Flask
pip install flask

# 2. Run the app
python flask_app.py

# 3. Access in browser at:
http://localhost:5000

## 🛠️ Usage Guide

### Adding a Note
1. Fill in the "Note Title" and "Note Body" fields at the top of the page
2. Click the "Add Note" button

### Editing a Note
1. Click the "Edit" button next to any note
2. Modify the title or content in the form
3. Click "Update Note" to save changes

### Deleting a Note
- Click the "Delete" button next to any note (no confirmation dialog)

📝 Notes automatically:
- Save to `notes.json` immediately
- Show newest notes first
- Display creation timestamps in `YYYY-MM-DD HH:MM:SS` format
