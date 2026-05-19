# Python Notes App (CLI)

A simple **command-line note-taking application** built with Python.

Users can add, view, delete individual notes, or clear all notes.
All notes are stored in a local `notes.txt` file with timestamps.

---

## Features

- Add notes with timestamp
- View all saved notes
- Delete a specific note
- Delete all notes
- File-based storage (`notes.txt`)

---

## How to Run

Make sure you have Python installed on your system.

Then run the project using:

```bash
python main.py
```

---

## Menu Options

When the program starts, you will see:

```
1- Add note
2- Show notes
3- Delete note
4- Delete all notes
5- Exit
```

---

## Note Format

Notes are saved in `notes.txt` in this format:

```
[19/05/2026 22:15] start python
```

- The part in brackets is the date and time  
- The rest is the actual note content  

---

## How It Works

- When adding a note, the current date and time are generated using `datetime`
- Notes are appended to `notes.txt`
- The file is read line by line when deleting a specific note
- Matching notes are removed safely

---

## Project Structure

```
project/
│
├── main.py
├── notes.txt
└── README.md
```

---

## About This Project

This project is built for learning purposes and helps understand:

- File handling in Python
- Loops and conditionals
- Basic CLI application structure

---

## License

This project does not include a license.
All rights reserved by the author.