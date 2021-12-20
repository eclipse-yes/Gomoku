# -*- coding: utf-8 -*-
# author: eclipse


import pygame as pg
import gloval

gloval.init()


def windows():
    # 初始化pygame
    pg.init()
    # 加载背景图片 棋盘图片 黑白子图片 logo图片 label标题图片
    gloval.setval("screen", pg.display.set_mode((750, 600), 0, 32))  # 分辨率，标志位，色深
    gloval.setval("imBackground", pg.image.load("background.png").convert())
    gloval.setval("imChessboard", pg.image.load("chessboard.png").convert())
    gloval.setval("imBlackPiece", pg.image.load("chessblack.png").convert_alpha())
    gloval.setval("imWhitePiece", pg.image.load("chesswhite.png").convert_alpha())

    gloval.setval("imLogo", pg.image.load("logo.png"))
    gloval.setval("imLabel", pg.image.load("toplabel.png"))
    # 设置窗口标题
    pg.display.set_caption("调参侠的五子棋大乱斗之勇者无畏")  # 设置窗口标题

