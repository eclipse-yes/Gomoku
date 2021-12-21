# -*- coding: utf-8 -*-


import gloval

gloval.init()
import random


# 常量配置信息 棋盘大小
GOMOKU_SIZE = 9


# 打分表
tuple_score = [None] * 10
tuple_score[0] = 7  # 没有子
tuple_score[1] = 35  # 一个己方子
tuple_score[2] = 800  # 两个己方子
tuple_score[3] = 15000  # 三个己方子
tuple_score[4] = 800000  # 四个己方子
tuple_score[5] = 15  # 一个对方子
tuple_score[6] = 400  # 两个对方子
tuple_score[7] = 8000  # 三个对方子
tuple_score[8] = 100000  # 四个对方子
tuple_score[9] = 0  # 又有白又有黑


# 计算一个空位的分数（需要棋谱数组和空位位置，返回该位置的分数）
def chess_score(array, chess_pos, whiteround):
    pos_score = 0
    x = chess_pos[0]
    y = chess_pos[1]
    black_num = 0
    white_num = 0
    ##竖列
    for i in range(5):  # 1234  统计竖列所有五元组的得分总和
        for j in range(5):  # 01234 统计一个五元组的得分
            if [x - j + i, y] in array[::2]:  # 黑子判断 #横向
                black_num += 1
            if [x - j + i, y] in array[1::2]:  # 白子判断 #横向
                white_num += 1
        pos_score = pos_score + chess_tuple_score(
            black_num, white_num, whiteround
        )  # 计算一个元组
        white_num = 0
        black_num = 0
    ##横列
    for i in range(5):
        for j in range(5):
            if [x, y - j + i] in array[::2]:  # 黑子判断 #横向
                black_num += 1
            if [x, y - j + i] in array[1::2]:  # 白子判断 #横向
                white_num += 1
        pos_score = pos_score + chess_tuple_score(black_num, white_num, whiteround)
        white_num = 0
        black_num = 0
    ##左斜/
    for i in range(5):
        for j in range(5):
            if [x + j - i, y - j + i] in array[::2]:  # 黑子判断 #横向
                black_num += 1
            if [x + j - i, y - j + i] in array[1::2]:  # 白子判断 #横向
                white_num += 1
        pos_score = pos_score + chess_tuple_score(black_num, white_num, whiteround)
        white_num = 0
        black_num = 0
    ##右斜\
    for i in range(5):
        for j in range(5):
            if [x - j + i, y - j + i] in array[::2]:  # 黑子判断 #横向
                black_num += 1
            if [x - j + i, y - j + i] in array[1::2]:  # 白子判断 #横向
                white_num += 1
        pos_score = pos_score + chess_tuple_score(black_num, white_num, whiteround)
        white_num = 0
        black_num = 0
    return pos_score


# 计算每一个五连
def chess_tuple_score(black_num, white_num, whiteround):
    if black_num == 0 and white_num == 0:  # 没有子
        pos_tuple_score = tuple_score[0]
    elif black_num > 0 and white_num > 0:  # 又有白又有黑
        pos_tuple_score = tuple_score[9]
    else:  # 只有黑或者只有白
        if whiteround == -1:
            if black_num != 0:  # 计算横着一格黑子
                pos_tuple_score = tuple_score[black_num]
            if white_num != 0:  # 计算横着一格白子
                pos_tuple_score = tuple_score[white_num + 4]
        if whiteround == 1:
            if black_num != 0:  # 计算横着一格黑子
                pos_tuple_score = tuple_score[black_num + 4]
            if white_num != 0:  # 计算横着一格白子
                pos_tuple_score = tuple_score[white_num]
    return pos_tuple_score


# 寻找棋盘上分数最高的空格,返回bestpos最佳位置
def find_maxscore(array, whiteround):
    if array == []:
        # best_pos = [8, 8]
        best_pos = [5, 5]
    else:
        chess_score_array = []
        for row in range(1, GOMOKU_SIZE):
            for col in range(1, GOMOKU_SIZE):
                chess_pos = [row, col]
                if chess_pos not in array:
                    pos_score = chess_score(array, chess_pos, whiteround)
                    chess_score_array.append([pos_score, row, col])
        chess_score_array.sort(reverse=True)

        # 极限边界情况下 会出现 IndexError 的异常
        try:
            # 随机落子
            if chess_score_array[0][0] - chess_score_array[2][0] < 50:
                choose_pos = random.randint(0, 2)

            elif chess_score_array[0][0] - chess_score_array[1][0] < 100:
                choose_pos = random.randint(0, 1)
            else:
                choose_pos = 0
            pc_pressed_x = chess_score_array[choose_pos][1]
            pc_pressed_y = chess_score_array[choose_pos][2]
            best_pos = [pc_pressed_x, pc_pressed_y]
            # print(best_pos)
            print(chess_score_array)
        except IndexError as e:
            pass  # 不进行任何处理
    return best_pos

