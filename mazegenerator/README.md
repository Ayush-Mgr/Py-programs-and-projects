# 🚀 Maze Generator  🧩

Welcome to the **Maze Generator **! This repository contains three independent Python scripts that generate and animate mazes using Depth-First Search (DFS). Perfect for maze enthusiasts, educators, or coders who love procedural generation! 

![Maze GIF](https://media.giphy.com/media/3o7TKUM3IgJBX2as9O/giphy.gif)

---

## 📦 **Dependencies Installation**

**All scripts require these libraries**. Install them as follows:

### For `grid.py` (Grid Generator):
```bash
pip install matplotlib
```

### For `maze.py`  (Static Maze Generator)and `animation_maze.py`(Animated Maze Generator) :
```bash
pip install matplotlib random
```

---

## 🧠 **How It Works: Depth-First Search (DFS)**

### 📚 Algorithm Breakdown
1. **Start at a random cell**.
2. **Mark it as visited**.
3. **Choose a random unvisited neighbor** and carve a path.
4. **Recursively Backtrack** if got stuck ,go back to last saved checkpoint.
5. ** repeat** until all cells are visited.

![DFS Maze Generation](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)
---

## 🛠 **Technical Deep Dive**

### `grid.py`
- Uses `matplotlib` to plot a basic grid.
- **No maze logic**—just a canvas for visualization!

### `maze.py`
- **DFS-driven**: Builds a maze by recursively knocking down walls,**recurssive bactracking** and checking unvisited cells 
- Rendered statically with `matplotlib`.


### `animation_maze.py`
- **matplotlib.animation magic**: Animates the DFS process step-by-step.

---
## DONE

![Celebration GIF](https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif)
