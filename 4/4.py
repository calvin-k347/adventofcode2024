
with open("4pt1.txt") as f:
    rows = [line.strip() for line in f.readlines()]
    width = len(rows[0])
    height = len(rows)
    print(height, width)
    count = 0
    for i in range(height):
        for j in range(width):
            '''check linear'''
            # forwards
            if j + 3 < width:
                if rows[i][j:j+4] == "XMAS":
                    count +=1
            # backwards
            if j - 3 >= 0:
                if rows[i][j-3:j+1] == "SAMX":
                    count += 1
            # up
            if i - 3 >= 0:
                above = rows[i][j] + rows[i - 1][j] + rows[i - 2][j] + rows[i - 3][j]
                if above == "XMAS" or above == "SAMX":
                    count += 1
            if i + 3 < height :
                below = rows[i][j] + rows[i + 1][j] + rows[i + 2][j] + rows[i + 3][j]
                if below == "XMAS" or below == "SAMX":
                    count += 1
            '''check diagonal'''
            if i + 3 < height and j + 3 < width:
                diag = rows[i][j] + rows[i+1][j+1] + rows[i + 2][j + 2] + rows[i + 3][j + 3]
                if diag == "XMAS" or diag == "SAMX":
                    count +=1
            if i -3 >=0 and j - 3 >= 0:
                diag = rows[i][j] + rows[i-1][j-1] + rows[i - 2][j - 2] + rows[i - 3][j - 3]
                if diag == "XMAS" or diag == "SAMX":
                    count +=1
            if i +3 < height and j - 3 >= 0:
                diag = rows[i][j] + rows[i+1][j-1] + rows[i + 2][j - 2] + rows[i + 3][j - 3]
                if diag == "XMAS" or diag == "SAMX":
                    count +=1
            if i -3 >= 0 and j + 3 < width:
                 diag = rows[i][j] + rows[i-1][j+1] + rows[i - 2][j + 2] + rows[i - 3][j + 3]
                 if diag == "XMAS" or diag == "SAMX":
                    count +=1
            
    print(count)


