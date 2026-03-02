def build_dictionary(num_pairs: int) -> dict:
    """
    Build an antonyms dictionary from input pairs.

    Args:
        num_pairs (int): Number of word pairs to read.

    Returns:
        dict: Dictionary with words as keys and their antonyms as values.
    """
    dictionary = {}

    for _ in range(num_pairs):
        string = input().strip()
        words_list = string.split()
        dictionary[words_list[0]] = words_list[1]

    return dictionary


def find_antonym(word: str, dictionary: dict) -> str:
    """
    Find antonym for a word using the dictionary.

    Args:
        word (str): Word to find antonym for.
        dictionary (dict): Antonyms dictionary.

    Returns:
        str: Antonym if found, otherwise the original word.
    """
    match word in dictionary:
        case True:
            return dictionary[word]

        case False:
            return word


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
        target_word = input().strip()
        result = find_antonym(target_word, dictionary)

        print(result)

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
