def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

#FIX: Refactored logic into logic_utils.py using Copilot Agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    Returns: "Win", "Too High", or "Too Low"
    """
    #FIX: Fixed hint bug by using int() conversion for numeric comparison instead of string comparison using claude to ensure correct logic for "Too High" and "Too Low" outcomes.
    guess_int = int(guess)
    secret_int = int(secret)


    if guess_int == secret_int:
        return "Win"
    if guess_int > secret_int:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
