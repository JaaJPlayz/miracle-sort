def is_sorted(arr: list[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def miracle_sort(arr: list[int]) -> list[int]: ...


def main() -> None:
    my_arr = [1, 2, 3, 3, 1, 2, 4, 5, 1, 5]

    while not is_sorted(my_arr):
        sorted_arr = miracle_sort(my_arr)


if __name__ == "__main__":
    main()
