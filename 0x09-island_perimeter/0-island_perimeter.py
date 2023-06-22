#!/usr/bin/python3

def island_perimeter(grid):

    """

    Calculate the perimeter of an island in a grid.

    Parameters:

    grid (List[List[int]]): A 2D list of integers where 0 represents water, 1 represents land.

    Returns:

    int: The perimeter of the island.

    """

    # Initialize perimeter to 0

    perimeter = 0

    # Iterate over each row in the grid

    for i in range(len(grid)):

        # Iterate over each cell in the row

        for j in range(len(grid[i])):

            # If the cell is land

            if grid[i][j] == 1:

                # Add 4 to the perimeter (since a square has 4 sides)

                perimeter += 4

                # If the cell above is also land, subtract 2 from the perimeter

                if i > 0 and grid[i-1][j] == 1:

                    perimeter -= 1

                # If the cell to the left is also land, subtract 2 from the perimeter

                if j > 0 and grid[i][j-1] == 1:

                    perimeter -= 1

    # Return the calculated perimeter

    return perimeter

