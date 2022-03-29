import curses
from curses import wrapper
import time

def my_raw_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input

def main(stdscr):
    stdscr.getch()
    user_input=my_raw_input(stdscr, 5, 5, "Direction?")
    print(user_input)
    time.sleep(5)

wrapper(main)