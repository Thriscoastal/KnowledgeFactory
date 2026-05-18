# Day 1 of Python: What I Learned Today

Just making this file to keep track of all the new stuff I learned on my first day of Python. There's a lot to remember, but it's starting to make sense!

## 1. Variables & Data Types
* **Variables:** The tutorial said to think of these as boxes with labels where you store data. You just use `=` to put something in the box.
* **Data Types I learned:**
    * `int`: Regular whole numbers (like `85` or `-10`).
    * `float`: Numbers with decimals (like `92.5` or `3.14`).
    * `str`: "Strings". This is just text, but you have to put it in quotes like `"Hello"`.
    * `bool`: Booleans. Just `True` or `False`. (Make sure to capitalize the first letter!)
    * `list`: A list of things in order using brackets. Example: `[90, 85, 95]`.
    * `dict`: Dictionaries. These have a "key" and a "value", kind of like looking up a word in a real dictionary. Example: `{"name": "Alice", "score": 90}`.

## 2. If Statements (Conditions)
This is how you make the code choose what to do. 
* `if`: Do this thing if it's true.
* `elif`: (Short for "else if"). If the first thing wasn't true, try checking this instead.
* `else`: If absolutely nothing else was true, just do this.

## 3. Loops
Loops are awesome because you don't have to copy and paste the same code a hundred times.
* **`for` loop:** Use this when you know how many times to loop (like going through every item in a list).
* **`while` loop:** This keeps repeating *until* something tells it to stop. (I accidentally made one that ran forever today and crashed my program lol).

## 4. Functions
* You make these using the word `def`. 
* They are basically mini-programs that you write once and can use over and over. You can give them inputs (arguments) and they spit out an answer using `return`.

## 5. Figuring out what my code is doing (Print vs. Logging)
* **`print()`:** I use this for everything right now. It just prints text to the screen so I can see what a variable is doing.
* **`logging`:** Apparently, this is what real developers use instead of print. You can set it to different levels like `ERROR` or `INFO` and save it to a file. I'm not really using this yet, but good to know!

## 6. When Things Break (Errors & Stack Traces)
When my code crashes, Python yells at me with a giant block of red text called a **Stack Trace**.

**The coolest trick I learned today:** Read it from the **bottom up!**
1.  **The Bottom Line (The "What"):** The very last line tells you the actual error (like `TypeError`).
2.  **Right Above That (The "Where"):** This tells you the exact line number in my file where I messed up.
3.  **The Top Stuff (The "How"):** This shows the trail of how the code got to the error. I mostly ignore the deep stuff unless it's pointing to my own code.

### Errors I keep getting:
* **`SyntaxError`:** Means I messed up the grammar. Usually, I forgot a colon `:` at the end of an `if` statement or missed a parenthesis.
* **`NameError`:** I tried to use a variable I haven't made yet. Usually a typo on my part.
* **`TypeError`:** Trying to mix things that don't mix. Like trying to add the word "hello" to the number 5. 
* **`ValueError`:** Right type of thing, but bad value. Like telling Python to turn the word "apple" into a number.
* **`IndexError`:** I asked for an item in a list that isn't there (like asking for the 5th item in a list that only has 3 things).
* **`KeyError`:** I tried to look up a word in my dictionary that doesn't exist.
* **`AttributeError`:** Trying to do something to a variable that it can't do.