def build_dictionary(num_entries: int) -> dict:
    """
    Build a dictionary mapping items to their form.

    Args:
        num_entries (int): Number of dictionary entries to read.

    Returns:
        dict: Dictionary with items as keys and their form as values.
    """
    dictionary = {}

    for _ in range(num_entries):
        string = input().strip()
        words_list = string.split()
        form = words_list[0]
        items = words_list[1:]

        for item in items:
            dictionary[item] = form

    return dictionary


def find_form(item: str, dictionary: dict) -> str:
    """
    Find the form for a given item using the dictionary.

    Args:
        item (str): Item to find form for.
        dictionary (dict): Dictionary with items as keys and forms as values.

    Returns:
        str: Form if found, otherwise the original item.
    """
    match item in dictionary:
        case True:
            return dictionary[item]

        case False:
            return item


def main() -> None:
    """
    Main function.
    """
    try:
        number = int(input())

        if number < 0:
            print("Количество записей должно быть неотрицательным")
            return

        dictionary = build_dictionary(number)
        target_item = input().strip()
        result = find_form(target_item, dictionary)

        print(result)

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
