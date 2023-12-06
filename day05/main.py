def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        print(parse_file(file))


def parse_file(file):
    for raw_line in file:
        line_str = raw_line.strip()


if __name__ == "__main__":
    main()
