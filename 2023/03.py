import re

# ===== PART 1 ===== #

num_pattern = r"\d+"

def find_matches(lines: list[list[str]]) -> list[int]:
    m = len(lines)
    n = len(lines[0])
    matches = []
    for i in range(len(lines)):
        line = lines[i]
        nums = re.findall(num_pattern, line)
        curr = 0
        j = 0
        while j < len(line):
            if line[j].isdigit():
                num_length = len(nums[curr])
                for r, c in neighbor_squares(i, j, m, n, num_length):
                    if not lines[r][c].isdigit() and lines[r][c] != ".":
                        matches.append(int(nums[curr]))
                        break
                curr += 1
                j += num_length
            else:
                j += 1
    return matches
            
def neighbor_squares(i: int, j: int, m: int, n: int, num_length) -> list[tuple[int, int]]:
    neighbors = []
    left = max(0, j - 1)
    top = max(0, i - 1)
    right = min(n - 1, j + num_length)
    bottom = min(m - 1, i + 1)
 
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if r == i and c in range(j, j + num_length):
                continue
            neighbors.append((r, c))
    
    return neighbors

def part_one() -> None:
    lines = open("input.txt").read().splitlines()
    matches = find_matches(lines)
    print(sum(matches))
    

# ===== PART 2 ===== #

# separated from find_matches to clarify part 1 vs. part 2
def find_potential_gears(lines: list[list[str]]) -> dict[tuple[int, int], list[int]]:
    m = len(lines)
    n = len(lines[0])
    gears = {}
    for i in range(len(lines)):
        line = lines[i]
        nums = re.findall(num_pattern, line)
        curr = 0
        j = 0
        while j < len(line):
            if line[j].isdigit():
                num_length = len(nums[curr])
                for r, c in neighbor_squares(i, j, m, n, num_length):
                    if lines[r][c] == "*":
                        if (r, c) not in gears:
                            gears[(r, c)] = [int(nums[curr])]
                        else:
                            gears[(r, c)].append(int(nums[curr]))
                curr += 1
                j += num_length
            else:
                j += 1
    return gears

def part_two() -> None:
    lines = open("input.txt").read().splitlines()
    gear_ratios = [(nums[0] * nums[1]) for _, nums in find_potential_gears(lines).items() if len(nums) == 2]
    print(sum(gear_ratios))


# ===== SOLUTIONS ===== # 

if __name__ == "__main__":
    print("===== Part 1 =====")
    part_one()
    print("===== Part 2 =====")
    part_two()