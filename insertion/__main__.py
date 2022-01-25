import random


DATA = [random.randint(1, 101) for _ in range(10)]


def insertion_sort(items):
    for seek in range(1, len(items)):
        item = items[seek]
        for backtrack in range(seek - 1, -1, -1):
            if item < items[backtrack]:
                items[backtrack + 1] = items[backtrack]
            else:
                backtrack += 1
                break
        items[backtrack] = item


def main():
    print(DATA)

    data = DATA.copy()
    insertion_sort(data)
    print(data)


if __name__ == '__main__':
    main()

