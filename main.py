import random


DATA = [random.randint(1, 101) for _ in range(10)]


def selection_sort(items):
    for curr in range(len(items)):
        for seek in range(curr + 1, len(items)):
            if items[seek] < items[curr]:
                items[curr], items[seek] = items[seek], items[curr]


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
    selection_sort(data)
    print(data)

    data = DATA.copy()
    insertion_sort(data)
    print(data)


if __name__ == '__main__':
    main()

