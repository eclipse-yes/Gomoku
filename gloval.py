# -*- coding: utf-8 -*-


def init():
    global glodic
    glodic = {}


def setval(name, val):
    glodic[name] = val


def getval(name, defva=None):
    return glodic[name]

