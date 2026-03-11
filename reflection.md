# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---1. The hints were wrong; when it needs to display "GO HIGHER" as a hint "Go LOWER" was displayed and vice-versa. 2. When the game was opened for first time, it displays that one guess was already attempted when the user hasn't input anything yet. 3. Scoring is kind of wierd. 4. When the difficulty was changed to hard the range change to 1-50, which isn't hard compared to normal game, which has range 1-100. Also, even when the range is changed to easy or hard, secret number in the range 1-100 is generated which didn't match the range for the difficulty level. And the game always displays "Guess a number between 1 and 100" for every level.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used Copilot and Claude to fix the bug.
The correct AI suggestion I received was when I asked to fix the hint bug; it show me the line of code where the bug was located and what was wrong in the logic. I prompt it to correct the logic and save the changes. To verify, I submit my gusses to check whether the bug was fixed or not.

I prompted the Claude to change the secret number and reset the game based on the level of difficulty chosen by the player, the claude not only does that but also change the numbers of attempts allowed in different difficulty level to match the level selected by the player which confused me at firt; the number of attempts allowed for easy level is 6, normal is 8, and haed is 5 with varying number ranges for each level of difficulty.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I ran the code and played the game myself to check whether the bugs were fixed or not; I checked manually whether the secret numbers generated for each level of difficulty match the difficulty level chosen by the player. Beside that I prompted Claude to make me test cases in the test_game_logic.py to check the hint logic and run the test through pytest command in terminal.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
