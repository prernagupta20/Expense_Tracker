Expense Tracker
Overview

The Expense Tracker is a Python-based console application designed to help users manage and monitor their daily expenses. It allows users to record expenses with details such as date, category, description, and amount. The application is simple, lightweight, and ideal for beginners learning Python programming while creating a practical personal finance tool.

Core Architecture

The project follows a procedural programming approach. Expenses are stored in an in-memory list, with each expense represented as a dictionary:

{
  "date": "DD-MM-YYYY",
  "category": "Food/Travel/etc",
  "description": "Expense details",
  "amount": 250.0
}


The program uses a menu-driven interface to interact with the user. A while loop keeps the menu active until the user chooses to exit. Functions such as adding, viewing, searching, deleting expenses, and calculating total spending operate on the list of dictionaries.

Features

Add Expense: Record new expenses with date, category, description, and amount.

View All Expenses: Display all recorded expenses in a clean, numbered list.

Total Spending: Calculate and display the sum of all expenses.

Search Expense: Find expenses by keyword in date, category, or description.

Delete Expense: Remove any expense by selecting its index from the list.

Exit: Safely terminate the program.

Technical Specifications

Programming Language: Python 3

Data Structures: Lists and Dictionaries

Interface: Console-based, menu-driven

Dependencies: None (uses Python standard library)

Platform: Cross-platform (Windows, macOS, Linux)
