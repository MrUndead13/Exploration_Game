import curses
from curses import wrapper
import time
from maps import *

def print_map(map, stdscr):
    CYAN = curses.color_pair(1)

    for i, row in enumerate(map):
        for j, value in enumerate(row):
            stdscr.addstr(i,j*2,value, CYAN)

def moving(map, position, direction):
    if direction=="UP":
        if position[0]>0:
            if map[position[0]-1][position[1]]!="#":
                map[position[0]][position[1]]=" "
                map[position[0]-1][position[1]]="C"
                position=(position[0]-1,position[1])
    elif direction=="DOWN":
        if position[0]<len(map):
            if map[position[0]+1][position[1]]!="#":
                map[position[0]][position[1]]=" "
                map[position[0]+1][position[1]]="C"
                position = (position[0]+1, position[1])
    elif direction=="LEFT":
        if position[1]>0:
            if map[position[0]][position[1]-1] != "#":
                map[position[0]][position[1]] = " "
                map[position[0]][position[1]-1] = "C"
                position = (position[0], position[1]-1)
    elif direction=="RIGHT":
        if position[1]<len(map[0]):
            if map[position[0]][position[1]+1] != "#":
                map[position[0]][position[1]] = " "
                map[position[0]][position[1]+1] = "C"
                position = (position[0], position[1]+1)
    return map, position

def find_start(map, start):
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value == start:
                return i,j
    return None

def find_end(map, end):
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value == end:
                return i,j
    return None

def my_raw_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input

def main(stdscr):
    curses.init_pair(1,curses.COLOR_CYAN, curses.COLOR_BLACK)
    maps=[map1, map2, map3, map4]
    for map in maps:
        stdscr.clear()
        start = "S"
        end = "E"
        position=find_start(map, start)
        end_point=find_end(map,end)
        map[position[0]][position[1]] = "C"
        print_map(map, stdscr)
        time.sleep(0.5)
        stdscr.refresh()

        while position!=end_point:
            user_input=my_raw_input(stdscr, 10, 10, "Direction?")
            if user_input==b'z':
                direction="UP"
            elif user_input==b's':
                direction="DOWN"
            elif user_input==b'q':
                direction="LEFT"
            elif user_input==b'd':
                direction="RIGHT"
            map, position = moving(map, position, direction)
            print_map(map, stdscr)
    stdscr.getch()

wrapper(main)