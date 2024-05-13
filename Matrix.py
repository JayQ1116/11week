class SizeMismatchException(Exception):
    pass

class Matrix:
    def __init__(self,rows,cols,data):
        self.rows=rows
        self.cols=cols
        self.data=[[0]*cols for _ in range(rows)]