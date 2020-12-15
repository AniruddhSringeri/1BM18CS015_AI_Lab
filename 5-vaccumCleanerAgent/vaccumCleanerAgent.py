def print_action(k ,l):
    if(floor[k][l] == 0):
        print("Location is clean")
    else:
        print("Location is dirty, sucking...")
        floor[k][l] = 0
        print("Done sucking")
        
def jobdone():
    for k in range(r):
        for l in range(c):
            if(floor[k][l] == 1):
                return False
    return True

floor =  []

c = 4
r = 3

i = 0
j = 0

prev_move = "right"   
    
        
def move_left():
    global j
    global i
    j = j - 1
    global prev_move
    prev_move = "left"
    print("Moving left..")
    print("Reached room " + str(i+1) +"," + str(j+1))
    print_action(i, j)

def move_right():
    global j
    global i
    
    global prev_move
    prev_move = "right"
    j = j + 1
    print("Moving right..")
    print("Reached room " + str(i+1) +"," + str(j+1))
    print_action(i, j)
    
def move_down():
    global j
    global i
    global prev_move
    prev_move = "down"
    i = i + 1
    print("Moving down..")
    print("Reached room " + str(i+1) +"," + str(j+1))
    print_action(i, j)
    
def move_up():
    global j
    global i
    global prev_move
    prev_move = "up"
    i = i - 1
    print("Moving up..")
    print("Reached room " + str(i+1) +"," + str(j+1))
    
def clean():
    global i, j, r, c
    r = int(input("Enter the number of rows:")) 
    c = int(input("Enter the number of columns:")) 
    
    print("Enter the entries row wise:") 

    for y in range(r):
        a =[] 
        for z in range(c): 
             a.append(int(input())) 
        floor.append(a) 
    
    print("The entered floor is as follows")

    for y in range(r): 
        for z in range(c): 
            print(floor[y][z], end = " ") 
        print() 
    print("r is "+ str(r))
    print("c is "+ str(c))

    print("Starting from room 1, 1")
    
    print_action(i, j)
    while(jobdone() == False):
        if(j == 0):
            if(prev_move == "left"):
                if(i == r-1):
                    break
                move_down()
            else:
                move_right()

        elif(j == c - 1):
            if(prev_move == "right"):
                if(i == r - 1):
                    break
                move_down()
            else:
                move_left()

        else:
            if(prev_move == "left"):
                move_left()
            else:
                move_right()

    print("Job done, the floor is clean")
    for y in range(r): 
        for z in range(c): 
            print(floor[y][z], end = " ") 
        print()
      
clean()