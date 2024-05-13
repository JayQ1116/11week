class SizeMismatchException(Exception):
    pass

class Matrix:
    def __init__(self,data):
        self.data=data
        self.rows=len(data)
        self.cols=len(data[0])
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise SizeMismatchException("Matrix size mismatch")

        result = Matrix([[0]*self.cols for _ in range(self.rows)])
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise SizeMismatchException("Matrix size mismatch")
        result = Matrix([[0]*other.cols for _ in range(self.rows)])
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

if __name__ == "__main__":
    A = Matrix([[1, 2],[3, 4],])
    B = Matrix([[3,4],[5,6]])

    C = Matrix([[3,4],[5,6],[1,2]])
    D = Matrix([[3,4,5],[5,6,7]])
    print(A)
    print(A+B)
    print(A*D)
    try:
        print(A+C)
    except Exception as e:
        print(e)
    try:
        print(A*C)
    except Exception as e:
        print(e)