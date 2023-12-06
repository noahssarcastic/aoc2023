def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        print(parse_file(file))


def parse_file(file):
    pts = 0
    for raw_line in file:
        line_str = raw_line.strip()
        win_str, numbers_str = line_str.split(":")[1].split("|")
        winners = [int(x.strip()) for x in win_str.split()]
        numbers = [int(x.strip()) for x in numbers_str.split()]
        wins = sum([1 if x in numbers else 0 for x in winners])
        if wins == 0:
            continue
        pts += 2 ** (wins - 1)
    return pts


if __name__ == "__main__":
    main()
