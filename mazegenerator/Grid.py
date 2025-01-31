import matplotlib.pyplot as plt
size_x = 5
size_y = 5
#plt.figure(figsize=(size_x,size_y))
#plt.xticks([]), plt.yticks([])
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('grey')
ax.tick_params(axis='both', colors='white')

def line(x1, y1, x2, y2):
    """Draws a line between two points."""
    plt.plot([x1, x2], [y1, y2], color='white', linewidth=2)

def del_line(x1, y1, x2, y2, color='white'):
    """Draws a line between two points."""
    plt.plot([x1, x2], [y1, y2], color= 'black', linewidth=2)


    
# Draw outer boundaries

line(0, 0, size_x , 0)  # Bottom wall
line(size_x , 0, size_x   , size_y )  # Right wall
line(size_x , size_y , 0,size_y )  # Top wall
line(0, size_y , 0, 0)  # Left wall

for i in range(1, size_x):
    line(i , 0, i , size_y )  # Vertical lines

for j in range(1, size_y):
    line(0, j , size_x , j )  # Horizontal lines

del_line(2, 2, 0)  # Remove the "Up" wall
del_line(2, 2, 1)  # Remove the "Right" wall
del_line(2, 2, 2)  # Remove the "Down" wall
del_line(2, 2, 3)  # Remove the "Left" wall
#Start and end points (optional visualization)
plt.scatter(0.5, 0.5, color='green', label='Start')  # Start
plt.scatter(4.5, 4.5, color='red', label='End')  # End


# Show the legend
plt.legend()

plt.show()

