prob_num = 2

# 初期位置の宣言
i_state = []
# 初期位置1
i_state.append([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 11, 14, None],
                [13, 10, 15, 12]])
# 初期位置2
i_state.append([[2, 10, 3, 4],
                [1, 14, 6, 7],
                [5, None, 11, 8],
                [9, 13, 15, 12]])

# 初期位置3
i_state.append([[14, 3, 6, 4],
                [10, 2, 11, 7],
                [1, 5, 15, 8],
                [9, 13, None, 12]])

# 初期位置4
i_state.append([[14, 3, 11, 6],
                [10, 15, 5, 4],
                [13, 9, 2, 7],
                [1, 12, 8, None]])
init_state = i_state[prob_num - 1]
