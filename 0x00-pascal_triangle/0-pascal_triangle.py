#!/usr/bin/python3
def pascal_triangle(n):
  # Base case 
  if n <= 0:
    return []

  # Create an empty list
  triangle = []

  # Iterate through rows 
  for row_num in range(n):
    # Initialize the row
    row = [1]

    # Calculate each term of the row
    for i in range(1, row_num):
      row.append(triangle[row_num-1][i-1] + triangle[row_num-1][i])
    
    # Append the last element as 1
    if len(row) != 0:
      row.append(1)
    
    # Append the row to the triangle
    triangle.append(row)

  return triangle

