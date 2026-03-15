from logic_utils import check_guess, get_range_for_difficulty, parse_guess

# --- check_guess tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_easy_mode_range():
    # Easy mode should return the smallest fixed range for beginner difficulty
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)

def test_hard_mode_higher_than_normal():
    # Hard mode is intended to be tougher than Normal, so upper bound must be greater
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert hard_low == 1
    assert hard_high > normal_high

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

# --- Edge case tests ---

def test_negative_number():
    # Negative numbers are valid ints and should still return a hint
    ok, value, err = parse_guess("-5")
    assert ok == True
    assert value == -5

def test_decimal_input():
    # Decimals should be converted to int (3.7 becomes 3)
    ok, value, err = parse_guess("3.7")
    assert ok == True
    assert value == 3

def test_very_large_number():
    # Very large numbers should still parse without crashing
    ok, value, err = parse_guess("99999999")
    assert ok == True
    assert value == 99999999

def test_text_input():
    # Non-numeric text should return False and an error message
    ok, value, err = parse_guess("hello")
    assert ok == False
    assert value is None
    assert err == "That is not a number."

def test_empty_input():
    # Empty string should return False and prompt user to enter a guess
    ok, value, err = parse_guess("")
    assert ok == False
    assert err == "Enter a guess."