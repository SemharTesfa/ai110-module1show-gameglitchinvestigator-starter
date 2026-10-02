# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The purpose of this project was to debug an AI-generated number-guessing game. I found backward hints, incomplete New Game behavior, incorrect difficulty-range handling, and a hardcoded range message. I corrected these problems, moved `check_guess()` into `logic_utils.py`, and added pytest coverage. I used ChatGPT to understand the problems and Claude in VS Code to apply code changes, but I reviewed and tested every suggestion before accepting it.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user selects Normal difficulty, which displays a range of 1 to 100.
2. With a secret number of 50, the user enters 40.
3. The game returns "Too Low" and correctly tells the user to go higher.
4. The user enters 70, and the game returns "Too High" and tells the user to go lower.
5. The user enters 50, and the game displays the winning message and final score.
6. The user clicks New Game, and the secret, attempts, score, status, and history reset.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```text
collected 4 items

tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_check_guess_handles_string_secret PASSED

4 passed in 0.16s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
