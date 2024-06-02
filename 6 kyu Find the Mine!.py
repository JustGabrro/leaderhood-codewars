def mine_location(field):
    for x in range(len(field)):
        for y in range(len(field)):
            if field[x][y] == 1:
                return [x, y]