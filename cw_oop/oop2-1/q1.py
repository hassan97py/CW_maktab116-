class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            # print(i)
            for j in range(other.cols):
                # print(j)
                for k in range(self.cols):
                    # print(k)
                    # print(result.data[i][j])
                    # print(self.data[i][k])
                    # print(other.data[k][j])
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
                    # print(result.data[i][j])
        return result

    def __str__(self):
        result = ""
        for row in self.data:
            result += " | " + ", ".join(f"{x:6}" for x in row) + " |\n"
            # result += " " .join( x for x in row)
        
         
        return result


a=Matrix(2,3,[[1,2,3],[5,6,7]])
b=Matrix(3,2,[[1,2],[5,6],[8 ,9]])
# b=Matrix(2,3)
print(a)
print(b)
print(a*b)


# A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
# B = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])

# C = A + B
# print("A + B:\n", C)

# D = A - B
# print("A - B:\n", D)

# E = A * B
# print("A * B:\n", E)

# [[0 for _ in range(cols)] for _ in range(rows)]
# for i in range(rews):
#     for i in range(cols):
#         return 0