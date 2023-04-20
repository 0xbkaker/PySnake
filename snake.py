import time

import curses
x = 0
y = 0


def curses_init():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)
    return stdscr

def move_up():
    global x
    global y
    y -= 1
    window.delch(y+1,x)
    window.addch(y,x,'■')

def move_down():
    global x
    global y
    y += 1
    window.delch(y-1,x)
    window.addch(y,x,'■')


def move_right():
    global x
    global y
    x += 1
    window.delch(y,x-1)
    window.addch(y,x,'■')

def move_left():
    global x
    global y
    x -= 1
    window.delch(y,x+1)
    window.addch(y,x,'■')




window = curses_init()

c = window.getch()
if c == curses.KEY_DOWN:
    move = move_down
elif c == curses.KEY_UP:
    move = move_up
elif c == curses.KEY_RIGHT:
    move = move_right
elif c == curses.KEY_LEFT:
    move = move_left

window.nodelay(True)

while True:
    move()
    c = window.getch()
    if c == curses.KEY_DOWN:
        move = move_down
    elif c == curses.KEY_UP:
        move = move_up
    elif c == curses.KEY_RIGHT:
        move = move_right
    elif c == curses.KEY_LEFT:
        move = move_left
    time.sleep(0.1)
    
    if c == ord('q'):
        window.nodelay(False)
        break  # Exit the while loop