import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random as rd

# Maze dimensions
size_x = 10
size_y = 10

# Setup the figure
plt.xticks([]), plt.yticks([])
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Draw the grid
def line(x1, y1, x2, y2):
    """Draws a line between two points."""
    plt.plot([x1, x2], [y1, y2], color='white', linewidth=1)

# Draw outer boundaries and grid lines
line(0, 0, size_x, 0)  # Bottom wall
line(size_x, 0, size_x, size_y)  # Right wall
line(size_x, size_y, 0, size_y)  # Top wall
line(0, size_y, 0, 0)  # Left wall
for i in range(1, size_x):
    line(i, 0, i, size_y)  # Vertical lines
for j in range(1, size_y):
    line(0, j, size_x, j)  # Horizontal lines

# Define cells and make them unvisited
cells = [[{'visited': False} for _ in range(size_y)] for _ in range(size_x)]
stack = []  # Stack for backtracking
steps = []  # Steps to animate
Longest_path = [0,0]
path_size = len(stack)
# Mark cell as visited
def visited_cell(x, y):
    cells[x][y]['visited'] = True

# Generate random starting point on the boundary
def random_xy():
    rand = rd.randint(1, 4)
    if rand == 1:  # Left wall
        return 0, rd.randint(0, size_y - 1)
    elif rand == 2:  # Bottom wall
        return rd.randint(0, size_x - 1), 0
    elif rand == 3:  # Right wall
        return size_x - 1, rd.randint(0, size_y - 1)
    else:  # Top wall
        return rd.randint(0, size_x - 1), size_y - 1

# Deletes a wall
def del_line(x1, y1, x2, y2):
    """Deletes the wall between two adjacent cells."""
    if x1 == x2:  # Vertical alignment
        if y1 < y2:  # Up
            steps.append(((x1, x1 + 1), (y1 + 1, y1 + 1)))
        elif y1 > y2:  # Down
            steps.append(((x1, x1 + 1), (y1, y1)))
    elif y1 == y2:  # Horizontal alignment
        if x1 < x2:  # Right
            steps.append(((x1 + 1, x1 + 1), (y1, y1 + 1)))
        elif x1 > x2:  # Left
            steps.append(((x1, x1), (y1, y1 + 1)))

# Find neighbors of the current cell
def neighbors():
    x, y = current_cell
    neighbor_cells = []
    if y + 1 < size_y and not cells[x][y + 1]['visited']:  # Up
        neighbor_cells.append((x, y + 1))
    if x + 1 < size_x and not cells[x + 1][y]['visited']:  # Right
        neighbor_cells.append((x + 1, y))
    if y - 1 >= 0 and not cells[x][y - 1]['visited']:  # Down
        neighbor_cells.append((x, y - 1))
    if x - 1 >= 0 and not cells[x - 1][y]['visited']:  # Left
        neighbor_cells.append((x - 1, y))
    return neighbor_cells

# Initialize maze generation
start_x, start_y = random_xy()
visited_cell(start_x, start_y)

current_cell = [start_x, start_y]
stack.append(current_cell)

# Simulate the maze generation and record steps
while stack:
    if not neighbors():  # If all neighbors are visited
        stack.pop()
        if stack:
            current_cell = stack[-1]
    else:
        neighbor_cells = neighbors()
        n = rd.randint(0, len(neighbor_cells) - 1)
        neighbor = neighbor_cells[n]
        del_line(current_cell[0], current_cell[1], neighbor[0], neighbor[1])
        visited_cell(neighbor[0], neighbor[1])
        stack.append(neighbor)
        current_cell = neighbor

        if len(stack) > path_size:
            Longest_path= current_cell
            path_size = len(stack)

# Start point visualization
plt.scatter(start_x+0.5 , start_y+0.5, color='green')  # Start
plt.text(size_x/2.5, -1, 'START', color='green', fontsize=12) #Label
plt.text(size_x/1.5, -1, 'END', color='red', fontsize=12) #Label
plt.scatter(Longest_path[0]+0.5 , Longest_path[1]+0.5, color='red')  # End 


# Animation function
def update(frame):
    """Animates the maze generation by drawing the recorded steps."""
    if frame < len(steps):
        x_coords, y_coords = steps[frame]
        ax.plot(x_coords, y_coords, color='black', linewidth=2)

# Animate the steps
ani_steps = ani.FuncAnimation(fig, update, frames=len(steps), interval=100, repeat=False)
 

# Show animation
plt.show()
