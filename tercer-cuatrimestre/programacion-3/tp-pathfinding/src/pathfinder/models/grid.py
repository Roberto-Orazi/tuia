from src.pathfinder.models.node import Node


class Grid:
    def __init__(
        self, grid: list[list[Node]], initial: tuple[int, int], end: tuple[int, int]
    ) -> None:
        self.grid: list[list[Node]] = grid
        # Initial cell
        self.start = initial
        self.initial = initial
        # End cell
        self.end = end

        # Calculate grid dimensions
        self.width = max(len(row) for row in grid)
        self.height = len(grid)

    def actions(self, pos: tuple[int, int]) -> list[str]:
        """Determine the possible actions from a cell

        Args:
            pos (tuple[int, int]): Cell position

        Returns:
            list[str]: Possible actions
        """
        row, col = pos

        # Map actions with resulting cell positions
        action_pos_mapper = {
            "up": (row - 1, col),
            "down": (row + 1, col),
            "left": (row, col - 1),
            "right": (row, col + 1),
            # "upleft": (row - 1, col - 1),
            # "upright": (row - 1, col + 1),
            # "downleft": (row + 1, col - 1),
            # "downright": (row + 1, col + 1),
        }

        # Determine possilbe actions
        possible_actions = []

        for action, (r, c) in action_pos_mapper.items():
            if not (0 <= r < self.height and 0 <= c < self.width):
                continue

            if self.grid[r][c].value == "#":
                continue

            possible_actions.append(action)

        return possible_actions

    def result(self, pos: tuple[int, int], action: str) -> tuple[int, int]:
        """Get the resulting cell position after performing an action

        Args:
            pos (tuple[int, int]): Cell position
            action (str): Action to perform

        Returns:
            tuple[int, int]: Resulting cell position
        """
        row, col = pos

        match action:
            case "up":
                return (row - 1, col)
            case "down":
                return (row + 1, col)
            case "left":
                return (row, col - 1)
            case "right":
                return (row, col + 1)
            # case "upleft":
            #     return (row - 1, col - 1)
            # case "upright":
            #     return (row - 1, col + 1)
            # case "downleft":
            #     return (row + 1, col - 1)
            # case "downright":
            #     return (row + 1, col + 1)
            case _:
                raise ValueError(f"Invalid action: {action}")

    def objective_test(self, pos: tuple[int, int]) -> bool:
        """Test if the cell is the goal

        Args:
            pos (tuple[int, int]): Cell position

        Returns:
            bool: True if the cell is the goal, False otherwise
        """
        return pos == self.end

    def individual_cost(self, pos: tuple[int, int], action: str) -> int:
        """Get the cost of performing an action from a cell

        Args:
            pos (tuple[int, int]): Cell position
            action (str): Action to perform

        Returns:
            int: Cost of performing the action
        """
        new_pos = self.result(pos, action)
        return self.grid[new_pos[0]][new_pos[1]].cost

    def __repr__(self) -> str:
        return f"Grid([[...], ...], {self.initial}, {self.end})"
