"""Print the Collatz sequence starting at 27 and its number of steps (transitions)."""


def collatz(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


if __name__ == "__main__":
    sequence = collatz(27)
    for value in sequence:
        print(value)
    print(f"Total steps: {len(sequence) - 1}")
