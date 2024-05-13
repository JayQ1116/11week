class SizeMismatchException(Exception):
    pass

class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.data=[[0]*cols for _ in range(rows)]
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise SizeMismatchException("Matrix size mismatch")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])