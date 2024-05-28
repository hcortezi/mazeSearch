from pyamaze import maze, agent, COLOR

def compute_path(my_maze, my_agent):

    start = (my_maze.rows, my_maze.cols)
    goal = (1, 1)
    explored = [start]
    frontier = [start]
    dicPath = {}

    while frontier:
        cellAtual = frontier.pop()
        if cellAtual == goal:
            break
        for d in 'ESNW':
            if my_maze.maze_map[cellAtual][d] == True:
                if d == 'E':
                    cellFilha = (cellAtual[0], cellAtual[1] + 1)
                elif d == 'W':
                    cellFilha = (cellAtual[0], cellAtual[1] - 1)
                elif d == 'S':
                    cellFilha = (cellAtual[0] + 1, cellAtual[1])
                elif d == 'N':
                    cellFilha = (cellAtual[0] - 1, cellAtual[1])
                if cellFilha in explored:
                    continue
                explored.append(cellFilha)
                frontier.append(cellFilha)
                dicPath[cellFilha] = cellAtual

    path = {}
    cell = goal
    while cell != start:
        path[dicPath[cell]] = cell
        cell = dicPath[cell]
    return path

if __name__ == "__main__":
    # cria environment
    my_maze = maze(10, 10)
    # leitura do labirinto do exercício
    my_maze.CreateMaze(1, 1, pattern="v", theme=COLOR.light)
    # criação do agente
    my_agent = agent(my_maze, 10, 10, shape="arrow", filled=True, footprints=True)
    # computo do caminho que o agente vai fazer para atingir a saída
    my_path = compute_path(my_maze, my_agent)
    # execução do computo do caminho
    my_maze.tracePath({my_agent: my_path}, delay=200)
    # executa tudo
    my_maze.run()
