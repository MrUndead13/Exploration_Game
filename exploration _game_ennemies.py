#TO DO:
#Add ennemies that bump back : DONE
#Add an input to attack and erase the ennemy : DONE
#Add a score and print it : DONE
#Add a life counter that is shown on screen and reduces when hit by ennemy : DONE

#Use git to manage different versions of the project
#Add a final boss that moves every time he loses a life (10 lifes)
#Find other features

import curses
from curses import wrapper
import time
from maps_ennemies import *

def print_map(map, stdscr):
    CYAN = curses.color_pair(1)

    for i, row in enumerate(map):
        for j, value in enumerate(row):
            stdscr.addstr(i,j*2,value, CYAN)

def moving(map, position, direction, lifes):
    if direction=="UP":
        if position[0]>0:
            if check_ennemy(map, position, direction)==True:
                lifes-=1
                if map[position[0]+1][position[1]]!="#":
                    map[position[0]][position[1]] = " "
                    map[position[0] + 1][position[1]] = "C"
                    position = (position[0] + 1, position[1])

            else:
                if map[position[0]-1][position[1]]!="#":
                    map[position[0]][position[1]]=" "
                    map[position[0]-1][position[1]]="C"
                    position=(position[0]-1,position[1])
    elif direction=="DOWN":
        if position[0]<len(map):
            if check_ennemy(map, position, direction) == True:
                lifes -= 1
                if map[position[0]-1][position[1]]!="#":
                    map[position[0]][position[1]]=" "
                    map[position[0]-1][position[1]]="C"
                    position=(position[0]-1,position[1])
            else:
                if map[position[0]+1][position[1]]!="#":
                    map[position[0]][position[1]]=" "
                    map[position[0]+1][position[1]]="C"
                    position = (position[0]+1, position[1])
    elif direction=="LEFT":
        if position[1]>0:
            if check_ennemy(map, position, direction) == True:
                lifes -= 1
                if map[position[0]][position[1] + 1] != "#":
                    map[position[0]][position[1]] = " "
                    map[position[0]][position[1] + 1] = "C"
                    position = (position[0], position[1] + 1)
            else:
                if map[position[0]][position[1]-1] != "#":
                    map[position[0]][position[1]] = " "
                    map[position[0]][position[1]-1] = "C"
                    position = (position[0], position[1]-1)
    elif direction=="RIGHT":
        if position[1]<len(map[0]):
            if check_ennemy(map, position, direction) == True:
                lifes -= 1
                if map[position[0]][position[1]-1] != "#":
                    map[position[0]][position[1]] = " "
                    map[position[0]][position[1]-1] = "C"
                    position = (position[0], position[1]-1)
            else:
                if map[position[0]][position[1]+1] != "#":
                    map[position[0]][position[1]] = " "
                    map[position[0]][position[1]+1] = "C"
                    position = (position[0], position[1]+1)
    return map, position, lifes

def check_ennemy(map, position, direction):
    ennemy=False
    if direction=="UP":
        if map[position[0]-1][position[1]]=="X":
            ennemy=True
    elif direction=="DOWN":
        if map[position[0]+1][position[1]]=="X":
            ennemy=True
    elif direction=="LEFT":
        if map[position[0]][position[1]-1]=="X":
            ennemy=True
    elif direction=="RIGHT":
        if map[position[0]][position[1]+1]=="X":
            ennemy=True
    return ennemy

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

def attack(map, position, attack_direction, score):
    if (map[position[0]-1][position[1]]=="X" and attack_direction=="UP"):
        map[position[0] - 1][position[1]] = " "
        score += 100
    elif (map[position[0]+1][position[1]]=="X" and attack_direction=="DOWN"):
        map[position[0] + 1][position[1]] = " "
        score += 100
    elif (map[position[0]][position[1]-1]=="X" and attack_direction=="LEFT"):
        map[position[0]][position[1]-1] = " "
        score += 100
    elif (map[position[0]][position[1]+1]=="X" and attack_direction=="RIGHT"):
        map[position[0]][position[1]+1] = " "
        score += 100
    return map, score

def my_raw_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input

def main(stdscr):
    quit=False
    score=0
    lifes=3
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    maps = [map1, map2, map3, map4]
    for map in maps:
        if quit==False:
            stdscr.clear()
            start = "S"
            end = "E"
            position = find_start(map, start)
            end_point = find_end(map, end)
            map[position[0]][position[1]] = "C"
            print_map(map, stdscr)
            stdscr.addstr(15, 15, "Lifes: " + str(lifes))
            stdscr.addstr(20, 20, "Score: " + str(score))
            time.sleep(0.5)
            stdscr.refresh()

            while position != end_point and lifes > 0:
                # while lifes>0:
                direction = None
                attack_direction = None
                user_input = my_raw_input(stdscr, 10, 10, "Direction or attack?")
                if user_input == b'z':
                    direction = "UP"
                elif user_input == b's':
                    direction = "DOWN"
                elif user_input == b'q':
                    direction = "LEFT"
                elif user_input == b'd':
                    direction = "RIGHT"
                elif user_input == b'i':
                    attack_direction = "UP"
                elif user_input == b'k':
                    attack_direction = "DOWN"
                elif user_input == b'j':
                    attack_direction = "LEFT"
                elif user_input == b'l':
                    attack_direction = "RIGHT"
                if attack_direction == None:
                    map, position, lifes = moving(map, position, direction, lifes)
                else:
                    map, score = attack(map, position, attack_direction, score)
                print_map(map, stdscr)
                stdscr.addstr(15, 15, "Lifes: " + str(lifes))
                stdscr.addstr(20, 20, "Score: " + str(score))
            if lifes == 0:
                quit = True
                stdscr.addstr(15, 15, "Lifes: " + str(lifes))
                stdscr.addstr(0, 25, "Game Over")
                stdscr.refresh()

    stdscr.getch()
wrapper(main)