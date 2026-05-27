##  1. Connecting to APIs
An **API** (Application Programming Interface) is just a fancy way for two computer programs to talk to each other. 
To get Python to talk to OpenAI or Ollama, you use a Python library (usually the `openai` package). 

* **The Secret Trick:** Ollama was built to *mimic* OpenAI's API. That means you can write your Python code once using the `openai` library, and by just changing the web address (the URL), you can switch between paying for OpenAI in the cloud or running Ollama for free on your laptop!

---

## 2. Response Handling
When you ask the AI a question, it doesn't just hand you back a simple sentence. It throws back a big, complex package of data (called a JSON object). 

* **What's inside the package?** It includes metadata like how many tokens you used, the model name, and the actual answer.
* **Digging for gold:** To get the text you actually want to read, your Python code has to dig into that package. It usually looks like a Russian nesting doll of code: 
  `answer = response.choices[0].message.content`
  *(Translation: Open the response -> look at the first choice -> read the message -> grab the text content).*

---

##  3. Streaming Outputs
Have you noticed that ChatGPT types out its answers word-by-word? That is called **Streaming**.

* **Without Streaming:** You ask a question. Python waits... and waits... and waits 10 seconds for the AI to finish writing the whole essay. Then it dumps the whole text on your screen at once. Boring!
* **With Streaming:** The AI sends you pieces of the answer (chunks of tokens) as soon as it thinks of them. Your Python app catches these chunks and prints them immediately, creating that cool real-time typewriter effect. It makes your app feel 100x faster.

---

## 4. Prompt Chaining 
Sometimes, asking an AI to do a massive task in one single prompt makes it confused and produces garbage. **Prompt Chaining** is the fix.

Instead of one giant prompt, you break the job into an assembly line of smaller, focused prompts. You take the **output** of Prompt 1 and use it as the **input** for Prompt 2.

* **Step 1 (Extraction):** "Read this messy 5-page email thread and extract just the names of the people."
* **Step 2 (Formatting):** Give the list of names from Step 1 to the AI and say: "Put these names into a neat comma-separated list."
* **Why do this?** It gives the AI smaller, easier jobs. It results in way fewer mistakes and makes your code much more reliable!