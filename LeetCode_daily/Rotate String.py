def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    return goal in s + s