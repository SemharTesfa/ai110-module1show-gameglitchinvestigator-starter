from logic_utils import check_guess

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should say to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower()

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should say to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower()

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

from logic_utils import check_guess

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should say to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower()

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should say to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower()

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_handles_string_secret():
    outcome, message = check_guess(9, "10")

    assert outcome == "Too Low"
    assert "higher" in message.lower()