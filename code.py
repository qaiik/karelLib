x   = 0   #starting x 
y   = 0   #starting y
dir = 0   #starting direction

FLAT = 0
UP = 1
BACK = 2
DOWN = 3

def k_change_dir(n):
    global dir
    dir += n
    if dir > 3:
        dir = 0
    if dir < 0:
        dir = 3
    
        
def k_turn_left():
    k_change_dir(1)
    turn_left()
    
def k_turn_right():
    k_change_dir(-1)
    turn_right()
    
def k_set_dir(n): #find a way to determine if its faster to decrement (turn right) or increment (turn left)
    while dir != n:
        k_turn_left()
        
def move_x(mvx):
    global dir
    global x
    dir_bkp = dir
    k_set_dir(0 if mvx > 0 else 2)
    
    for _ in range(abs(mvx)):
        move()
        if mvx > 0:
            x += 1
        else:
            x -= 1
    k_set_dir(dir_bkp)
    
def move_y(mvy):
    global dir
    global y
    dir_bkp = dir
    k_set_dir(1 if mvy > 0 else 3)
    for _ in range(abs(mvy)):
        move()
        if mvy > 0:
            y += 1
        else:
            y -= 1
    k_set_dir(dir_bkp)

def set_x(tox):
    if x < tox:
        move_x(tox - x)
    else:
        move_x(-(x - tox))

def set_y(toy):
    if y < toy:
        move_y(toy - y)
    else:
        move_y(-(y - toy))
        
def find_max_x(): 
    global x
    global dir
    dir_bkp = dir
    k_set_dir(0)
    while front_is_clear():
        move_x(1)
    k_set_dir(dir_bkp)
    return x

def find_max_y(): 
    global y
    global dir
    dir_bkp = dir
    k_set_dir(1)
    while front_is_clear():
        move_y(1)
    k_set_dir(dir_bkp)
    return y
        
# mx = find_max_x()
# my = find_max_y()
# move_y(-my)
# move_x(-mx)
