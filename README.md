# U.S. States Guessing Game

![U.S. States Game Screenshot](blank_states_img.gif)

A simple game to test your knowledge of the 50 U.S. states, built with Python. Created as part of the 100 Days of Code challenge.

### Features

* Guess state names and see them appear on the map.
* Type "Exit" to quit at any time.
* When you exit, a `states_to_learn.csv` file is automatically created with all the states you missed!

### How to Run

1.  Clone this repository.
2.  Install the requirements:
    ```bash
    pip install pandas
    ```
3.  Run the game:
    ```bash
    python main.py
    ```

### What I Learned

This project was great practice for a few key things:

* Reading and filtering data from a CSV file using the **Pandas** library.
* Using the **Turtle** library to create a simple GUI and handle user input.
* Managing game state with `while` loops and lists.
* Creating new files to save data for the user.