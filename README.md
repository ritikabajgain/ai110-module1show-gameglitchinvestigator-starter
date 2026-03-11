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
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.
      The game's purpose is to allow players to guess the secret number multiple times based on the difficulty level selected by the user; it has a funtion to show the hint whether the secret number is higher or lower.
      One of the bug I found was the hint bug. The game shows reversed hint for every number guessed by the player. Another bug was the game displayed the wrong number of attempts left or when the game was reset, the number of attempts and the score remain unchanged. One more bug was when the difficulty level was changed, the range for numbers changed but the secret number doesn't changed accordingly.
      I used Claude and Copilot to fix the bugs mentioned above by giving prompt to suggest me the best changes possible to fix the bug by exactly describing how the bug looks like and keeping the changes in the code suggested by the AI agents.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
      (image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
