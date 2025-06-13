# ✊✋✌️ Rock-Paper-Scissors – Python Edition

This is a simple **Rock-Paper-Scissors game** written in Python that allows a human player to play against the computer via the console.

## 🎮 How It Works

1. The computer randomly selects a number from **1 to 3**:
   - 1 = Rock ✊  
   - 2 = Paper ✋  
   - 3 = Scissors ✌️

2. The user is prompted to enter a number between 1 and 3 to make their choice.

3. The result is then calculated based on classic game rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choice = Repeat round

## 🧠 Game Logic

- Input is validated (must be 1, 2, or 3)
- Winner is determined using `if-elif` statements
- Computer's choice is displayed after each round

## 🚀 How to Run

Make sure Python is installed, then run:

```bash
python rock_paper_scissors.py
```

Follow the prompt and enter your move!

## 🛠 Future Ideas

- Loop the game until user quits  
- Add score tracking  
- Use strings/emojis instead of numbers  
- Add a GUI with Tkinter or PyGame  
