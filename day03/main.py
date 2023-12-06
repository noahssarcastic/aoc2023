from io import TextIOWrapper
from typing import List


class ThreeQueue:
    N = 3

    def __init__(self) -> None:
        self.queue: List[str] = ["" for _ in range(self.N)]

    def add(self, x: str) -> None:
        self.queue[1:] = self.queue[0 : self.N - 1]
        self.queue[0] = x

    def get(self, i: int) -> str:
        return self.queue[i]


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        print(parse_file(file))


def parse_file(file: TextIOWrapper) -> int:
    # we parse lines in three block chunks
    # the top line is parsed as a chunk of two, itself and the line below
    # the last line is parsed as a chunk of two, itself and the line above
    queue = ThreeQueue()
    total = 0
    for raw_line in file:
        line_str = raw_line.strip()
        queue.add(line_str)
        # if first line skip
        if line_str == "":
            continue
        total += sum(find_gear_ratios(queue))
    # handle last line
    queue.add("")
    total += sum(find_gear_ratios(queue))
    return total


def find_gear_ratios(queue: ThreeQueue) -> List[int]:
    line = queue.get(1)
    gear_ratios: List[int] = []
    for idx, char in enumerate(line):
        if char != "*":
            continue
        idx_range = range(idx - 1, (idx + 1) + 1)
        parts = find_part_numbers(queue, idx_range)
        if len(parts) == 2:
            gear_ratios.append(parts[0] * parts[1])
    return gear_ratios


def find_part_numbers(queue: ThreeQueue, idx_range: range) -> List[int]:
    # scan above, current, and below lines for part numbers in range
    parts: List[int] = []
    for line_to_scan in queue.queue:
        cursor = 0
        while cursor < len(line_to_scan):
            char = line_to_scan[cursor]
            if not char.isdigit() or cursor not in idx_range:
                cursor += 1
                continue
            start_idx = find_part_number_start(line_to_scan, cursor)
            end_idx = find_part_number_end(line_to_scan, cursor)
            part_number = int(line_to_scan[start_idx : end_idx + 1])
            parts.append(part_number)
            cursor += end_idx - cursor + 1
    return parts


def find_part_number_start(line: str, idx: int) -> int:
    for i, char in zip(range(idx, -1, -1), reversed(line[: idx + 1])):
        if not char.isdigit():
            return i + 1
    return 0


def find_part_number_end(line: str, idx: int) -> int:
    for i, char in zip(range(idx, len(line)), line[idx:]):
        if not char.isdigit():
            return i - 1
    return len(line) - 1


if __name__ == "__main__":
    main()
