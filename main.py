# -*- coding: utf-8 -*-


import pygame as pg

# 用exit来退出程序
from sys import exit
import gloval

gloval.init()
import windows as wd
import menu
import judger
import easy_pc


# 配置相关全局常量
GOMOKU_SIZE = 9
CHESS_SIZE = 50
CHESS_BOARD_SIZE = 480

# 棋盘配置: 9X9棋盘下的配置信息
# (1，1)的实际坐标为(40，40)，(9，9)的实际坐标为(440, 440),有14个间隔


def drawbg():
    """画背景"""
    screen.blit(imBackground, (0, 0))
    global chessboard_start_x
    global chessboard_start_y
    chessboard_start_x = 55
    chessboard_start_y = 85
    screen.blit(imChessboard, (chessboard_start_x, chessboard_start_y))

    screen.blit(gloval.getval("imLogo"), (570, 20))
    screen.blit(gloval.getval("imLabel"), (230, 20))


def drawmenu():
    """画菜单"""
    if gamestate == 1:
        menu.menu1()  # 画’开始游戏‘，‘游戏说明’，’结束游戏‘按钮
    elif gamestate == 2:
        menu.menu2()  # 画 ‘人机对战’，‘双人对战’，'返回上级菜单',‘结束游戏’
    elif gamestate == 3:
        menu.menu3()  # 画 ‘玩家先手’，‘电脑先手’，'返回上级菜单',‘结束游戏’
    elif gamestate == 4 or gamestate == 5 or gamestate == 6:
        menu.menu4()  # 画‘悔棋’，‘重新开始’，‘结束游戏’按钮
    elif gamestate == 7:
        menu.menu7()  # 画‘重新开始’，‘结束游戏’按钮


def drawmove():
    """画鼠标移动的相关效果"""
    gloval.setval("mouse_x", pg.mouse.get_pos()[0])  # 鼠标的坐标
    gloval.setval("mouse_y", pg.mouse.get_pos()[1])
    mouse_x, mouse_y = pg.mouse.get_pos()  # 棋子跟随鼠标移动
    if (
        chessboard_start_x < mouse_x < chessboard_start_x + CHESS_BOARD_SIZE
        and chessboard_start_y < mouse_y < chessboard_start_y + CHESS_BOARD_SIZE
        and (gamestate == 4 or gamestate == 5 or gamestate == 6)
    ):
        if whiteround[chess_num] == 1:
            screen.blit(
                imWhitePiece, (mouse_x - CHESS_SIZE / 2, mouse_y - CHESS_SIZE / 2)
            )
        else:
            screen.blit(
                imBlackPiece, (mouse_x - CHESS_SIZE / 2, mouse_y - CHESS_SIZE / 2)
            )
    elif gamestate == 1:
        menu.movemenu1()
    elif gamestate == 2:
        menu.movemenu2()
    elif gamestate == 3:
        menu.movemenu3()
    elif gamestate == 4 or gamestate == 5 or gamestate == 6:
        menu.movemenu4()
    elif gamestate == 7:
        menu.movemenu7()


def drawpress():
    """鼠标事件 按键情况"""

    global whiteround
    global chess_array
    global d
    global chess_num
    global piece_x, piece_y, piece
    press_intro = gloval.getval("press_intro")
    press_regret = gloval.getval("press_regret")
    # d = (518-22)/14  			 	#(1，1)的实际坐标为(22，22)，(15，15)的实际坐标为(518，518),有14个间隔
    d = (440 - 40) / 8  # (1，1)的实际坐标为(40, 40)，(9，9)的实际坐标为(440，440),有8个间隔
    for event in pg.event.get():  # 获取鼠标点击事件
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            gloval.setval("pressed_x", event.pos[0])
            gloval.setval("pressed_y", event.pos[1])
            pressed_x, pressed_y = event.pos[0], event.pos[1]
            # 第一种情况，人人对战
            if (
                chessboard_start_x < pressed_x < chessboard_start_x + CHESS_BOARD_SIZE
                and chessboard_start_y
                < pressed_y
                < chessboard_start_y + CHESS_BOARD_SIZE
                and gamestate == 4
            ):
                player_pos_chess(pressed_x, pressed_y)
            # 第二种情况，玩家先手
            elif (
                chessboard_start_x < pressed_x < chessboard_start_x + CHESS_BOARD_SIZE
                and chessboard_start_y
                < pressed_y
                < chessboard_start_y + CHESS_BOARD_SIZE
                and gamestate == 5
            ):
                ifem = player_pos_chess(pressed_x, pressed_y)  # 玩家下棋
                if ifem != False:
                    pc_pos_chess()  # 电脑下棋
            # 第三种情况，电脑先手
            elif (
                chessboard_start_x < pressed_x < chessboard_start_x + CHESS_BOARD_SIZE
                and chessboard_start_y
                < pressed_y
                < chessboard_start_y + CHESS_BOARD_SIZE
                and gamestate == 6
            ):

                ifem = player_pos_chess(pressed_x, pressed_y)  # 玩家下棋
                if ifem != False:

                    pc_pos_chess()  # 电脑下棋
            # 第四种情况，点击菜单

            else:
                if gamestate == 1:
                    menu.pressmenu1()
                elif gamestate == 2:
                    menu.pressmenu2()
                elif gamestate == 3:
                    if 6 == menu.pressmenu3():
                        pc_pos_chess()
                elif gamestate == 4 or gamestate == 5 or gamestate == 6:
                    menu.pressmenu4()
                elif gamestate == 7:
                    menu.pressmenu7()
    restart = gloval.getval("restart")  # 是否重启游戏
    if chess_array:  # 画棋子和棋子上面的数字不为空，有落子
        draw_chess(chess_num, whiteround)  # 画棋子和上面的数字
    if press_intro == 1:  # 游戏简介信息
        draw_intro_text()
    if press_regret == 1:  # 悔棋
        regret()
    draw_chesscross(chess_num)  # 最后一个落子位置


def draw_intro_text():
    """游戏简介信息"""
    my_font = pg.font.Font("mufont.ttf", 25)
    my_font_color = (106, 90, 205)
    text1 = my_font.render("双方分别使用黑白两色的棋子，", True, my_font_color)
    text2 = my_font.render("下在棋盘直线与横线的交叉点上，", True, my_font_color)
    text3 = my_font.render("先形成五子连线者获胜。", True, my_font_color)
    # screen.blit(text1,(640,100))
    # screen.blit(text2,(640,140))
    # screen.blit(text3,(640,180))
    screen.blit(text1, (120, 175))
    screen.blit(text2, (120, 215))
    screen.blit(text3, (120, 255))


def regret():
    """悔棋"""
    global chess_num, chess_array, piece_y, piece_x, piece, whiteround
    if chess_num != 0:  # 删除所有储存的数组
        if gamestate == 4:
            del chess_array[-1]
            del piece_x[-1]
            del piece_y[-1]
            del piece[-1]
            del whiteround[-1]
            chess_num = chess_num - 1
        if gamestate == 5 or gamestate == 6:
            del chess_array[-1]
            del chess_array[-1]
            del piece_x[-1]
            del piece_y[-1]
            del piece_x[-1]
            del piece_y[-1]
            del piece[-1]
            del piece[-1]
            del whiteround[-1]
            del whiteround[-1]
            chess_num = chess_num - 2
    gloval.setval("press_regret", 0)


def draw_chess(chess_num, whiteround):
    """画棋子上面的数字"""
    my_font = pg.font.Font("mufont.ttf", 18)
    for i in range(chess_num):

        if whiteround[i] == -1:  # 黑子
            screen.blit(
                imBlackPiece, (piece_x[i] - CHESS_SIZE / 2, piece_y[i] - CHESS_SIZE / 2)
            )
            text_w = my_font.render(str(i + 1), True, (255, 255, 255))
            screen.blit(text_w, (piece_x[i] - 7, piece_y[i] - 12))
        else:  # 白子
            screen.blit(
                imWhitePiece, (piece_x[i] - CHESS_SIZE / 2, piece_y[i] - CHESS_SIZE / 2)
            )
            text_b = my_font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(text_b, (piece_x[i] - 7, piece_y[i] - 12))


def draw_chesscross(chess_num):
    """画最后一个落子的位置"""
    if chess_num != 0:
        pg.draw.rect(
            screen,
            button,
            [
                int(piece_x[chess_num - 1] - CHESS_SIZE / 2),
                int(piece_y[chess_num - 1] - CHESS_SIZE / 2),
                48,
                48,
            ],
            2,
        )


def array2index(array):
    """二维坐标转一维索引值"""
    return (array[0] - 1) * GOMOKU_SIZE + array[1]

    ##一维索引值转二维坐标


def index2array(index):
    i, j = (
        int((index - index % GOMOKU_SIZE) / GOMOKU_SIZE + 1),
        int(index % GOMOKU_SIZE),
    )
    if j == 0:
        i -= 1
        j = GOMOKU_SIZE
    return i, j

    ##二维坐标转化为棋盘内的真实坐标（计算棋子在棋盘中的位置）（计算棋子的实际位置）


def getrealpos(array):
    # piece_chessboard_x,piece_chessboard_y = 22+(array[1]-1)*d,22+(array[0]-1)*d
    piece_chessboard_x, piece_chessboard_y = (
        40 + (array[1] - 1) * d,
        40 + (array[0] - 1) * d,
    )
    piece_x, piece_y = (
        piece_chessboard_x + chessboard_start_x,
        piece_chessboard_y + chessboard_start_y,
    )
    return piece_x, piece_y

    ##得到棋盘上棋子的数组位置


def getpos(pressed_x, pressed_y):
    mouse_chessboard_x = pressed_x - chessboard_start_x  # 鼠标在棋盘中的坐标
    mouse_chessboard_y = pressed_y - chessboard_start_y
    # i_tmp = round((mouse_chessboard_y-22)/d)+1	# 计算鼠标最接近的格点
    # j_tmp = round((mouse_chessboard_x-22)/d)+1
    i_tmp = round((mouse_chessboard_y - 40) / d) + 1  # 计算鼠标最接近的格点
    j_tmp = round((mouse_chessboard_x - 40) / d) + 1
    if i_tmp in range(1, 10) and j_tmp in range(1, 10):  # 1到9判断标号是否有效
        chess_i = i_tmp
        chess_j = j_tmp
        return chess_i, chess_j
    ##判断是否为空


def if_isempty(i, j):
    if [i, j] not in piece:
        return True
    else:
        return False


def player_pos_chess(pressed_x, pressed_y):
    global whiteround
    global chess_array
    global chess_num
    global piece_x, piece_y, piece

    try:
        # 当用户点击在棋盘之外的地方时会发生bug, catch it
        chess_array.append(list(getpos(pressed_x, pressed_y)))  # 记录位置，黑棋白棋数组交替
        piece_i, piece_j = getrealpos(chess_array[chess_num])  # 已处理的位置
        isempty = if_isempty(piece_i, piece_j)

        if isempty == True:  # 如果这个地方没有棋子
            whiteround.append(-whiteround[chess_num])
            piece_x.append(piece_i)
            piece_y.append(piece_j)
            piece.append([piece_i, piece_j])
            chess_num += 1
            gloval.setval("chess_array", chess_array)
            return 1
        else:  # 	如果这个地方有棋子
            del chess_array[chess_num]  # 删除那个重复的数组
            return 0
    except TypeError as e:
        # 当用户点击不符合要求的地方时 不进行任何的打印或者输出操作
        pass


def pc_pos_chess():
    global whiteround
    global chess_array
    global chess_num
    global piece_x, piece_y, piece
    pc_pressed = easy_pc.find_maxscore(chess_array, whiteround[-1])
    chess_array.append(pc_pressed)  # 记录电脑下棋位置
    piece_i, piece_j = getrealpos(chess_array[chess_num])  # 已处理的位置
    isempty = if_isempty(piece_i, piece_j)
    print(isempty)
    if isempty == True:  # 如果这个地方没有棋子
        whiteround.append(-whiteround[chess_num])
        piece_x.append(piece_i)
        piece_y.append(piece_j)
        piece.append([piece_i, piece_j])
        chess_num += 1
        gloval.setval("chess_array", chess_array)
    else:  # 	如果这个地方有棋子
        del chess_array[chess_num]  # 删除那个重复的数组


def main():
    # 初始化pygame 加载资源
    wd.windows()
    # 设置默认光标样式
    pg.mouse.set_cursor(*pg.cursors.arrow)
    gloval.setval("restart", 0)
    global restart

    restart = gloval.getval("restart")
    gloval.setval("press_intro", 0)
    gloval.setval("press_regret", 0)
    global gamestate  # 游戏状态信息，1为主菜单，2为人机和人人对战选择菜单，3为人机对战先后手选择菜单，456为对战菜单，7为结束游戏菜单
    gamestate = 1
    gloval.setval("gamestate", 1)
    global press, button
    press = (0, 0, 0)

    button = (132, 71, 34)
    global screen
    screen = gloval.getval("screen")
    global imBackground
    imBackground = gloval.getval("imBackground")
    global imChessboard
    imChessboard = gloval.getval("imChessboard")
    global imBlackPiece
    imBlackPiece = gloval.getval("imBlackPiece")
    global imWhitePiece
    imWhitePiece = gloval.getval("imWhitePiece")
    global whiteround  # 回合，黑子先走，whiteround为-1
    whiteround = [-1]
    global chess_array  # 储存双方落子信息，0246先手，1357后手
    chess_array = []
    global chess_num
    chess_num = 0
    global piece_x, piece_y, piece
    FPS = 60
    piece_x = []
    piece_y = []
    piece = []

    while restart == 0:
        # 刷新gamestate
        gamestate = gloval.getval("gamestate")
        # 画背景，左上角是坐标
        drawbg()
        # 画菜单
        drawmenu()
        # 鼠标事件按键情况
        drawpress()
        # 画鼠标移动的相关效果
        drawmove()
        # 判断是否赢棋
        judger.judge_context(chess_array)
        # 刷新画面
        pg.display.update()
        # 调整游戏帧数
        FPSClock = pg.time.Clock()
        FPSClock.tick(FPS)
        restart = gloval.getval("restart")


if __name__ == "__main__":
    while True:
        main()
