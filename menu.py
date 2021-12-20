# -*- coding: utf-8 -*-

import pygame as pg
from sys import exit

# import easygui
from windows import *
import gloval

gloval.init()


# 颜色配置
press = (0, 0, 0)  # 当用户按压后 变成黑色
button = (132, 71, 34)  # button的颜色 棕色

# 常量
# For Menu who has three buttons like Menu1:
BUTTON_LEFT_POS = 570
BUTTON_TOP_POS = 185

BUTTON_LENGTH = 160
BUTTON_LENGTH2 = 224
BUTTON_LENGTH3 = 96
BUTTON_HEIGHT = 70

MENU1_BUTTON2_TOP = 335
MENU_LAST_BUTTON_TOP = 480

(MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS) = (580, 195)
(MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS) = (580, 345)
(MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS) = (580, 490)

(MENU2_TEXTAREA2_LEFT_POS, MENU2_TEXTAREA2_TOP_POS) = (580, 295)
(MENU2_TEXTAREA3_LEFT_POS, MENU2_TEXTAREA3_TOP_POS) = (580, 395)

# For Menu who has four buttons like Menu2:
MENU2_BUTTON2_TOP = 285
MENU2_BUTTON3_TOP = 385

########## 对于需要组合计算的配置
# 340 = BUTTON_TOP_POS + BUTTON_HEIGHT
# 870 = BUTTON_LEFT_POS + BUTTON_LENGTH
# 490 = MENU1_BUTTON2_TOP +
# 640 = MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
# 440 = MENU2_BUTTON2_TOP + BUTTON_HEIGHT
# 950 = BUTTON_LEFT_POS + BUTTON_LENGTH2
# 540 = MENU2_BUTTON3_TOP + BUTTON_HEIGHT

# For Font:
FONT_SIZE = 35


def menu1():
    screen = gloval.getval("screen")

    # 画’开始游戏‘，‘游戏说明’，’结束游戏‘按钮
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU1_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )

    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    text1 = my_font.render("开始游戏", True, button)
    text2 = my_font.render("游戏说明", True, button)
    text3 = my_font.render("结束游戏", True, button)
    screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    screen.blit(text2, (MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS))
    screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))


def movemenu1():
    mouse_x = gloval.getval("mouse_x")
    mouse_y = gloval.getval("mouse_y")
    screen = gloval.getval("screen")
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)

    if (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and BUTTON_TOP_POS < mouse_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)
        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text1 = my_font.render("开始游戏", True, press)

        screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU1_BUTTON2_TOP < mouse_y < MENU1_BUTTON2_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU1_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("游戏说明", True, press)
        screen.blit(
            text2, (MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS)
        )
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < mouse_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text3 = my_font.render("结束游戏", True, press)
        screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))
    else:
        pg.mouse.set_cursor(*pg.cursors.arrow)


def pressmenu1():
    screen = gloval.getval("screen")
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    pressed_x = gloval.getval("pressed_x")
    pressed_y = gloval.getval("pressed_y")
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and BUTTON_TOP_POS < pressed_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):  # 开始游戏，进入菜单2
        gloval.setval("gamestate", 2)
        gloval.setval("press_intro", 0)

    elif (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU1_BUTTON2_TOP < pressed_y < MENU1_BUTTON2_TOP + BUTTON_HEIGHT
    ):  # 游戏介绍
        gloval.setval("press_intro", 1)
    elif (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < pressed_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):  # 退出游戏
        pg.quit()
        exit()
    else:
        gloval.setval("press_intro", 0)


def menu2():  # 画 ‘人机对战’，‘双人对战’，'返回上级',‘结束游戏’
    screen = gloval.getval("screen")

    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU2_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU2_BUTTON3_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )

    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    text1 = my_font.render("人机对战", True, button)
    text2 = my_font.render("双人对战", True, button)
    text3 = my_font.render("返回上级", True, button)
    text4 = my_font.render("结束游戏", True, button)

    screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    screen.blit(text2, (MENU2_TEXTAREA2_LEFT_POS, MENU2_TEXTAREA2_TOP_POS))
    screen.blit(text3, (MENU2_TEXTAREA3_LEFT_POS, MENU2_TEXTAREA3_TOP_POS))
    screen.blit(text4, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))


def movemenu2():
    mouse_x = gloval.getval("mouse_x")
    mouse_y = gloval.getval("mouse_y")
    screen = gloval.getval("screen")
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)

    if (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and BUTTON_TOP_POS < mouse_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text1 = my_font.render("人机对战", True, press)
        screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU2_BUTTON2_TOP < mouse_y < MENU2_BUTTON2_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU2_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("双人对战", True, press)
        screen.blit(text2, (MENU2_TEXTAREA2_LEFT_POS, MENU2_TEXTAREA2_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU2_BUTTON3_TOP < mouse_y < MENU2_BUTTON3_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)
        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU2_BUTTON3_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("返回上级", True, press)
        screen.blit(text2, (MENU2_TEXTAREA3_LEFT_POS, MENU2_TEXTAREA3_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < mouse_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text3 = my_font.render("结束游戏", True, press)
        screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))
    else:
        pg.mouse.set_cursor(*pg.cursors.arrow)


def pressmenu2():
    pressed_x = gloval.getval("pressed_x")
    pressed_y = gloval.getval("pressed_y")
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and BUTTON_TOP_POS < pressed_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):  # 进入 人机对战界面
        gloval.setval("gamestate", 3)  #

    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU2_BUTTON2_TOP < pressed_y < MENU2_BUTTON2_TOP + BUTTON_HEIGHT
    ):  # 进入 玩家对战界面
        gloval.setval("gamestate", 4)

    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH2
        and MENU2_BUTTON3_TOP < pressed_y < MENU2_BUTTON3_TOP + BUTTON_HEIGHT
    ):  # 返回上级，即返回最初级菜单
        gloval.setval("gamestate", 1)
    elif (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < pressed_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.quit()
        exit()


def menu3():
    # 画 ‘玩家先手’，‘电脑先手’，'返回上级',‘结束游戏’
    screen = gloval.getval("screen")
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU2_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU2_BUTTON3_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )

    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    text1 = my_font.render("玩家先手", True, button)
    text2 = my_font.render("电脑先手", True, button)
    text3 = my_font.render("返回上级", True, button)
    text4 = my_font.render("结束游戏", True, button)

    screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    screen.blit(text2, (MENU2_TEXTAREA2_LEFT_POS, MENU2_TEXTAREA2_TOP_POS))
    screen.blit(text3, (MENU2_TEXTAREA3_LEFT_POS, MENU2_TEXTAREA3_TOP_POS))
    screen.blit(text4, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))


def movemenu3():
    mouse_x = gloval.getval("mouse_x")
    mouse_y = gloval.getval("mouse_y")
    screen = gloval.getval("screen")
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)

    if (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and BUTTON_TOP_POS < mouse_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text1 = my_font.render("玩家先手", True, press)
        screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU2_BUTTON2_TOP < mouse_y < MENU2_BUTTON2_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU2_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("电脑先手", True, press)
        screen.blit(text2, (MENU2_TEXTAREA2_LEFT_POS, MENU2_TEXTAREA2_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH2
        and MENU2_BUTTON3_TOP < mouse_y < MENU2_BUTTON3_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU2_BUTTON3_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("返回上级", True, press)
        screen.blit(text2, (MENU2_TEXTAREA3_LEFT_POS, MENU2_TEXTAREA3_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < mouse_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text3 = my_font.render("结束游戏", True, press)
        screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))
    else:
        pg.mouse.set_cursor(*pg.cursors.arrow)


def pressmenu3():  # 人机对战选择先后手的菜单
    pressed_x = gloval.getval("pressed_x")
    pressed_y = gloval.getval("pressed_y")
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and BUTTON_TOP_POS < pressed_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):  # 玩家先手
        gloval.setval("gamestate", 5)
        return 1
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU2_BUTTON2_TOP < pressed_y < MENU2_BUTTON2_TOP + BUTTON_HEIGHT
    ):  # 电脑先手
        gloval.setval("gamestate", 6)
        return 6
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH2
        and MENU2_BUTTON3_TOP < pressed_y < MENU2_BUTTON3_TOP + BUTTON_HEIGHT
    ):
        gloval.setval("gamestate", 2)
        return 1
    elif (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < pressed_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.quit()
        exit()


def menu4():
    # 画‘悔棋’，‘重新开始’，‘退出’按钮
    screen = gloval.getval("screen")
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH3, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU1_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    text1 = my_font.render("悔棋", True, button)
    text2 = my_font.render("重新开始", True, button)
    text3 = my_font.render("结束游戏", True, button)
    screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    screen.blit(text2, (MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS))
    screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))


def movemenu4():
    mouse_x = gloval.getval("mouse_x")
    mouse_y = gloval.getval("mouse_y")
    screen = gloval.getval("screen")
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)

    if (
        BUTTON_LEFT_POS < mouse_x < 790
        and BUTTON_TOP_POS < mouse_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, BUTTON_TOP_POS, BUTTON_LENGTH3, BUTTON_HEIGHT],
            5,
        )
        text1 = my_font.render("悔棋", True, press)

        screen.blit(text1, (MENU_FIRST_TEXTAREA_LEFT_POS, MENU_FIRST_TEXTAREA_TOP_POS))
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU1_BUTTON2_TOP < mouse_y < MENU1_BUTTON2_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU1_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("重新开始", True, press)
        screen.blit(
            text2, (MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS)
        )
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < mouse_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)

        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text3 = my_font.render("结束游戏", True, press)
        screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))
    else:
        pg.mouse.set_cursor(*pg.cursors.arrow)


def pressmenu4():
    pressed_x = gloval.getval("pressed_x")
    pressed_y = gloval.getval("pressed_y")
    if (
        BUTTON_LEFT_POS < pressed_x < 790
        and BUTTON_TOP_POS < pressed_y < BUTTON_TOP_POS + BUTTON_HEIGHT
    ):  # 悔棋
        gloval.setval("press_regret", 1)
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU1_BUTTON2_TOP < pressed_y < MENU1_BUTTON2_TOP + BUTTON_HEIGHT
    ):  # 重新开始，且回到菜单1
        gloval.setval("gamestate", 1)
        gloval.setval("restart", 1)
    elif (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < pressed_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):  # 退出游戏
        pg.quit()
        exit()


def menu7():
    # 画‘重新开始’，‘退出’按钮
    screen = gloval.getval("screen")
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU1_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    pg.draw.rect(
        screen,
        button,
        [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
        5,
    )
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    text2 = my_font.render("重新开始", True, button)
    text3 = my_font.render("结束游戏", True, button)
    screen.blit(text2, (MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS))
    screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))


def movemenu7():
    mouse_x = gloval.getval("mouse_x")
    mouse_y = gloval.getval("mouse_y")
    screen = gloval.getval("screen")
    my_font = pg.font.Font("mufont.ttf", FONT_SIZE)
    if (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU1_BUTTON2_TOP < mouse_y < MENU1_BUTTON2_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)
        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU1_BUTTON2_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text2 = my_font.render("重新开始", True, press)
        screen.blit(
            text2, (MENU1_SECOND_TEXTAREA_LEFT_POS, MENU1_SECOND_TEXTAREA_TOP_POS)
        )
    elif (
        BUTTON_LEFT_POS < mouse_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < mouse_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):
        pg.mouse.set_cursor(*pg.cursors.broken_x)
        pg.draw.rect(
            screen,
            press,
            [BUTTON_LEFT_POS, MENU_LAST_BUTTON_TOP, BUTTON_LENGTH, BUTTON_HEIGHT],
            5,
        )
        text3 = my_font.render("结束游戏", True, press)
        screen.blit(text3, (MENU_LAST_TEXTAREA_LEFT_POS, MENU_LAST_TEXTAREA_TOP_POS))
    else:
        pg.mouse.set_cursor(*pg.cursors.arrow)


def pressmenu7():
    pressed_x = gloval.getval("pressed_x")
    pressed_y = gloval.getval("pressed_y")
    if (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU1_BUTTON2_TOP < pressed_y < MENU1_BUTTON2_TOP + BUTTON_HEIGHT
    ):  # 重新开始，且回到菜单1
        gloval.setval("gamestate", 1)
        gloval.setval("restart", 1)
    elif (
        BUTTON_LEFT_POS < pressed_x < BUTTON_LEFT_POS + BUTTON_LENGTH
        and MENU_LAST_BUTTON_TOP < pressed_y < MENU_LAST_BUTTON_TOP + BUTTON_HEIGHT
    ):  # 退出游戏
        pg.quit()
        exit()

