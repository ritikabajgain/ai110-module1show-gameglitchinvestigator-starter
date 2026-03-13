# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- When I first ran the game, the interface looked playable, but several behaviors were clearly broken. The hint direction was reversed, so it showed "Go LOWER" when it should have shown "Go HIGHER," and vice versa. The attempts-left display was also off by one at the start of a game. I also noticed that changing difficulty did not fully reset the game state, and the "Guess a number" instruction still showed the normal range instead of updating per difficulty.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used Claude Opus 4.6 as my main AI teammate in this project. One correct suggestion was to fix the hint logic by correcting the guess comparison, and I verified it by entering test guesses above and below the secret number and checking that the hint direction matched. One misleading suggestion was that, while fixing logic issues, it also changed parts of my UI layout that I did not ask to change, such as control positions and where instruction text appeared. I verified that by comparing the app before and after the edits and noticing that the New Game and Show hint controls were arranged differently and the "Guess a number between ..." instruction moved on the page.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I confirmed the fixes by running the app and playing the game myself multiple times. During manual testing, I checked whether each difficulty level generated a secret number within its correct range, which helped me verify that difficulty settings were working as expected. I also asked Claude to help create test cases in test_game_logic.py for the hint logic, then ran them using pytest in the terminal. Using both manual checks and automated tests, I was more confident that the bugs were actually fixed.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Every time we interact with a Streamlit app — like clicking a button or typing something — the entire Python script runs again from the top. This is called a "rerun." The problem is that any regular variable we set gets wiped out on each rerun, so things like the secret number or the attempt count would reset on every click. That is where session state comes in: it is basically a small storage space that remembers values across reruns so they do not disappear. Once I stored the secret number in session state, it stayed the same for the whole game instead of changing every time the player clicked "Submit."

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- One habit I want to keep is improving my prompting strategy: before applying any code changes, I will first ask for multiple possible fixes and compare the options. Next time, I will be more deliberate about reviewing each AI suggestion line by line before accepting it, especially when a change might affect game flow or UI behavior. This project changed how I view AI-generated code because I now see it as a strong assistant, but not something I should trust blindly. AI can speed up debugging and testing, but I still need to verify logic, run tests, and make the final decisions as the developer.
