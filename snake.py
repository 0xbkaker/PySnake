import curses
H = 20
W = 10
def curses_init():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    return stdscr

def r():
    for yy in range(W):
        for xx in range(H):
            window.addch(yy,xx,m[yy][xx])
        #time.sleep(0.1)
        window.refresh()

def change_y(d):
    global x
    global y
    y += d
    m[y-d][x] = '░'
    m[y][x] = '■'

def change_x(d):
    global x
    global y
    x += d
    m[y][x-d] = '░'
    m[y][x] = '■'   

x = 0
y = 0
m = [['░' for x in range(H)] for y in range(W)] 
m[0][0] = '■'


 


        
window = curses_init()
while True:
    r()
    c = window.getch()
    if c == curses.KEY_DOWN:
        change_y(1)
    elif c == curses.KEY_UP:
        change_y(-1)
    elif c == curses.KEY_RIGHT:
        change_x(1)
    elif c == curses.KEY_LEFT:
        change_x(-1)        
    elif c == ord('q'):
        break  # Exit the while loop