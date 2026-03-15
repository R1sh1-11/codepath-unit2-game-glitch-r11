# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game had a title and there was a input box to enter my guess. I clicked on the input box and started typing a random number. The game would then process my request and tell me if my answer needed to be lower or higher based on the hints it gave me.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The hints kept saying go lower even when the number was 1, and the beginning of the guessing game started with guessing from numbers 1-100. Another one, is that the secret number in fact did keep changing. It should be one number the whole time because guessing the number otherwise would make it dynamic and not static. Hard mode had a range of 1-50 which was actually easier than Normal  mode's 1-100. I expected Hard mode to be harder with a larger range.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude to work on this project. I used Gemini to explain some instances. I primarly used Claude for its coding abilitiy and used Gemini to get deeper explainations if I was stuck.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of an AI suggestion that was correct was that it told me to change the code in the difficulty section. For instance, if the difficulty was set to high then the range should be greater than 100. However, the range returned was 1-50 and not something much higher to lower the odds of a correct guess. I verified the result by checking what difficulty the game had in the developer debug info portal and what numbers it showed to guess.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Copilot generated pytest tests that used `result == "Win"` to check the outcome 
of check_guess. This was incorrect because check_guess returns a tuple like 
("Win", "🎉 Correct!"), not just a string. The tests would have failed if I ran 
them as-is. I caught this by understanding what check_guess actually returns and 
fixed it to use `result[0] == "Win"` instead.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when both the automated tests passed AND the live game 
behaved correctly. For the hints bug, I ran pytest and all 5 tests passed. I also 
ran streamlit run app.py and manually tested guesses to confirm the hints were 
showing the right direction.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran pytest in the terminal from the project root and got 5 tests passing. 
This showed me that check_guess correctly returns "Too High" when the guess 
is above the secret, "Too Low" when below, and "Win" when they match. It also 
confirmed that Hard mode has a higher range than Normal mode after my fix.
- Did AI help you design or understand any tests? How?
Copilot helped me generate the initial structure of the tests, suggesting 
what inputs and expected outputs to use. However it made a mistake by checking 
`result == "Win"` instead of `result[0] == "Win"`, not knowing that check_guess 
returns a tuple. I had to correct this myself before the tests would pass.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because every time you clicked Submit, 
Streamlit reran the entire script from top to bottom, which called 
random.randint again and generated a brand new number each time.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are like refreshing a webpage every time you click 
anything — everything resets and starts over. Session state is like a 
sticky note that survives the refresh, so important information like 
the secret number gets remembered between clicks.
- What change did you make that finally gave the game a stable secret number?
I wrapped the secret number in `if "secret" not in st.session_state` 
so it only generates once at the very start of the game. After that, 
Streamlit reads it from session state instead of regenerating it, 
keeping it stable for the whole game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
One habit I want to reuse is adding FIXME comments to mark exactly where 
a bug is before trying to fix it. It kept me focused on one problem at a 
time and gave me a clear reference point when prompting Copilot.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time I would test AI output immediately instead of assuming it is 
correct. Copilot gave me tests that looked right but would have failed 
because it did not account for the tuple return type in check_guess.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed how I think about AI generated code because I realized 
it can look completely correct on the surface but still have subtle logic 
bugs that only show up when you actually run it. You always need to verify 
it yourself.
