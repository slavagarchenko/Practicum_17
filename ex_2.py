def build_dictionary(num_pairs: int) -> dict:
    """
    Build a translation dictionary from input pairs.

    Args:
        num_pairs (int): Number of word pairs to read.

    Returns:
        dict: Dictionary with source words as keys and translations as values.
    """
    dictionary = {}

    for _ in range(num_pairs):
        string = input().strip()
        words_list = string.split()
        dictionary[words_list[0]] = words_list[1]

    return dictionary


def translate_sentence(sentence: str, dictionary: dict) -> list:
    """
    Translate a sentence using the dictionary.

    Args:
        sentence (str): Sentence to translate.
        dictionary (dict): Translation dictionary.

    Returns:
        list: List of translated words (original if not found).
    """
    words = sentence.split()
    translated_words = []

    for word in words:
        match word in dictionary:
            case True:
                translated_words.append(dictionary[word])

            case False:
                translated_words.append(word)

    return translated_words


def main() -> None:
    """
    Main function.
    """
    try:
        number = int(input())

        if number < 0:
            print("Количество пар должно быть неотрицательным")
            return

        dictionary = build_dictionary(number)
        sentence = input().strip()
        translated_words = translate_sentence(sentence, dictionary)

        for word in translated_words:
            print(word, end=" ")

        print()

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
