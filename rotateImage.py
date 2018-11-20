class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l1, l2 = len(matrix), len(matrix[0])
        for i in range(l1):
        	for j in range(i+1, l2):
        		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        start, end = 0, l2-1
        while start < end:
        	for i in range(l1):
        		matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
        	start += 1
        	end -= 1


Solution().rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
