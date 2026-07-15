import random
def play_hangman():
    print("--- WELCOME TO HANGMAN GAME ---")

    # 1. Predefined list of 5 words
    word_bank = ["research", "inquiry", "science", "testing", "analyse"]
    secret_word = random.choice(word_bank)

    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        # Displaying the word progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord: " + display_word.strip())
        print(f"Attempts left: {attempts_left}")

        # Check Win Condition
        if "_" not in display_word:
            print(f"\n🎉 Victory, Master! You guessed the word: {secret_word}!")
            return

        # Take user guess
        guess = input("Guess a letter (or the whole word!): ").lower().strip()

        # INSTANT WIN: If you guess the whole word perfectly!
        if guess == secret_word:
            print(f"\n🎉 Incredible! You guessed the entire word instantly: {secret_word}!")
            return

        # Input validation for single letters
        if len(guess) != 1:
            print("Bot: That wasn't the secret word, and it's longer than 1 letter. Strike!")
            attempts_left -= 1
            continue

        if not guess.isalpha():
            print("Bot: Invalid entry. Please enter text characters only.")
            continue

        if guess in guessed_letters:
            print("Bot: You already guessed that letter!")
            continue

        # Process the single letter guess
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Bot: Correct guess!")
        else:
            print("Bot: Strike! That letter is not in the word.")
            attempts_left -= 1

    print(f"\n💀 Game Over. The secret word was: {secret_word}.")

play_hangman()
