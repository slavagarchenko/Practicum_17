def count_word_frequencies(words_list: list) -> dict:
    """
    Count frequencies of words in a list.

    Args:
        words_list (list): List of words.

    Returns:
        dict: Dictionary with words as keys and their frequencies as values.
    """
    word_count = {}

    for word in words_list:
        match word in word_count:
            case True:
                word_count[word] += 1

            case False:
                word_count[word] = 1

    return word_count


def main() -> None:
    """
    Main function.
    """
    try:
        string = input("Введите строку: ").strip()

        if not string:
            print("Введена пустая строка")
            return

        words_list = string.split()
        word_count = count_word_frequencies(words_list)
        sorted_words = sorted(word_count.items(), key=lambda x: x[1],
                              reverse=True)

        for word, count in sorted_words:
            print(word)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
