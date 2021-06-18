# pathfinderAI
Using a breadth-first search algorithm, the code can generate a maze of custom size and difficulty and output a path from beginning to end.

## features
- board generation with size and difficulty optional
- rules of the game provided via 'check_valid' function that checks if moves are valid
- converts maze to more familiar x, y coordinates so that any given square = maze[y][x]
- breadth-first search algorithm that inputs the most recent list of valid paths, and outputs an updated list of input paths + new valid moves - non-valid paths
- because of this, as the maze increases, as do computational demands at an exponential rate
- prints out maze showing the path found as well as how many moves were required 
