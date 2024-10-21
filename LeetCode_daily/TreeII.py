from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        pq: deque[tuple[int, TreeNode]] = deque()
        pq.append((root.val, root))

        while pq:
            n = len(pq)

            levelSum = 0
            for localSum, node in pq:
                levelSum += node.val

            for _ in range(n):
                localSum, node = pq.popleft()

                childSum = 0
                if node.left:
                    childSum += node.left.val
                if node.right:
                    childSum += node.right.val

                if node.left:
                    pq.append((childSum, node.left))
                if node.right:
                    pq.append((childSum, node.right))

                node.val = levelSum - localSum

        return root


def main() -> None:
    # Create the tree:
    #      5
    #     / \
    #    4   9
    #   / \ / \
    #  1  3 2  6

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(6)

    solution = Solution()
    result = solution.replaceValueInTree(root)

    def print_level_order(node: Optional[TreeNode]) -> None:
        if not node:
            return

        queue: deque[TreeNode] = deque([node])
        values: List[int] = []

        while queue:
            current = queue.popleft()
            values.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print("Result:", values)

    print_level_order(result)


if __name__ == "__main__":
    main()
