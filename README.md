# Code_Alpha_Hangman_game
Code Alpha - Python Programming Internship - Task 1: Hangman game

# CodeAlpha: Hangman Game (Interactive Word Guessing System)

## **Project Overview**
            This project is an interactive, console-based Hangman game developed as part of the Python Programming Internship at CodeAlpha. The game challenges users to guess a randomly chosen word from an analytical word bank, supporting both single-letter guesses and full-word guesses with robust input validation.

## **Key Concepts Used**
1. **Random Selection ("random.choice")-** Uses Python's built-in 'random' module to dynamically select a secret word from a predefined list.
2. **State & Tracking Variables-** Tracks the user's remaining attempts and guessed letters using list structures to manage game states dynamically.
3. **Iterative Progress Display-** Uses a 'for' loop to scan the secret word, revealing correctly guessed letters while hiding others behind underscores ('_').
4. **Instant-Win Logic-** Features an advanced shortcut conditional check that allows the player to guess the entire word instantly for a quick victory.
5. **Strict Input Validation-** Prevents program crashes by explicitly trapping invalid inputs (numbers, symbols, or double-guesses) and penalizing incorrect full-word attempts.

## **Game Mechanics & Flow**
1. **The Core Loop:** The system displays the masked word progress and current attempts left, looping continuously while attempts remain.
2. **Guess Processing:**
   * **Exact Match-** Guessing the whole secret word instantly triggers the victory state.
   * **Valid Letter-** If the single letter exists in the word, it reveals itself on the next turn.
   * **Invalid Entries-** Non-alphabetic inputs or previously guessed letters are caught gracefully.
3. **Endgame States:**
   * **Victory-** Unveiling all characters or guessing the word directly ends the program with a win message.
   * **Defeat-** Running out of attempts reveals the secret word and terminates.

## **How to Run**
1. Copy the code from "hangman game.py".
2. Paste it into any Python 3 environment (like OnlineGDB, VS Code, or Google Colab).
3. Hit **Run** and attempt to crack the secret word!
