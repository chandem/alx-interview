def pascal_triangle(n):
    if n <= 0:
        return []
    # create the first row of the triangle
    row = [1]
    # create a list of lists to store the triangle
    triangle = [row]
    # calculate the rest of the rows
    for i in range(1, n):
        # create a new row
        row = [1]
        # calculate the values in the row
        for j in range(1, i):
            # each value is the sum of the two values above it
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        row.append(1)
        # add the row to the triangle
        triangle.append(row)
    return triangle
