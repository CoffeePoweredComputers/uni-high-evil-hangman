def get_largest_family(valid_words, letter_guess):

    families = dict()

    for word in valid_words:

        obfuscated_word = "".join(letter if letter == letter_guess else "-" for letter in word)

        if letter_guess not in obfuscated_word:
            continue

        if obfuscated_word not in families:
            families[obfuscated_word] = []

        families[obfuscated_word].append(word)

    return max(families.values(), key = lambda x: len(x)) if len(families) > 0 else None

def play_a_game(word_len, num_guesses, valid_words, show_total):

    guessed_letters = set()
    obfuscated_word = "-" * word_len

    while (num_guesses > 0) and ("-" in obfuscated_word):

        print("Guesses remaining:", num_guesses)

        if show_total:
            print("Words remaining:", len(valid_words))

        print("Word: ", obfuscated_word)

        letter_guess = input("Enter a letter: ")
        while (letter_guess in guessed_letters) or (not letter_guess.isalpha()) or (len(letter_guess) != 1):
            letter_guess = input("Invalid guess. Enter another letter: ")

        guessed_letters.add(letter_guess)

        words_with_letter = get_largest_family(valid_words, letter_guess)
        if words_with_letter is None:
            num_guesses -= 1
        else:
            valid_words = words_with_letter

        obfuscated_word = "".join(letter if letter in guessed_letters else "-" for letter in valid_words[0])

        print()
    print("You have guessed the word: ", obfuscated_word)

def main():
    # This is where you will implement the "main" flow of your program
    num_guesses = 10

    with open("dictionary.txt") as fp:
        word_list = list(map(str.strip, fp.readlines()))
    word_lengths = list(map(len, word_list))

    while True:
        print("--------------------------------------------------")
        print("|               Starting a New Game              |")
        print("--------------------------------------------------")

        while (word_len := int(input("Enter a length: "))) not in word_lengths:
            print("There are no words of this length. Please select another.")
            continue

        valid_words = [word for word in word_list if len(word) == word_len]
        show_words = input("Would you like to display the remaining word count (y/n)?").lower() == "y"
        print()

        play_a_game(word_len, num_guesses, valid_words, show_words)

        if input("Play again (y/n)?: ") == "n":
            break
        print()
            
if __name__ == "__main__":
    main()
