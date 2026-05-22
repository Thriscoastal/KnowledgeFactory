# Day 5: Object-Oriented Programming & System Architecture

## Overview
Documenting my foundational learnings in Python OOP and system architecture

## 1. Core OOP Concepts

* **Class & Object:** A class acts as a structural blueprint, while an object is a specific instance created from that blueprint.
* **Class and Object Attributes:** Object attributes (using `self`) are unique to each instance. Class attributes are shared across all instances of the class.
* **Encapsulation & Private Variables (`__name`):** Encapsulation restricts direct access to certain components. In Python, prefixing an attribute with a double underscore (`__`) makes it private, preventing unintended external modifications.
* **Abstraction:** The practice of hiding complex implementation details and exposing only the necessary functionalities to the user.
* **Inheritance & `super()`:** Inheritance allows a new class (child) to acquire the properties and methods of an existing class (parent). The `super()` function is used to securely call the parent class's methods, promoting code reusability.
* **Polymorphism:** The ability of different classes to respond to the same method call in their own unique way. 
* **Class Decorators & Static Methods:** * `@staticmethod`: A utility function grouped within a class that does not require access to instance (`self`) or class (`cls`) data.
    * `@classmethod`: A method bound to the class itself rather than the instance, taking `cls` as its first parameter.

## 2. Modular Coding

Writing monolithic scripts is not sustainable for production. Modular coding involves dividing the codebase into distinct, manageable files based on functionality (e.g., separating database configurations, machine learning models, and API routing). This approach is highly critical when building scalable systems and simplifies debugging.

## 3. System Design Basics: Architecture Overview

Understanding the high-level flow of data is essential for full-stack and backend development:

* **Frontend (Client-Side):** The user interface. It captures user inputs and displays data but does not handle heavy business logic.
* **Backend (Server-Side):** The core engine of the application. This is where Python classes, AI model integrations, and business rules are executed. It processes requests from the frontend.
* **Database (Storage):** The persistent storage layer. The backend queries this layer to retrieve or update records before sending a response back to the client.

**Standard Data Flow:** The Frontend issues an API request -> The Backend processes the request and queries the Database -> The Database returns data to the Backend -> The Backend formats the data and serves it back to the Frontend.