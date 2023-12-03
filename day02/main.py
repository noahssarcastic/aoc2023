import re


MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


class CubeSet:
    def __init__(self, set_string: str) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0
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
            sets = [CubeSet(x.strip()) for x in sets.split(";")]
            if all(
                x.red <= MAX_RED_CUBES
                and x.green <= MAX_GREEN_CUBES
                and x.blue <= MAX_BLUE_CUBES
                for x in sets
            ):
                total += game_id
        print(total)


if __name__ == "__main__":
    main()
