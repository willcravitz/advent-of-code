# ===== PART 1 ===== #

def num_matches(card: str) -> list[int]:
    card, numbers = card.split(":")
    winning, mine = numbers.split("|")
    winning = {int(x) for x in winning.split()}
    mine = {int(x) for x in mine.split()}
    matches = 0
    for num in winning:
        if num in mine:
            matches += 1
            mine.remove(num)
    return matches

def score(card: str) -> int:
    matches = num_matches(card)
    if matches == 0:
        return 0
    else:
        return 2 ** (matches - 1)

def part_one() -> None:
    lines = open("input.txt").read().splitlines()
    scores = [score(card) for card in lines]
    print(sum(scores))
    

# ===== PART 2 ===== #

def get_card_counts(cards: list[str]) -> dict[int, int]:
    card_counts = {}
    for i in range(len(cards)):
        card_counts[i+1] = card_counts.get(i+1, 0) + 1
        matches = num_matches(cards[i])
        for j in range(i+1, i+1+matches):
            if j < len(cards):
                card_counts[j+1] = card_counts.get(j+1, 0) + card_counts[i+1]
    return card_counts
    
def part_two() -> None:
    lines = open("input.txt").read().splitlines()
    card_counts = get_card_counts(lines)
    print(sum(card_counts.values()))
    

# ===== SOLUTIONS ===== # 

if __name__ == "__main__":
    print("===== Part 1 =====")
    part_one()
    print("===== Part 2 =====")
    part_two()