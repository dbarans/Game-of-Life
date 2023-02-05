
MATRIX_SIZE = 100


def check_cell(matrix_in):

 
    matrix_out = [[0 for i in range(MATRIX_SIZE)] for j in range(MATRIX_SIZE)]

    
    
    for index_i, i in enumerate(matrix_in):
        for index_j, j in enumerate(i):

            left = index_j - 1
            middle_width = index_j
            right = index_j + 1
            up = index_i - 1
            down = index_i + 1
            middle_height = index_i 
            
            
            if index_j == 0:
                left = MATRIX_SIZE - 1
            if index_j == MATRIX_SIZE - 1:
                right = 0
            if index_i == 0:
                up = MATRIX_SIZE - 1
            if index_i == MATRIX_SIZE - 1:
                down = 0

            number_of_adjacent_cells = 0
            
            if matrix_in[up][left] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[up][middle_width] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[up][right] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[middle_height][left] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[middle_height][right] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[down][left] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[down][middle_width] == 1:
                number_of_adjacent_cells += 1
            if matrix_in[down][right] == 1:
                number_of_adjacent_cells += 1
            if j == 1:
                if number_of_adjacent_cells == 2 or number_of_adjacent_cells == 3:
                    matrix_out[index_i][index_j] = 1
                else:
                    matrix_out[index_i][index_j] = 0
            else:
                if number_of_adjacent_cells == 3:
                    matrix_out[index_i][index_j] = 1
                else:
                    matrix_out[index_i][index_j] = 0

    return matrix_out
