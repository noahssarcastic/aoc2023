from typing import List


class Queue:
    def __init__(self) -> None:
        self.queue: List[int] = []

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        temp = self.queue[0]
        self.queue = self.queue[1:]
        return temp

    def set(self, i: int, x: int) -> None:
        self.queue[i] = x

    def get(self, i: int) -> int:
        return self.queue[i]


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        print(parse_file(file))


def parse_file(file):
    cards = 0
    extra_cards = Queue()
    for raw_line in file:
        line_str = raw_line.strip()
        win_str, numbers_str = line_str.split(":")[1].split("|")
        winners = [int(x.strip()) for x in win_str.split()]
        numbers = [int(x.strip()) for x in numbers_str.split()]

        try:
            copies = extra_cards.dequeue() + 1
        except IndexError:
            copies = 1
        cards += copies

        wins = sum(1 if x in numbers else 0 for x in winners)
        for i in range(wins):
            try:
                extra_cards.set(i, extra_cards.get(i) + copies)
            except IndexError:
                extra_cards.enqueue(copies)
    return cards


if __name__ == "__main__":
    main()
