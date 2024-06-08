from pyamaze import maze, agent, COLOR

def compute_path(my_maze, my_agent):

    # Verificação de labirinto vazio
    if my_maze.rows == 0 or my_maze.cols == 0 or not my_maze.maze_map:
        print("Erro de Labirinto Vazio")
        return {}
    
    # Verificação de agente nulo
    if my_agent is None:
        print("Erro de Agente Nulo.")
        return {}
    
    # Atribuição de início e saída
    start = (my_maze.rows, my_maze.cols)
    goal = (my_maze._goal)

    # Listas para explorar
    explored = [start]
    frontier = [start]
    dicPath = {}
    
    # Verificação se o agente já está na célula de saída
    if start == goal:
        return {start: start}

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

    # Verificação se a saída não foi encontrada
    if goal not in dicPath:
        print("Não foi possível encontrar um caminho até a saída.")
        return {}

    path = {}
    cell = goal
    while cell != start:
        path[dicPath[cell]] = cell
        cell = dicPath[cell]
    # Imprimir o caminho
    print("Caminho encontrado:", path)
    return path

if __name__ == "__main__":
    # cria environment
    my_maze = maze()
    # leitura do labirinto do exercício
    my_maze.CreateMaze(pattern="v", theme=COLOR.light)
    # criação do agente
    my_agent = agent(my_maze, shape="arrow", filled=True, footprints=True)
    # computo do caminho que o agente vai fazer para atingir a saída
    my_path = compute_path(my_maze, my_agent)
    # execução do computo do caminho
    my_maze.tracePath({my_agent: my_path}, delay=200)
    # executa tudo
    my_maze.run()