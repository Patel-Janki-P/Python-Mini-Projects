# 🐍 Python Mini Projects

This repository contains beginner-to-intermediate level **Python mini projects**, developed to practice and demonstrate core programming concepts including functions, loops, conditionals, and OOP. These are fully functional console and GUI-based games.

---

## 📁 Projects Included

### 1. 🎲 Blackjack Game
A simple console-based blackjack game where you play against the computer (dealer). Cards are dealt randomly, and the score is calculated based on classic Blackjack rules.

- Uses: `random` module
- Features:
  - Card dealing simulation
  - Score comparison logic
  - Ace adjustment logic (11 becomes 1 if needed)
  - ASCII logo from `art.py`

---

### 2. 💀 Hangman Game
A word guessing game with ASCII graphics. Try to guess the word letter by letter before you run out of lives.

- Uses: `random` module
- External files required:
  - `hangman_words.py` (contains a list of words)
  - `hangman_art.py` (contains ASCII stages and logo)

- Features:
  - Tracks correct and incorrect guesses
  - Shows hangman stage visually
  - Displays win/loss message

---

### 3. 🐍 Snake Game (Turtle Graphics)
A graphical version of the classic Snake game built using the `turtle` module.

- Uses: `turtle`, `time`, and OOP (object-oriented programming)
- External files required:
  - `snake.py` (Snake class)
  - `food.py` (Food class)
  - `scoreBoard.py` (Scoreboard class)

- Features:
  - Arrow key controls
  - Food eating and snake growth
  - Collision detection with walls and self
  - Score tracking

> ✅ Note: Requires supporting files in the same directory.

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Patel-Janki-P/Python-Mini-Projects.git
   cd Python-Mini-Projects

2. **Run any project using Python 3:**
   ```bash
   python main.py

> You may need to install Python 3 or turtle module (pre-installed in most setups).

---
## 📌 Requirements
- Python 3.x
- No external packages required (only standard libraries)
- For snake Game, ensure your environment supports GUI rendering (like local machine or IDLE)

---
> Developed by JANKI PATEL

