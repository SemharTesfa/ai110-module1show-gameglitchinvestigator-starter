# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, the Streamlit interface opened and allowed me to select a difficulty and enter guesses. However, the hints were backwards: when my guess was higher than the secret number, the game told me to go higher instead of lower. Easy mode could generate a secret number outside its stated range, and the instruction message always displayed “Guess a number between 1 and 100,” regardless of the selected difficulty. Finally, clicking New Game did not fully reset the previous score, status, attempts, or history.

### Bug Reproduction Log

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Secret = 25, guess = 56 | Display “Too High” and “Go LOWER!” | Displayed “Too High” but said “Go HIGHER!” | None |
| Difficulty = Easy (1–20), then click New Game | Generate a secret number between 1 and 20 | Generated secret = 56, which was outside the selected range | None |
| Select Easy difficulty | Display “Guess a number between 1 and 20” | Displayed “Guess a number between 1 and 100” | None |
| Finish a game, then click New Game | Reset the old game and allow a new game to begin | Previous game information remained, and the new game did not properly start | None |

---

## 2. How did you use AI as a teammate?

I used ChatGPT to identify and explain the bugs, and I used Claude in VS Code to edit the project files. One correct suggestion was to move `check_guess()` from `app.py` into `logic_utils.py` and correct the backward high and low hints; I verified this by running pytest and playing the game manually. Claude initially suggested resetting the attempt counter to 1, but I changed it to 0 because no guess had been submitted at the beginning of a new game. I reviewed the AI-generated changes and verified my version by confirming that New Game reset the game with the full number of attempts available.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after checking it with both automated tests and the live Streamlit application. I ran four pytest tests covering a high guess, a low guess, a winning guess, and a numeric string secret. All four passed. I manually changed between Easy, Normal, and Hard and confirmed that the displayed guessing range matched the selected difficulty. I also verified that the hints pointed in the correct direction and that New Game reset the secret, attempts, score, status, and history.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script from top to bottom whenever the user interacts with a button, input, or another widget. Normal variables can therefore be recreated or lost during each rerun. `st.session_state` keeps important information, such as the secret number, score, attempts, game status, and history, available between reruns. To properly start a new game, every related session-state value must be reset.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing a small automated test for each bug instead of relying only on manual testing. I also want to review every AI-generated diff and test the changes before accepting them. Next time, I will give the AI more focused prompts that clearly state which files and functions it may change. This project taught me that AI-generated code can be helpful, but it still requires human review because code can run without crashing while producing incorrect behavior.