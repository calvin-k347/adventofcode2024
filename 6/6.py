visted = set()
with open("6pt1.txt") as f:
    rows = f.readlines()
    pos = [0,0]
    dir = ("^", ">", "v", "<")
    y_bounds = len(rows)
    x_bounds = len(rows[0]) - 1
    for i in range(len(rows)):
        for j in range(len(rows[i])-1):
            if rows[i][j] not in (".", "#"):
                pos = [i,j]
                dir = rows[i][j]
    print(rows[y_bounds-1][x_bounds-1])
    print(pos)
    
    while(pos[0] >= 0 and pos[1] >= 0 and pos[0] < y_bounds and pos[1] < x_bounds):
        y = pos[0] 
        x = pos[1]

        if dir == "^": 
            pos[0] -= 1
            if rows[pos[0]][pos[1]] == "#":
                pos[0] +=1
                dir = ">"
        if dir == ">":
            pos[1] += 1
            if rows[pos[0]][pos[1]] == "#":
                pos[1] -=1
                dir = "v"
        if dir == "v":
            pos[0] += 1
            if rows[pos[0]][pos[1]] == "#":
                pos[0] -=1
                dir = "<"
        if dir == "<":
            pos[1] -= 1
            if rows[pos[0]][pos[1]] == "#":
                pos[1] +=1
                dir = "^"

        visted.add((pos[0],pos[1]))
    print(len(visted))
    