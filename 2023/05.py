# ===== PART 1 ===== #

def find_dest(start: int, map_lines: list[str]) -> dict[int, int]:
    for line in map_lines:
        dest_start, source_start, length = map(int, line.split())
        if start in range(source_start, source_start + length):
            diff = start - source_start
            return dest_start + diff
    return start

def final_value(start: int, maps: list[list[str]]) -> int:
    print(f"Working on seed {start}")
    for map in maps:
        start = find_dest(start, map)
    return start

def parse_lines(lines: list[str]) -> tuple[list[int], list[list[str]]]:
    seeds = list(map(int, lines[0][6:].split()))
    maps = []
    for i in range(2, len(lines)):
        if "map" in lines[i]:
            start = i+1
            continue
        if lines[i] == "" or i == len(lines) - 1:
            end = i
            if i == len(lines) - 1:
                end += 1
            maps.append(lines[start:end])
    return seeds, maps

def part_one() -> None:
    lines = open("input.txt").read().splitlines()
    seeds, maps = parse_lines(lines)
    locations = [final_value(seed, maps) for seed in seeds]
    print(min(locations))


# ===== PART 2 ===== #

def seeds_from_ranges(ranges: list[int]) -> list[int]:
    seeds = []
    for i in range(0, len(ranges), 2):
        print(i)
        start, length = ranges[i: i+2]
        seeds += range(start, start + length)
    return seeds

# need to work on a faster solution
def part_two() -> None:
    lines = open("input.txt").read().splitlines()
    ranges, maps = parse_lines(lines)
    seeds = seeds_from_ranges(ranges)
    locations = [final_value(seed, maps) for seed in seeds]
    print(min(locations))


# ===== SOLUTIONS ===== # 

if __name__ == "__main__":
    print("===== Part 1 =====")
    part_one()
    print("===== Part 2 =====")
    part_two()