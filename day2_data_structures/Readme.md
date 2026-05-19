# Day 2 of Python: Data Structures, JSON, and Practice

##  Table of Contents
- [1. Lists](#1-lists)
- [2. Tuples](#2-tuples)
- [3. Sets](#3-sets)
- [4. Dictionaries (Dicts)](#4-dictionaries-dicts)
- [5. Comprehensions](#5-comprehensions)
- [6. JSON Handling](#6-json-handling)

---

## 1. Lists
Lists are exactly what they sound like: a sequence of items in a specific order.
- **Syntax:** Square brackets `[]`
- **Example:** `["apple", "banana", "cherry"]`
- **Key Features:** - **Mutable:** You can change them whenever you want.
  - Use `.append()` to add items to the end.
  - Use `.pop()` to remove items.
  - Duplicates are allowed (Python doesn't care if the same item is in there twice).

## 2. Tuples
Tuples are immutable lists. 
- **Syntax:** Parentheses `()`
- **Example:** `(40.7128, -74.0060)`
- **Key Features:**
  - **Immutable:** Once created, they cannot be changed.
  - Perfect for data that should never ever change while the program is running, like map coordinates.
  - Python runs them a tiny bit faster than lists.

## 3. Sets
A set is a jumbled-up bag of items.
- **Syntax:** Curly braces `{}`
- **Example:** `{2, 4, 6, 8}`
- **Key Features:**
  - No specific order.
  - **No duplicates allowed.**
  - *Best trick:* If you have a list with duplicate numbers and only want the unique ones, turn it into a set—duplicates vanish instantly! 
  - Super fast for checking if an item exists inside them.

## 4. Dictionaries (Dicts)
Dictionaries store data in "Key-Value" pairs. Instead of looking up an item by its position in a line, you look it up by its name (the key).
- **Syntax:** Curly braces with colons `{key: value}`
- **Example:** `{"username": "coder_99", "score": 100}`
- **Key Features:**
  - *Pro tip:* Instead of doing `my_dict["score"]`, it's safer to use `my_dict.get("score")`. That way, if the "score" key doesn't exist, the whole program won't crash with a `KeyError`.

## 5. Comprehensions
A shortcut to create a list or dictionary in just one single line of code.
- **Example:** `[x * 2 for x in my_list]`
- **Why use it?** Instead of writing a big, bulky `for` loop that takes up 4 lines just to multiply some numbers, you squish it inside the brackets. It does the exact same thing as a normal loop, it just looks cooler and saves space.

## 6. JSON Handling
JSON (JavaScript Object Notation) is a text format used to send data across the internet or save it to a file. It looks exactly like a Python Dictionary.
- **Setup:** You must `import json` at the top of your file.
- **`json.dumps()`:** Takes a Python dictionary and turns it into a giant text string (the "s" stands for string) so you can save it or send it.
- **`json.loads()`:** Takes a giant text string of JSON and turns it back into a normal Python dictionary that you can actually use in your code.
