import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds: int) -> str:
    """Format seconds into MM:SS string."""
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"

