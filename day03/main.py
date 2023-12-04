from typing import Generic, List, TypeVar


T = TypeVar("T")


class NQueue(Generic[T]):
    def __init__(self, n: int) -> None:
        self.queue: List[T | None] = [None for _ in range(n)]
        self.n = n

    def add(self, x: T) -> None:
        self.queue[1:] = self.queue[0 : self.n - 1]
        self.queue[0] = x

    def get(self, i: int) -> T | None:
        return self.queue[i]


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        print(get_parts_sum(file))


def get_parts_sum(file) -> int:
    three_queue: NQueue[str] = NQueue(3)
    total = 0
    while True:
        raw_line = file.readline()
        three_queue.add(raw_line.strip())
        line_to_scan = three_queue.get(1)
        if line_to_scan is None:
            continue
        total += scan_line_for_parts(three_queue, line_to_scan)
        if raw_line == "":
            break
    return total


def scan_line_for_parts(line_queue: NQueue[str], line: str) -> int:
    cursor_idx = 0
    total = 0
    while cursor_idx < len(line):
        char = line[cursor_idx]
        if char.isdigit():
            part_number_len = find_part_number_length(line, cursor_idx)
            part_number = int(line[cursor_idx : cursor_idx + part_number_len])
            if is_valid_part(line_queue, cursor_idx, part_number_len):
                total += part_number
            cursor_idx = cursor_idx + part_number_len
        else:
            cursor_idx += 1
    return total


def find_part_number_length(line: str, start: int) -> int:
    for i in range(start, len(line)):
        if not line[i].isdigit():
            return i - start
    return len(line) - start


def is_valid_part(line_queue: NQueue[str], cursor_idx: int, part_number_len: int):
    for line in line_queue.queue:
        if line is None:
            continue
        if any(
            is_symbol(line[x])
            for x in range(
                max(cursor_idx - 1, 0), min(cursor_idx + part_number_len + 1, len(line))
            )
        ):
            return True
    return False


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


if __name__ == "__main__":
    main()
