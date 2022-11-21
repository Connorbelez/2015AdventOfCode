# --- Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year,
# you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how 
# to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 
# 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle
# various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners
# of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 
# 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions 
# Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on,
# and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

import numpy as np

def getInstructions(string,matrix):
    lineSplit = string.strip().split(" ")
    
    if lineSplit[0] == "toggle":
        x1,y1 = map(int,lineSplit[1].split(","))
        x2,y2 = map(int,lineSplit[3].split(","))
        matrix[x1:x2+1,y1:y2+1] += 2 

    elif lineSplit[1] == "on":
        x1,y1 = map(int,lineSplit[2].split(","))
        x2,y2 = map(int,lineSplit[4].split(","))
        matrix[x1:x2+1,y1:y2+1] += 1

        # print("on",x1,y1,x2,y2)
    else:
        x1,y1 = map(int,lineSplit[2].split(","))
        x2,y2 = map(int,lineSplit[4].split(","))
        matrix[x1:x2+1,y1:y2+1] -= 1

        # print("off",x1,y1,x2,y2)
    


# if __name__ == '__main__':
#     lightMatrix = np.zeros((1000,1000),dtype= int)
#     with open("data6p1.txt") as f:
#         for line in f:
#             getInstructions(line,lightMatrix)
#     lightMatrix[lightMatrix < 0] = 0
#     print(np.sum(lightMatrix))
#     print(lightMatrix)



# import numpy as np

# def getInstructions(string,matrix):
#     lineSplit = string.strip().split(" ")
    
#     if lineSplit[0] == "toggle":
#         x1,y1 = map(int,lineSplit[1].split(","))
#         x2,y2 = map(int,lineSplit[3].split(","))
#         matrix[x1:x2+1, y1:y2+1] += 2 

#     elif lineSplit[1] == "on":
#         x1,y1 = map(int,lineSplit[2].split(","))
#         x2,y2 = map(int,lineSplit[4].split(","))
#         matrix[x1:x2+1, y1:y2+1] += 1

#         # print("on",x1,y1,x2,y2)
#     else:
#         x1,y1 = map(int,lineSplit[2].split(","))
#         x2,y2 = map(int,lineSplit[4].split(","))
#         matrix[x1:x2+1, y1:y2+1] -= 1

#         # print("off",x1,y1,x2,y2)
    

def getInstructions2(string,matrix):
    lineSplit = string.strip().split(" ")
    
    if lineSplit[0] == "toggle":
        x1,y1 = map(int,lineSplit[1].split(","))
        x2,y2 = map(int,lineSplit[3].split(","))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                matrix[i][j] += 2

    elif lineSplit[1] == "on":
        x1,y1 = map(int,lineSplit[2].split(","))
        x2,y2 = map(int,lineSplit[4].split(","))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                matrix[i][j] += 1

        # print("on",x1,y1,x2,y2)
    else:
        x1,y1 = map(int,lineSplit[2].split(","))
        x2,y2 = map(int,lineSplit[4].split(","))
        # matrix[x1:x2+1,y1:y2+1] -= 1
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                matrix[i][j] -= 1
                if matrix[i][j] < 0:
                    matrix[i][j] = 0
        # print("off",x1,y1,x2,y2)
    

if __name__ == '__main__':
    lightMatrix = np.zeros((1000,1000),dtype= int)
    lm = [[0 for i in range(1000)] for j in range(1000)]
    s1 = 0
    with open("data6p1.txt") as f:
        for line in f:
            getInstructions(line,lightMatrix)
            getInstructions2(line, lm)
    lightMatrix[lightMatrix < 0] = 0
    print(np.sum(lightMatrix))
    print(lightMatrix)
    for row in lm:
        s1 += sum(row)
    print(s1)

# if __name__ == '__main__':
#     lightMatrix = np.zeros((1000,1000),dtype=int)
#     lm = [[0 for i in range(1000)] for j in range(1000)]
#     s1 = 0
#     with open("data6p1.txt") as f:
#         for line in f:
#             getInstructions(line,lightMatrix)
#             getInstructions(line,lm)
#     lightMatrix[lightMatrix < 0] = 0
#     print(np.sum(lightMatrix))
#     print(lightMatrix)
#     for row in lm:
#         s1 += sum(row)
        
    # print(s1)


