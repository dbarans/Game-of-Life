
MATRIX_SIZE = 100


def check_cell(matrix_in):

 
    matrix_out = [[0 for i in range(MATRIX_SIZE)] for j in range(MATRIX_SIZE)]

  
    
    for index_i, i in enumerate(matrix_in):

        for index_j, j in enumerate(i):
            if index_j == 0 or index_i == 0 or index_i == MATRIX_SIZE - 1 or index_j == MATRIX_SIZE - 1:
                pass
            else:
               
                number_of_adjacent_cells = 0
                if matrix_in[index_i - 1][index_j - 1] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i - 1][index_j] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i - 1][index_j + 1] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i][index_j - 1] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i][index_j + 1] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i + 1][index_j - 1] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i + 1][index_j] == 1:
                    number_of_adjacent_cells += 1
                if matrix_in[index_i + 1][index_j + 1] == 1:
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
