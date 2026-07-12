# Digital Time Capsule

***CS50’s Introduction to Programming with Python - FINAL PROJECT***

## Video Demo

https://youtu.be/80yTvTo5Q7E

## Description

> A command-line application for writing messages to your future self.

**Digital Time Capsule** is a Python application that lets you create personal "time capsules" containing messages, goals, memories, or reflections that remain locked until a date you choose.

Instead of burying a physical box, your memories are securely stored in a local JSON file and can only be opened once their unlock date has arrived.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Crypt_of_civilization.jpg/960px-Crypt_of_civilization.jpg" alt="Crypt of Civilization interior, photographed prior to sealing" width="500">

*The Crypt of Civilization — not to be opened until 8113. Source: Wikipedia.*

## Features

- Create digital time capsules
- Set a future unlock date
- Record your current mood
- Automatically generate a unique 4-digit ID for every capsule
- Persistent storage using JSON
- Search capsules by title
- View all saved capsules
- Delete unwanted capsules
- Open capsules once their unlock date has been reached

## How It Works

Each capsule contains:

- **ID** – randomly generated unique 4-digit identifier
- **Title** – short name for the capsule
- **Message** – your note to your future self
- **Unlock Date** – when the capsule becomes available
- **Mood** – how you felt when creating it

All capsules are stored locally in `capsules.json`, allowing them to persist between program runs.

## Design

### Object-Oriented Programming (OOP)

Each capsule is represented by a `Capsule` class, making the code easier to organize and extend. This approach keeps related data and functionality together while making future features easier to implement.

### JSON Storage

Instead of using a database, the project stores data in a simple JSON file. This keeps the application lightweight and easy to understand while providing persistent storage.

### Unique IDs

Each capsule receives a randomly generated four-digit ID using Python's `random` module. Before assigning an ID, the program checks existing capsules to ensure there are no duplicates.

## Testing

This project includes a `pytest` test file located in `test_project.py` that tests core functionality such as capsule creation, unique ID generation, and saving and loading JSON data. Temporary files are used during testing so `capsules.json` is never modified.
