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
        
def move_x(x):
    global dir
    dir_bkp = dir
    k_set_dir(0 if x > 0 else 2)
    for _ in range(abs(x)):
        move()
    k_set_dir(dir_bkp)

# move_x(3)
# move_x(-3)


    
    
