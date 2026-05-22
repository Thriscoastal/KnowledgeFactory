# Day 4: Making the Internet and AI Talk to My Code!

Welcome to my Day 4 notes! Honestly, today blew my mind. Up until now, my code only lived inside my own computer. Today, I learned how to make my programs talk to other servers across the internet and even plug into AI brains (both on my laptop and in the cloud!). 

Here is a breakdown of what I finally figured out today.

---

## 🍽️ 1. What the heck is a REST API?

Basically, an API (Application Programming Interface) is like a waiter at a restaurant. My code is the customer, and the server is the kitchen. I can't just go into the kitchen and grab data; I have to ask the waiter (the API) to get it for me. 

We do this using **HTTP Methods** (the type of request we are making):
*   **`GET`**: "Bring me the menu." (Fetching data)
*   **`POST`**: "Here is my order, please make it." (Sending new data to create something)
*   **`PUT` / `PATCH`**: "Can I change my side to fries?" (Updating existing data)
*   **`DELETE`**: "Cancel my order." (Deleting data)

### Status Codes 
Whenever you ask a server for something, it replies with a number code:
*   **`200 OK`**: Everything went perfectly!
*   **`201 Created`**: It successfully made the thing I `POST`ed.
*   **`400 Bad Request`**: I typed something wrong and the server is confused.
*   **`401 / 403`**: I forgot my password or API key. Access denied!
*   **`404 Not Found`**: I asked for a link that doesn't exist.
*   **`500 Internal Server Error`**: The server crashed on their end (not my fault!).

---

##  2. Postman (My New Best Friend)

Before writing actual Python code, I learned to use an app called **Postman**. It's basically a remote control for testing APIs. Instead of writing 10 lines of code just to see if a link works, I can just paste the URL into Postman, click "Send," and it shows me the data neatly formatted. It's a lifesaver for debugging!

---

## 3. Python `requests` Library

Okay, time to do it in code. Python has built-in ways to talk to APIs, but they are clunky. Everyone just uses a library called `requests` because it's super easy to read.

First, I had to install it in my terminal:
`pip install requests`

### Fetching Data (`GET`)
Here is how I pulled some fake data from a test website:

```python
import requests

# The URL I want to get data from
url = "[https://jsonplaceholder.typicode.com/posts/1](https://jsonplaceholder.typicode.com/posts/1)"


response = requests.get(url)

if response.status_code == 200:
    data = response.json() 
    print(f"I got the title! It is: {data['title']}")
else:
    print("Uh oh, something went wrong.")
