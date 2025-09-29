class Solution(object):
    def searchMatrix(self, matrix, target, index=0):
        if index == len(matrix):
            return False
        if matrix[index][0] <= target and matrix[index][-1] >= target:
            for i in matrix[index]:
                if i == target:
                    return True
            return False
        else:
            return self.searchMatrix(matrix, target, index + 1)

