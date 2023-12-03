import re
from typing import Self


class CubeSet:
    def __init__(self) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0

    def load_set_string(self, set_string: str) -> Self:
        for color_str in [x.strip() for x in set_string.split(",")]:
            re_match = re.search(r"(\d+) (\w+)", color_str)
            if re_match is None:
                raise RuntimeError(f"set not in expected format: {set_string}")
            num, color = int(re_match.group(1)), re_match.group(2)
            match color:
                case "red":
                    self.red = num
                case "green":
                    self.green = num
                case "blue":
                    self.blue = num
        return self

    def power(self) -> int:
        return self.red * self.blue * self.green

    def __repr__(self) -> str:
        return f"Set[{self.red}r,{self.green}g,{self.blue}b]"


def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        total = 0
        for line in file:
            game_id, sets = line.split(":")
            re_match = re.search(r"Game (\d+)", game_id)
            if re_match is None:
                raise RuntimeError(f"game id not in expected format: {game_id}")
            game_id = int(re_match.group(1))
            sets = [CubeSet().load_set_string(x.strip()) for x in sets.split(";")]
            min_set = CubeSet()
            for s in sets:
                min_set.red = max(s.red, min_set.red)
                min_set.green = max(s.green, min_set.green)
                min_set.blue = max(s.blue, min_set.blue)
            total += min_set.power()
        print(total)


if __name__ == "__main__":
    main()
