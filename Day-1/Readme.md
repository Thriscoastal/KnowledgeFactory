# Python Fundamentals: Core Concepts

This document tracks the foundational concepts of Python programming.

## 1. Variables & Data Types
*   **Variables:** Think of variables as labeled containers that store data in the computer's memory. You assign a value to a variable using the `=` operator.
*   **Common Data Types:**
    *   `int`: Whole numbers (e.g., `85`, `-10`).
    *   `float`: Decimal numbers (e.g., `92.5`, `3.14`).
    *   `str`: Strings, which are sequences of text wrapped in quotes (e.g., `"Hello"`, `'Python'`).
    *   `bool`: Booleans, representing truth values (`True` or `False`).
    *   `list`: Ordered, mutable collections of items (e.g., `[90, 85, 95]`).
    *   `dict`: Dictionaries, storing data in key-value pairs (e.g., `{"name": "Alice", "score": 90}`).

## 2. Conditions (Control Flow)
Conditions allow the program to make decisions based on whether a statement is `True` or `False`.
*   `if`: Runs a block of code if the condition is true.
*   `elif` (Else If): Checks another condition if the previous `if` was false.
*   `else`: Runs if all preceding conditions are false.

## 3. Loops
Loops are used to repeat a block of code automatically.
*   **`for` loop:** Best for iterating over a known sequence (like a list, dictionary, or a specific range of numbers).
*   **`while` loop:** Best for repeating code as long as a certain condition remains `True`.

## 4. Functions
Functions are reusable blocks of code that perform a specific task.
*   Defined using the `def` keyword.
*   They can take **arguments** (inputs) and `return` **outputs**.
*   Using functions keeps code DRY (Don't Repeat Yourself) and highly organized.

## 5. Debugging: Print vs. Logging
*   **`print()`:** Great for quick, temporary checks to see what value a variable holds at a specific moment.
*   **`logging`:** The professional way to track events. It allows you to set different levels of importance (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) and can be easily turned on/off or saved to a file without deleting the code.

## 6. Understanding Errors & Stack Traces
When Python encounters an error, it stops and prints a **Stack Trace** (or Traceback). 
*   **How to read it:** Always read a stack trace from the **bottom up**.
    *   The **last line** tells you the *type* of error (e.g., `TypeError`, `IndexError`, `NameError`) and a brief description.
    *   The **lines right above it** show you exactly which line of *your* code caused the crash.
    *   The **top lines** show the sequence of function calls that led to the error (the "stack").

### Common Types of Errors
Familiarizing yourself with the most frequent Python errors makes diagnosing issues significantly faster:
*   **`SyntaxError`:** The code violates Python's grammar rules (e.g., missing a colon `:`, unmatched parentheses).
*   **`NameError`:** Trying to use a variable or function name that hasn't been defined yet, often due to a typo.
*   **`TypeError`:** An operation is applied to an object of the wrong type (e.g., trying to add a string to an integer).
*   **`ValueError`:** A function gets an argument of the right type but an inappropriate value (e.g., `int("hello")`).
*   **`IndexError`:** Attempting to access a list element using an index that is out of bounds (e.g., asking for the 5th item in a 3-item list).
*   **`KeyError`:** Trying to look up a key in a dictionary that does not exist.
*   **`AttributeError`:** Attempting to use a method or property that an object doesn't possess (e.g., trying to use `.append()` on a string).

### How to Debug Using Stack Traces
A stack trace is essentially Python's way of showing you the exact breadcrumb trail of what was happening right before the program crashed. 

To effectively debug using a stack trace, **always read it from the bottom up.** 

Start by looking at the very last line; this is your "What." It will explicitly state the error type (like `TypeError` or `KeyError`) and provide a brief, specific message about what went wrong. Once you understand the *what*, look at the two lines immediately above it. This is your "Where." Python will point you to the exact file and line number in your code where the failure occurred. Go to that line in your editor and ask yourself how the specific error applies to that line. 

If the problem isn't immediately obvious on that single line, continue reading upwards through the trace. This reveals the "How." The trace shows the sequence of function calls (the stack) that led to the crash. For instance, if your line says `calculate_grade(student_score)` and it caused a `TypeError`, but `student_score` is a variable passed in from elsewhere, you look at the next block up in the trace to see where `calculate_grade` was called. By tracing the execution backwards, you can track down exactly where bad data entered your system. Ignore deep, internal paths to third-party libraries (like Pandas or standard library files) unless you are absolutely certain the bug isn't in your own code first.