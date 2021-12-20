# -*- coding: utf-8 -*-


import pygame as pg
import gloval

gloval.init()

"""
打印游戏结束的提示标语坐标 (120,175)
"""


def judge_context(chess_array):  # 黑色白色棋子的索引值列表
    press = (0, 0, 0)
    black_array = chess_array[::2]  # 奇数
    white_array = chess_array[1::2]  # 偶数
    screen = gloval.getval("screen")
    if five_pieces(black_array) == 1:
        # 黑方胜利
        my_font = pg.font.Font("mufont.ttf", 45)
        text2 = my_font.render("黑方胜利", True, press)
        screen.blit(text2, (550, 180))
        game_end()
    if five_pieces(white_array) == 1:
        # 白方胜利
        my_font = pg.font.Font("mufont.ttf", 45)
        text2 = my_font.render("白方胜利", True, press)
        screen.blit(text2, (550, 180))
        game_end()
    if len(chess_array) == 225:
        # 平局
        my_font = pg.font.Font("mufont.ttf", 45)
        text2 = my_font.render("和棋", True, press)
        screen.blit(text2, (550, 180))
        game_end()


def five_pieces(array):
    # 提取最后一颗棋子，负一
    if array:
        x = array[-1][0]
        y = array[-1][1]
        for j in range(1, 12):
            # 竖五连
            if (
                [x, j] in array
                and [x, j + 1] in array
                and [x, j + 2] in array
                and [x, j + 3] in array
                and [x, j + 4] in array
            ):
                return 1
            # 横五连
            if (
                [j, y] in array
                and [j + 1, y] in array
                and [j + 2, y] in array
                and [j + 3, y] in array
                and [j + 4, y] in array
            ):

                return 1
        for j in range(5):
            # \五连

            if (
                [x - j, y - j] in array
                and [x - j + 1, y - j + 1] in array
                and [x - j + 2, y - j + 2] in array
                and [x - j + 3, y - j + 3] in array
                and [x - j + 4, y - j + 4] in array
            ):
                return 1
            # /五连
            if (
                [x - j, y + j] in array
                and [x - j + 1, y + j - 1] in array
                and [x - j + 2, y + j - 2] in array
                and [x - j + 3, y + j - 3] in array
                and [x - j + 4, y + j - 4] in array
            ):

                return 1
        return 0


def game_end():
    gloval.setval("gamestate", 7)

