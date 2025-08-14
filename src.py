x            = 0   #starting x 
y            = 0   #starting y
dir          = 0   #starting direction
sdir         = dir #starting snapshot of dir

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
    
def k_set_dir(n):
    global dir
    left_turns = (n - dir) % 4
    right_turns = (dir - n) % 4

    if left_turns <= right_turns:
        for _ in range(left_turns):
            k_turn_left()
    else:
        for _ in range(right_turns):
            k_turn_right()
            
def snapshot_dir():
    global sdir
    sdir = dir
    
def restore_dir():
    global sdir
    k_set_dir(sdir)

        
def move_x(mvx, onmove=lambda: None, beforemove=lambda: None):
    global dir
    global x
    dir_bkp = dir
    desired_dir = 0 if mvx > 0 else 2
    if dir != desired_dir: 
        k_set_dir(desired_dir)
    for _ in range(abs(mvx)):
        move()
        onmove()
        if mvx > 0:
            x += 1
        else:
            x -= 1
    # k_set_dir(dir_bkp)
    
def move_y(mvy, onmove=lambda: None, beforemove=lambda: None):
    global dir
    global y
    dir_bkp = dir
    desired_dir = 1 if mvy > 0 else 3
    if dir != desired_dir: 
        k_set_dir(desired_dir)
    for _ in range(abs(mvy)):
        move()
        onmove()
        if mvy > 0:
            y += 1
        else:
            y -= 1
    # k_set_dir(dir_bkp)

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
    dir = dir_bkp
    return x

def find_max_y(): 
    global y
    global dir
    dir_bkp = dir
    k_set_dir(1)
    while front_is_clear():
        move_y(1)
    k_set_dir(dir_bkp)
    dir = dir_bkp
    return y
    
def try_take_ball():
    if balls_present():
        take_ball()
        
