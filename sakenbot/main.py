import sys
import random

"""
    height width player_id
    -----
    width     - map width (int)
    height    - map height (int)
    player_id - player id (int)
    tick      - iteration number (int)


    Example:
    16 16 1
"""

w = -1
h = -1

def hor(maze, x, y):
    cnt = 0
    if x + 1 < w and maze[x + 1][y] == ';':
        cnt += 1
    elif x + 2 < w and maze[x + 1][y] == '.' and maze[x + 2][y] == ';':
        cnt += 1
    
    if y + 1 < h and maze[x][y + 1] == ';':
        cnt += 1
    elif y + 2 < h and maze[x][y + 1] == '.' and maze[x][y + 2] == ';':
        cnt += 1

    if x - 1 >= 0 and maze[x - 1][y] == ';':
        cnt += 1
    elif x - 2 >= 0 and maze[x - 1][y] == '.' and maze[x - 2][y] == ';':
        cnt += 1

    if y - 1 >= 0 and maze[x][y - 1] == ';':
        cnt += 1
    elif y - 2 >= 0 and maze[x][y - 2] == '.' and maze[x][y - 1] == ';':
        cnt += 1

    return cnt    
    
    

def get_boxes(maze):
    bmb = []
    for i in range(len(maze)):
        tmp_bmb = []
        for j in range(len(maze[0])):
            tmp_bmb.append(hor(maze, i, j))
        bmb.append(tmp_bmb)
    return bmb


def get_needed_maze(maze):
    character_maze = []
    for i in range(len(maze[0])):
        tmp_row = []
        for j in range(len(maze)):
            tmp_row.append(maze[j][i])
        character_maze.append(tmp_row)

    return character_maze


def get_dist(maze, x, y):
    dist = []
    for row in maze:
        tmp_row = []
        for col in row:
            tmp_row.append(1001)
        dist.append(tmp_row)
    q = []
    q.append([x, y])
    dist[x][y] = 0
    while len(q) > 0:
        tmp_x, tmp_y = q.pop(0)
        if tmp_x + 1 < w and maze[tmp_x + 1][tmp_y] ==  '.' and dist[tmp_x][tmp_y] + 1 < dist[tmp_x + 1][tmp_y]:
            q.append([tmp_x + 1, tmp_y])
            dist[tmp_x + 1][tmp_y] = dist[tmp_x][tmp_y] + 1
        if tmp_x + 1 < w and maze[tmp_x + 1][tmp_y] ==  ';' and dist[tmp_x][tmp_y] + 10 < dist[tmp_x + 1][tmp_y]:
            q.append([tmp_x + 1, tmp_y])
            dist[tmp_x + 1][tmp_y] = dist[tmp_x][tmp_y] + 10
        if tmp_y + 1 < h and maze[tmp_x][tmp_y + 1] ==  '.' and dist[tmp_x][tmp_y] + 1 < dist[tmp_x][tmp_y + 1]:
            q.append([tmp_x, tmp_y + 1])
            dist[tmp_x][tmp_y + 1] = dist[tmp_x][tmp_y] + 1
        if tmp_y + 1 < h and maze[tmp_x][tmp_y + 1] ==  ';' and dist[tmp_x][tmp_y] + 10 < dist[tmp_x][tmp_y + 1]:
            q.append([tmp_x, tmp_y + 1])
            dist[tmp_x][tmp_y + 1] = dist[tmp_x][tmp_y] + 10
        if tmp_x - 1 >= 0 and maze[tmp_x - 1][tmp_y] ==  '.' and dist[tmp_x][tmp_y] + 1 < dist[tmp_x - 1][tmp_y]:
            q.append([tmp_x - 1, tmp_y])
            dist[tmp_x - 1][tmp_y] = dist[tmp_x][tmp_y] + 1
        if tmp_x - 1 >= 0 and maze[tmp_x - 1][tmp_y] ==  ';' and dist[tmp_x][tmp_y] + 10 < dist[tmp_x - 1][tmp_y]:
            q.append([tmp_x - 1, tmp_y])
            dist[tmp_x - 1][tmp_y] = dist[tmp_x][tmp_y] + 10
        if tmp_y - 1 >= 0 and maze[tmp_x][tmp_y - 1] ==  '.' and dist[tmp_x][tmp_y] + 1 < dist[tmp_x][tmp_y - 1]:
            q.append([tmp_x, tmp_y - 1])
            dist[tmp_x][tmp_y - 1] = dist[tmp_x][tmp_y] + 1
        if tmp_y - 1 >= 0 and maze[tmp_x][tmp_y - 1] ==  ';' and dist[tmp_x][tmp_y] + 10 < dist[tmp_x][tmp_y - 1]:
            q.append([tmp_x, tmp_y - 1])
            dist[tmp_x][tmp_y - 1] = dist[tmp_x][tmp_y] + 10

    return dist


def blast(dist, maze, b_x, b_y):
    to_submit = []
    original_x = b_x
    original_y = b_y
    dst_x = min(w - 1, b_x + 12)

    while b_x - 1 != dst_x:
        # dist[b_x][b_y] = 1001
        if maze[b_x][b_y] == ';' or maze[b_x][b_y] == '!':
            break
        to_submit.append([b_x, b_y])
        # print(b_x, b_y, dst_x, b_y, file=sys.stderr)
        
        b_x += 1

    b_x = original_x
    b_y = original_y
    dst_y = min(h - 1, b_y + 12)
    while b_y - 1 != dst_y:
        # dist[b_x][b_y] = 1001
        if maze[b_x][b_y] == ';' or maze[b_x][b_y] == '!':
            break
        to_submit.append([b_x, b_y])
        # print(b_x, b_y, b_x, dst_y, file=sys.stderr)
        
        b_y += 1

    b_x = original_x
    b_y = original_y
    dst_x = max(0, b_x - 12)
    while b_x + 1 != dst_x:
        # dist[b_x][b_y] = 1001
        if maze[b_x][b_y] == ';' or maze[b_x][b_y] == '!':
            break
        to_submit.append([b_x, b_y])
        # print(b_x, b_y, dst_x, b_y, file=sys.stderr)
        b_x -= 1

    b_x = original_x
    b_y = original_y
    dst_y = max(0, b_y - 12)
    while b_y + 1 != dst_y:
        # dist[b_x][b_y] = 1001
        if maze[b_x][b_y] == ';' or maze[b_x][b_y] == '!':
            break
        to_submit.append([b_x, b_y])
        # print(b_x, b_y, b_x, dst_y, file=sys.stderr)
        
        b_y -= 1
    return to_submit


def safe_point(entities, dist, maze, p_x, p_y):
    bombs = []
    for entity in entities:
        if entity[0] == 'b':
            b_x = int(entity[2])
            b_y = int(entity[3])
            dist[b_x][b_y] = 1001
            for blst in blast(maze, dist, b_x, b_y):
                bombs.append(blst)
                # print(blst, file=sys.stderr)
            # print(blst, file=sys.stderr)
    
    print(bombs, file=sys.stderr)

    mn = 1001
    _x = -1
    _y = -1
    for i in range(len(dist)):
        for j in range(len(dist[0])):
            # print(dist[i][j], end = '\t', file=sys.stderr)
        
            if dist[i][j] < mn and [i, j] not in bombs:
                mn = dist[i][j]
                _x = i
                _y = j
    #     print('', file=sys.stderr)
    # print('', file=sys.stderr)
    # print('safe point:', _x, _y, file=sys.stderr)
    return _x, _y

def bombs_nearby(entities, p_x, p_y):
    for entity in entities:
        if entity[0] == 'b':
            b_x = int(entity[2])
            b_y = int(entity[3])


            if abs(p_x - b_x) + abs(p_y - b_y) <= 4:
                return True
    return False

def move(maze, p_x, p_y, dest_x, dest_y, bomb_near):
    actions = ['up', 'down', 'right', 'left']
    if dest_x == p_x and dest_y == p_y:
        if bomb_near == False:
            return 'bomb'
        return 'stay'
    dst = get_dist(maze, dest_x, dest_y)
    mn = 1001
    dir_x = -1
    dir_y = -1
    direction = 'WARNING'
    if p_x + 1 < w and dst[p_x + 1][p_y] < mn:
        mn = dst[p_x + 1][p_y]
        dir_x = p_x + 1
        dir_y = p_y
        direction = 'right'
    if p_y + 1 < h and dst[p_x][p_y + 1] < mn:
        mn = dst[p_x][p_y + 1]
        direction = 'down'
        dir_x = p_x
        dir_y = p_y + 1
    if p_x - 1 >= 0 and dst[p_x - 1][p_y] < mn:
        mn = dst[p_x - 1][p_y]
        direction = 'left'
        dir_x = p_x - 1
        dir_y = p_y
    if p_y - 1 >= 0 and dst[p_x][p_y - 1] < mn:
        mn = dst[p_x][p_y - 1]
        direction = 'up'
        dir_x = p_x
        dir_y = p_y - 1

    if maze[dir_x][dir_y] == ';':
        direction = 'bomb'
    # for row in dst:
    #     for col in row:
    #         print(col, end = '\t', file=sys.stderr)
    #     print('', file=sys.stderr)
    # print('', file=sys.stderr)


    # print('dst:', dst[p_x][p_y], mn, file=sys.stderr)
    # if abs(dst[p_x][p_y] - mn) > 1:
    #     direction = 'bomb'
    return direction
        

dest_x = -1
dest_y = -1

while True:
    bomb_present = False
    mz = []
    p_x = -1
    p_y = -1
    me = -1
    entities = []
    line = input()
    w = int(line.split()[0])
    h = int(line.split()[1])
    me = int(line.split()[2])
    # print(line, file=sys.stderr)
    for i in range(h):
        # read map line
        line = input()
        # print(line, file=sys.stderr)
        mz.append(line)
    

    # n - number of actions takes during the tick
    n = int(input())

    for i in range(n):
        # read actions
        line = input()
        # print(line, file = sys.stderr)
        arr = line.split()
        entities.append(arr)
        if arr[0] == 'p' and me == int(arr[1]):
            p_x = int(arr[2])
            p_y = int(arr[3])
    
    n = int(input())

    for i in range(n):
        # read features
        line = input()
    
    # print('my coords:', p_x, p_y, file=sys.stderr)
    mz = get_needed_maze(mz)
    dist = get_dist(mz, p_x, p_y)

    # for row in dist:
    #     for col in row:
            # print(col, end = '\t', file=sys.stderr)
        # print('', file=sys.stderr)
    # print('', file=sys.stderr)

    boxes = get_boxes(mz)

    mn = 1001.0
    ratio = []
    for i in range(len(dist)):
        tmp_ratio = []
        for j in range(len(dist[0])):
            if boxes[i][j] != 0:
                tmp_ratio.append((dist[i][j] + 6) / boxes[i][j])
            else:
                tmp_ratio.append(1001)

            if tmp_ratio[j] < mn:
                mn = tmp_ratio[j]
                dest_x = i
                dest_y = j
        ratio.append(tmp_ratio)

    if bombs_nearby(entities, p_x, p_y):
        dest_x, dest_y = safe_point(entities, dist, mz, p_x, p_y)
    
    print(move(mz, p_x, p_y, dest_x, dest_y, bombs_nearby(entities, p_x, p_y)))
    # print('move:', move(mz, p_x, p_y, dest_x, dest_y, bombs_nearby(entities, p_x, p_y)), file=sys.stderr)

    # print('dest_x:', dest_x, 'dest_y:', dest_y, file = sys.stderr)

    # for row in dist:
        # print(row, file=sys.stderr)
    # print('', file = sys.stderr)


    
    # use file=sys.stderr to print for debugging
    # print("debug code", file=sys.stderr)

    # this will choose one of random actions
    actions = ["left", "up", "bomb", "right", "down"]
    random_index = random.randint(0, len(actions) - 1)

    # bot action
    # print(actions[random_index])