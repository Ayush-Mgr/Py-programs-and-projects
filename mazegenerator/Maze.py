import matplotlib.pyplot as plt
import random as rd

size_x = 20
size_y = 20

plt.xticks([]), plt.yticks([])
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')



def line(x1, y1, x2, y2):
    """Draws a line between two points."""
    plt.plot([x1, x2], [y1, y2], color='white', linewidth=1)


    
# Draw outer boundaries

line(0, 0, size_x , 0)  # Bottom wall
line(size_x , 0, size_x  , size_y)  # Right wall
line(size_x, size_y, 0,size_y)  # Top wall
line(0, size_y, 0, 0)  # Left wall
for i in range(1, size_x):
    line(i , 0, i , size_y )  # Vertical lines

for j in range(1, size_y):
    line(0, j , size_x , j )  # Horizontal lines



# the stack
stack = []

# Define cells and makes it unvisited
cells = [[{'visited': False} for _ in range(size_y)] for _ in range(size_x)]

#make cells visited
def visited_cell(x,y):
    cells[x][y]['visited'] = True

#gen random xy from walls
def Random_xy() :
    rand = rd.randint(1,4)
    
    if rand == 1:
        x = 0
        y = rd.randint(1,size_y-1)

    if rand == 2:
        x = rd.randint(1,size_x-1)
        y = 0
    
    if rand == 3:
        x = 4
        y = rd.randint(1,size_y-1)

    if rand == 4:
        x = rd.randint(1,size_x-1)
        y = 4
    
    return x , y

#deletes a line
def del_line(x1, y1, x2, y2):
    """Deletes the wall between two adjacent cells dynamically."""
    if x1 == x2:  # Vertical alignment (same x-coordinate, wall is horizontal)
        if y1 < y2:  # Neighbor is above (Up)
            plt.plot([x1, x1 + 1], [y1 + 1, y1 + 1], color='black', linewidth=2)
        elif y1 > y2:  # Neighbor is below (Down)
            plt.plot([x1, x1 + 1], [y1, y1], color='black', linewidth=2)
    elif y1 == y2:  # Horizontal alignment (same y-coordinate, wall is vertical)
        if x1 < x2:  # Neighbor is to the right
            plt.plot([x1 + 1, x1 + 1], [y1, y1 + 1], color='black', linewidth=2)
        elif x1 > x2:  # Neighbor is to the left
            plt.plot([x1, x1], [y1, y1 + 1], color='black', linewidth=2)





#Nabours,checks the cell above the current cell and visited or not
def Nabours():
    x, y = current_cell
    neighbors = []
    if y + 1 < size_y and not cells[x][y + 1]['visited']:    # U 
        neighbors.append((x, y + 1))
    if x + 1 < size_x and not cells[x + 1][y]['visited']:    # R
        neighbors.append((x + 1, y))
    if y - 1 >= 0 and not cells[x][y - 1]['visited']:        # D
        neighbors.append((x, y - 1))
    if x - 1 >= 0 and not cells[x - 1][y]['visited']:        # L
        neighbors.append((x - 1, y))
    return neighbors



path_size = len(stack)
Longest_path=[]

start_x, start_y = Random_xy()


visited_cell(start_x, start_y)

current_cell = [start_x, start_y]
stack.append(current_cell)
 


while len(stack) != 0:
    if len(Nabours()) == 0: # check if all the cells are visited
        stack.pop()
        if stack:
            current_cell = stack[-1]
    else:
       neighbors = Nabours()
       n = rd.randint(0, len(neighbors)-1) # random cell from the neighbors
       
      #stack.append(current_cell)
       del_line(current_cell[0], current_cell[1], neighbors[n][0], neighbors[n][1])
       visited_cell(neighbors[n][0], neighbors[n][1])
       stack.append(current_cell)
       current_cell = neighbors[n]

       if len(stack) > path_size:
            Longest_path= current_cell
            path_size = len(stack)
       
       






#Start and end points (optional visualization)

plt.scatter(start_x+0.5 , start_y+0.5, color='green')  # Start
plt.text(size_x/2.5, -1, 'START', color='green', fontsize=12) #Label


plt.scatter(Longest_path[0]+0.5 , Longest_path[1]+0.5, color='red')  # End  
plt.text(size_x/1.5, -1, 'END', color='red', fontsize=12) #Label





plt.show()
