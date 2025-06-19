from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
import json
import os

app = Flask("Notes App")

NOTES_FILE = 'notes.json'

def load_notes():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            json.dump([], f)
    with open(NOTES_FILE, 'r') as f:
        return json.load(f)

def save_notes(data):
    with open(NOTES_FILE, 'w') as f:
        json.dump(data, f, indent = 4, default=str)

@app.route('/')
def notes():
    data = load_notes()
    for note in data:
        note['timestamp'] = datetime.fromisoformat(note['timestamp'])
    return render_template("notes.html", notes=data)

@app.route('/add', methods = ['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        data = load_notes()
        note = {
            'note_id': len(data) + 1,
            'title': request.form['title'],
            'body': request.form['body'],
            'timestamp': datetime.now().isoformat()
        }
        data.append(note)
        save_notes(data)

        return redirect(url_for('notes'))

    return render_template("notes.html")

@app.route('/edit/<int:note_id>', methods = ['GET', 'POST'])
def edit_note(note_id):
    data = load_notes()
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        timestamp = request.form['timestamp']

        for note in data:
            if note['note_id'] == note_id:
                note['title'] = title
                note['body'] = body
                note['timestamp'] = datetime.now().isoformat()
                break

        save_notes(data)
        return redirect(url_for('notes'))

    for note in data:
        if note['note_id'] == note_id:
            return render_template("edit.html", note = note)

    return {"message": "Note not found"}, 404

@app.route('/delete/<int:note_id>', methods = ['POST'])
def delete_note(note_id):
    data = load_notes()
    for note in data:
        if note['note_id'] == note_id:
            data.remove(note)
            save_notes(data)
            return redirect(url_for('notes'))

    return {"message": "Note not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)