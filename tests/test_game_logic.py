from logic_utils import check_guess


def _hint_message(outcome):
    """Mirror the hint mapping used in app.py."""
    # FIX: Swapped hint messages to match the correct logic after fixing the bug in check_guess to make the hint message consistent with the actual outcome of the guess.
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    return "📈 Go HIGHER!"


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Hint-message tests (the bug was reversed hints) ---

def test_hint_correct_on_win():
    outcome = check_guess(50, 50)
    assert _hint_message(outcome) == "🎉 Correct!"

def test_hint_go_lower_when_guess_too_high():
    outcome = check_guess(75, 50)
    assert _hint_message(outcome) == "📉 Go LOWER!"

def test_hint_go_higher_when_guess_too_low():
    outcome = check_guess(25, 50)
    assert _hint_message(outcome) == "📈 Go HIGHER!"

def test_hint_one_above_secret():
    outcome = check_guess(51, 50)
    assert _hint_message(outcome) == "📉 Go LOWER!"

def test_hint_one_below_secret():
    outcome = check_guess(49, 50)
    assert _hint_message(outcome) == "📈 Go HIGHER!"

def test_hint_not_reversed_high():
    """Ensure a high guess does NOT show 'Go HIGHER!' (the old bug)."""
    outcome = check_guess(90, 50)
    assert _hint_message(outcome) != "📈 Go HIGHER!"

def test_hint_not_reversed_low():
    """Ensure a low guess does NOT show 'Go LOWER!' (the old bug)."""
    outcome = check_guess(10, 50)
    assert _hint_message(outcome) != "📉 Go LOWER!"
