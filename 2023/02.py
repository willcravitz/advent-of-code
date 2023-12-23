import re

# ===== PART 1 ===== #

game_pattern = r'Game (\d+): (\w.+)'
cubes_pattern = r'(\d+) (\w+)'

def get_game_id(line: str) -> int:
    match = re.search(game_pattern, line)
    if match:
        game_id = int(match.group(1))
        return game_id
    return None

def get_min_cubes(line: str) -> dict[str, int]:
    match = re.search(game_pattern, line)
    if match:
        # info about the game
        game_info_line = match.group(2)
        # divide up into list of cube set lists
        cube_sets = [cube_set.split(',') for cube_set in game_info_line.split(';')]
        min_cubes = {}
        for cube_set in cube_sets:
            for cube in cube_set:
                match = re.search(cubes_pattern, cube)
                if match:
                    num, color = match.groups()
                    # add to the dict if largest instance of the color
                    if color not in min_cubes:
                        min_cubes[color] = int(num)
                    else:
                        if min_cubes[color] < int(num):
                            min_cubes[color] = int(num)
        return min_cubes
    return None

def game_is_possible(line: str, possible_cubes: dict[str, int]) -> bool:
    min_cubes = get_min_cubes(line)
    for color in possible_cubes:
        if color not in min_cubes:
            continue
        elif possible_cubes[color] < min_cubes[color]:
            return False
    return True

def part_one() -> None:
    possible_cubes = {}
    for color in ['red', 'green', 'blue']:
        possible_cubes[color] = int(input(f'How many {color} cubes are there? '))
    games = open("input.txt").read().splitlines()
    possible_game_ids = [get_game_id(game) for game in games if game_is_possible(game, possible_cubes)]
    print(sum(possible_game_ids))


# ===== PART 2 ===== #

def set_power(line: str) -> int:
    min_cubes = get_min_cubes(line)
    power = 1
    for color in min_cubes:
        power *= min_cubes[color]
    return power

def part_two() -> None:
    games = open("input.txt").read().splitlines()
    powers = [set_power(game) for game in games]
    print(sum(powers))


# ===== SOLUTIONS ===== # 

if __name__ == "__main__":
    print("===== Part 1 =====")
    part_one()
    print("===== Part 2 =====")
    part_two()