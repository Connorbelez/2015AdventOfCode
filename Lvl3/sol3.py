# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location,
# and then an elf at the North Pole calls him via radio and tells him where 
# to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
# After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog,
# and so his directions are a little off, and Santa ends up visiting some 
# houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses






class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rx = 0
        self.ry = 0
        self.visited = {"0,0":True}
    def moveS(self, direction):
        print("Move: ",direction)
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '>':
            self.x += 1
        elif direction == '<':
            self.x -= 1
        else:
            raise Exception('Invalid direction')
        self.visited[str(self.x) + ',' + str(self.y)] = True
    def moveRS(self, direction):
        print("Move: ",direction)
        if direction == '^':
            self.ry += 1
        elif direction == 'v':
            self.ry -= 1
        elif direction == '>':
            self.rx += 1
        elif direction == '<':
            self.rx -= 1
        else:
            raise Exception('Invalid direction')
        self.visited[str(self.rx) + ',' + str(self.ry)] = True


    def countVisited(self):
        return len(self.visited)

        
    
if __name__ == '__main__':
    map1 = {}
    santa = Santa()

    with open('data3.txt') as f:
        moves = f.read()
        for i in range(len(moves)):
            if i % 2 == 0:
                santa.moveS(moves[i])
            else:
                santa.moveRS(moves[i])
    print(santa.countVisited())