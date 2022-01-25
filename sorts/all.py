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


def merge_sort(items):
    if len(items) < 2:
        return items
    midp = len(items) // 2
    left, right = merge_sort(items[0:midp]), merge_sort(items[midp + 1:-1])
    result = []
    iterl, iterr = iter(left), iter(right)

    DONE = object()
    def next_or_done(i):
        try:
            return next(i)
        except:
            return DONE

    currl = next_or_done(iterl)
    currr = next_or_done(iterr)

    while True:
        print(result)
        if currl is not DONE and currr is not DONE and currl < currr:
            result.append(currl)
            currl = next_or_done(iterl)
        elif currr is not DONE:
            result.append(currr)
            currr = next_or_done(iterr)
        elif currl is not DONE:
            result.append(currl)
            currl = next_or_done(iterl)
        else:
            return result


def main():
    print(DATA)

    data = DATA.copy()
    selection_sort(data)
    print(data)

    data = DATA.copy()
    insertion_sort(data)
    print(data)

    data = DATA.copy()
    data = merge_sort(data)
    print(data)


if __name__ == '__main__':
    main()

