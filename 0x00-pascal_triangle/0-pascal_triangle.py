#!/usr/bin/python3
def pascal_triangle(n):
  if n <= 0:
    return []

  triangle = []

  for row_num in range(n):
    row = [1]

    for i in range(1, row_num):
      row.append(triangle[row_num-1][i-1] + triangle[row_num-1][i])
    
    if len(row) != 0:
      row.append(1)
    
    triangle.append(row)

  return triangle

