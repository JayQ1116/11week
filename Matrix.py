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
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise SizeMismatchException("Matrix size mismatch")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

if __name__ == "__main__":
    A = Matrix(3, 2)
    A.data = [[1, 2],
              [3, 4],
              [5, 6]]

    B = Matrix(2, 3)
    B.data = [[7, 8, 9],
              [10, 11, 12]]

    C = A * B
    print(C)