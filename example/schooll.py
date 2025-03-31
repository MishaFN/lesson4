def hangman():
    word = input("Player 1, enter a word: ").upper()
    guessed_word = ["*" for _ in word]
    lives = 5
    guessed_letters = set()

    while lives > 0 and "*" in guessed_word:
        print("\nWord to guess:", "".join(guessed_word))
        print(f"You have {lives} lives left.")
        guess = input("Letter? ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            lives -= 1

    if "*" not in guessed_word:
        print("\nCongratulations! You guessed the word:", "".join(guessed_word))
    else:
        print("\nGame over! The word was:", word)

hangman()