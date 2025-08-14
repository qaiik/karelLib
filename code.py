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
            mvx += 1
        else:
            mvx -= 1
    k_set_dir(dir_bkp)
    
def move_y(mvy):
    global dir
    global y
    dir_bkp = dir
    k_set_dir(1 if mvy > 0 else 3)
    for _ in range(abs(mvy)):
        move()
        if mvy > 0:
            mvy += 1
        else:
            mvy -= 1
    k_set_dir(dir_bkp)
