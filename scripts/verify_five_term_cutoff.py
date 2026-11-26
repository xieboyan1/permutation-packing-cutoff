"""Verify a counterexample to the five-term cutoff for pattern packings."""

from functools import lru_cache


ALPHA = (1, 2, 3, 6, 7, 10, 11, 14, 17, 20, 4, 5, 8, 9, 12, 13, 15, 16, 18, 19)
BETA = (1, 2, 4, 5, 8, 9, 12, 13, 16, 19, 3, 6, 7, 10, 11, 14, 15, 17, 18, 20)


def packing_count(pattern, overlap, windows):
    """Count assignments of distinct ranks to positions in the given windows."""
    length = len(pattern)
    step = length - overlap
    size = length + (windows - 1) * step
    required_smaller = [0] * size

    for start in range(0, windows * step, step):
        for high, high_rank in enumerate(pattern):
            for low, low_rank in enumerate(pattern):
                if low_rank < high_rank:
                    required_smaller[start + high] |= 1 << (start + low)

    @lru_cache(maxsize=None)
    def count(unassigned):
        if unassigned == 0:
            return 1
        available = unassigned
        total = 0
        while available:
            bit = available & -available
            available ^= bit
            position = bit.bit_length() - 1
            if not (required_smaller[position] & unassigned):
                total += count(unassigned ^ bit)
        return total

    return count((1 << size) - 1)


def main():
    overlap = 10
    for pattern in (ALPHA, BETA):
        assert sorted(pattern) == list(range(1, 21))
        assert list(pattern[:overlap]) == sorted(pattern[:overlap])
        assert list(pattern[-overlap:]) == sorted(pattern[-overlap:])

    alpha_counts = tuple(packing_count(ALPHA, overlap, j) for j in range(1, 7))
    beta_counts = tuple(packing_count(BETA, overlap, j) for j in range(1, 7))
    print("j\talpha\tbeta")
    for j, (a, b) in enumerate(zip(alpha_counts, beta_counts), start=1):
        print(f"{j}\t{a}\t{b}")

    assert alpha_counts == (1, 3, 18, 172, 2313, 36000)
    assert beta_counts == (1, 3, 18, 172, 2313, 38313)


if __name__ == "__main__":
    main()
