def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2] == 1

matrix = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]