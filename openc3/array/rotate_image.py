"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""
matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]


def rotate_image(matrix):
    for i in range(len(matrix)-1, -1, -1):
        # print(f"{matrix[i]}")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]}")
        #     new_item.append(matrix[i][j])
        # matrix.insert(0, new_item)

    print(f"{matrix}")

if __name__ == "__main__":
    rotate_image(matrix_1)