from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GoRight:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Go Right

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Apply objective test
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Current node, starting from the root
        node = root

        while True:

            # Check if going right is possible
            if "right" not in grid.actions(node.state):
                return NoSolution(reached)

            # Get the successor
            successor = grid.result(node.state, "right")

            # Check if the successor is reached
            if successor in reached:
                continue

            # Initialize the son node
            son = Node(
                "",
                successor,
                cost=node.cost + grid.individual_cost(node.state, "right"),
                parent=node,
                action="right",
            )

            # Mark the successor as reached
            reached[successor] = True

            # Apply objective test
            if grid.objective_test(successor):
                return Solution(son, reached)
            
            # Continue with the son
            node = son

