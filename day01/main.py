"""
Day 1

https://adventofcode.com/2023/day/1

Part 1:
The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value 
that the Elves now need to recover. 
On each line, the calibration value can be found 
by combining the first digit and the last digit (in that order) 
to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 
12, 38, 15, and 77. 
Adding these together produces 142.
Consider your entire calibration document. 
What is the sum of all of the calibration values?

Part 2:
Your calculation isn't quite right. 
It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine 
also count as valid "digits".

Equipped with this new information, 
you now need to find the real first and last digit on each line. 

For example:
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.

What is the sum of all of the calibration values?
"""

LOOKUP_TABLE = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

MAX_KEY_LENGTH = 5


class Trie:
    """
    Represent a simple prefix tree (https://en.wikipedia.org/wiki/Trie).

    This implementation does not support mid-branch word terminations.
    Words like "go, golf, golfer" or "tea, teahouse"
    cannot be loaded into the tree together.
    """

    def __init__(self) -> None:
        self._trie = {}

    def add_branch(self, key: str, value: int) -> None:
        """Add a key (branch) to the tree."""
        cursor = self._trie
        for i, char in enumerate(key):
            if i == len(key) - 1:
                cursor[char] = value
                break
            if char not in cursor:
                cursor[char] = {}
            cursor = cursor[char]

    def search(self, key: str) -> int:
        """
        Search the tree for a given key.

        Return -1 if key not found.
        """
        cursor = self._trie
        try:
            for char in key:
                if isinstance(cursor, int):
                    return cursor
                cursor = cursor[char]
            return -1
        except KeyError:
            return -1


def main():
    """Calculate the sum of the first and last digits per line."""
    trie = Trie()
    for k, v in LOOKUP_TABLE.items():
        trie.add_branch(k, v)

    with open(input.txt, "r", encoding="utf-8") as file:
        print(iterate_file(file, trie))


def iterate_file(file, trie) -> int:
    """Iterate through file and calculate sum from first & last digits."""
    total = 0
    for line in file:
        first = find_first_digit(trie, line)
        last = find_first_digit(trie, line, reverse=True)
        total += first * 10 + last
    return total


def find_first_digit(trie, line, reverse=False):
    """
    Find the first numerical or spelled digit in a line.

    Set reverse to True to search the line end to start.
    """
    if reverse:
        iterator = zip(range(len(line) - 1, -1, -1), reversed(line))
    else:
        iterator = enumerate(line)
    for i, char in iterator:
        if char.isdigit():
            return int(char)
        maybe_digit = trie.search(line[i : i + MAX_KEY_LENGTH + 1])
        if maybe_digit > 0:
            return maybe_digit
    raise RuntimeError(f"no digits found in line {line}")


if __name__ == "__main__":
    main()
