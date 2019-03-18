from solver import Solution

sol = Solution()

def test_empty_string():
    assert sol.myAtoi("") == 0

def test_only_minus_sign():
    assert sol.myAtoi("-") == 0

def test_bad_input():
    assert sol.myAtoi("5-1") == 5

def test_integer():
    assert sol.myAtoi("100") == 100

def test_start_with_plus_sign():
    assert sol.myAtoi("+100") == 100

def test_negative_with_space():
    assert sol.myAtoi("   -42") == -42

def test_trailing_words():
    assert sol.myAtoi("4193 with words") == 4193

def test_leading_words():
    assert sol.myAtoi("words and 987") == 0

def test_too_small():
    assert sol.myAtoi("-91283472332") == -(2**31)

def test_too_big():
    assert sol.myAtoi("91283472332") == 2**31 - 1
