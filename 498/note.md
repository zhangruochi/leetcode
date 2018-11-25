## 思路

1. scan  row*col-1
2. even index: up right
    - x = i if i < rows else rows - 1
    - y = 0 if i < rows else i - (row - 1)

3. odd index: down left
    - x = 0 if i < cols else i - (cols - 1)
    - y = i if i < cols else cols  - 1