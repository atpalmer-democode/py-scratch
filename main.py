import random


DATA = [random.randint(1, 101) for _ in range(10)]


def selection_sort(items):
    for curr in range(len(items)):
        for seek in range(curr + 1, len(items)):
            if items[seek] < items[curr]:
                items[curr], items[seek] = items[seek], items[curr]


def main():
    data = DATA.copy()
    print(data)
    selection_sort(data)
    print(data)


if __name__ == '__main__':
    main()

