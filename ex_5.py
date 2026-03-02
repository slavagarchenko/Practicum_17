def build_family_tree(num_relations: int) -> dict:
    """
    Build a family tree dictionary from parent-child relations.

    Args:
        num_relations (int): Number of parent-child relations to read.

    Returns:
        dict: Dictionary with parent as key and list of children as value.
    """
    family_tree = {}

    for _ in range(num_relations):
        string = input().strip()
        words_list = string.split()
        parent = words_list[0]
        child = words_list[1]

        match parent in family_tree:
            case True:
                family_tree[parent].append(child)

            case False:
                family_tree[parent] = [child]

    return family_tree


def count_descendants(person: str, family_tree: dict) -> int:
    """
    Recursively count all descendants (children, grandchildren, etc.) for a person.

    Args:
        person (str): Name of the person to count descendants for.
        family_tree (dict): Dictionary with parent as key and list of children as value.

    Returns:
        int: Total number of descendants.
    """
    if person not in family_tree:
        return 0

    total = 0

    for child in family_tree[person]:
        total += 1
        total += count_descendants(child, family_tree)

    return total


def main() -> None:
    """
    Main function.
    """
    try:
        number = int(input())

        if number < 0:
            print("Количество отношений должно быть неотрицательным")
            return

        family_tree = build_family_tree(number)
        target_person = input().strip()
        result = count_descendants(target_person, family_tree)

        print(result)

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены корректные данные")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
