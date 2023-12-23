# ===== PART 1 ===== #

def get_first_digit(code: str) -> str:
    for char in code:
        if char.isdigit():
            return char

def get_last_digit(code: str) -> str:
    for char in code[::-1]:
        if char.isdigit():
            return char
        
def calibration_code(code: str) -> int:
    digit1 = get_first_digit(code)
    digit2 = get_last_digit(code)
    return int(digit1 + digit2)

def part_one() -> None:
    codes = open("input.txt").read().splitlines()
    calibrations = [calibration_code(code) for code in codes]
    print(sum(calibrations))
    

# ===== PART 2 ===== #

number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

def get_first_num(code: str) -> str:
    for i in range(len(code)):
        if code[i].isdigit():
            return code[i]
        for key, value in number_words.items():
            if code[i:].startswith(key):
                return str(value)
    return code

def get_last_num(code: str) -> str:
    for i in range(len(code) - 1, -1, -1):
        if code[i].isdigit():
            return code[i]
        for key, value in number_words.items():
            if code[i:].startswith(key):
                return str(value)
    return code

def calibration_code_with_words(code: str) -> int:
    digit1 = get_first_num(code)
    digit2 = get_last_num(code)
    return int(digit1 + digit2)

def part_two() -> None:
    codes = open("input.txt").read().splitlines()
    calibrations = [calibration_code_with_words(code) for code in codes]
    print(sum(calibrations))


# ===== SOLUTIONS ===== # 
    
if __name__ == "__main__":
    print("===== Part 1 =====")
    part_one()
    print("===== Part 2 =====")
    part_two()