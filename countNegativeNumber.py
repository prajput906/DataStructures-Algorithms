# Python implementation of Naive method to count of
# negative numbers in M[n][m]

def countNegative(M, n, m):
	count = 0

	# Follow the path shown using arrows above
	for i in range(n):
		for j in range(m):

			if M[i][j] < 0:
				count += 1

			else:
				# no more negative numbers in this row
				break
	return count


# Driver code
M = [
	[-3, -2, -1, 1],
	[-2, 2, 3, 4],
	[ 4, 5, 7, 8]
	]
print(countNegative(M, 3, 4))
