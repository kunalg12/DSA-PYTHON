class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal (if not, impossible to be rotation)
        if len(s) != len(goal):
            return False

        # Create doubled string that contains all rotations
        doubled_s = s + s
        # Check if goal exists in doubled string
        return goal in doubled_s