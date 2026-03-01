Overview:
This project is a dynamic pathfinding visualizer built using Python and Pygame.
It demonstrates how different search algorithms explore a grid to find a path between a start node and a goal node.
The simulator allows real-time interaction, obstacle generation, and dynamic changes while the algorithm is running.
FEATURES:
Visual implementation of:
A* Search
Greedy Best-First Search (GBFS)
Two heuristic options:
Manhattan Distance
Euclidean Distance
Interactive grid system
Dynamic obstacle generation during search
Real-time visualization of:
Visited nodes
Frontier (open set)
Final path
Performance metrics display:
Nodes Visited
Path Cost
Execution Time
How It Works
The grid consists of nodes (spots). Each node can be:
Start node (Blue)
Goal node (Purple)
Obstacle (Black)
Visited node (Red)
Frontier node (Yellow)
Final path (Green)
Algorithm Behavior
A* uses both:
g(n) → cost from start to current node
h(n) → heuristic estimate to goal
f(n) = g(n) + h(n)
Greedy Best-First Search uses only:
h(n) → heuristic value
It does not consider the actual path cost.
The algorithms use a priority queue (heap) to always expand the node with the lowest score.
Controls
Key	Action
Mouse Click	Set Start, Goal, and Obstacles
SPACE	Start search
A	Toggle between A* and GBFS
H	Switch heuristic (Manhattan / Euclidean)
G	Generate random maze
D	Toggle dynamic obstacles
C	Clear grid
Dynamic Mode
When dynamic mode is enabled:
Random obstacles may appear during the search.
This simulates a changing environment.
The algorithm adapts in real time.
Purpose of the Project
This project helps in understanding:
Difference between informed search algorithms
Effect of heuristics on performance
Path optimality vs speed
How priority queues work in search algorithms
Real-time AI behavior in dynamic environments
Technologies Used:
Python
Pygame
heapq (Priority Queue)
math module
