class Solution: 
	def Sudoku(self, board):
		rows = [set() for _ in range(9)]
		cols = [set() for _ in range(9)]
		squares = [set() for _ in range(9)]

		for i in range(9):
			for j in range(9):
				if not board[i][j] == '.':
					rows[i].add(board[i][j])
					cols[j].add(board[i][j])
					squares[(i//3)*3+j//3].add(board[i][j])

		missings = []
		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					existing = rows[i].union(cols[j]).union(squares[(i//3)*3+j//3])
					missing = [str(k) for k in range(1, 10) if not k in existing]
					missings.append(missing)
		self.helper(board, missings)

	def helper(self, board, missings):
		if not missings:
			return True
		missings.sort(key=lambda item: len(item[2]))
		x, y, missing = missings.pop(0)

		if not missing:
			return False

		for curr in missing:
			board[x][y] = curr

			new_missings = [[a, b, c[:] for a, b, c in missings]]
			for i, j, new_missing in new_missings:
				if curr in new_missing and (i==x or j==y or (i//3)*3+j//3 == (x//3)*3+y//3):
					new_missing.remove(curr)
			if self.helper(board, new_missings):
				return True
			board[x][y] = '.'
		return False
