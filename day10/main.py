import numpy as np

def whereToMove(pipeMap, x, y, income):
    char = pipeMap[x,y]

    key = income + char

    dictKeys = ["N|","NL","NJ","E-","EL","EF","S|","SF","S7","W-","W7","WJ"]
    dictValues=['S' ,'E' ,'W' ,'W' ,'N' ,'S' ,'N' ,'E' ,'W' ,'E' ,'S' ,'N' ]

    dictionary = zip(dictKeys, dictValues)
    dictionary = dict(dictionary)
    
    return dictionary[key]

def isInLoop(point,loop):
    px = point[0]
    py = point[1]
    
    left = 0
    right = 0

    for i, loopPoint in enumerate(loop):
        lx = loopPoint[0]
        ly = loopPoint[1]

        if ly == py:                        # w jednej poziomej linii
            if ly == loop[i-1][1] or ly == loop[i+1][1]:     # odcinek styczny
                continue
            
            if lx > px:
                right+=1

            else:
                left+=1
    
    if left%2==1 and right%2==1:
        return True
    else:
        return False

        

def main():
    f = open("day10/data.input", "r")
    Lines = f.read().splitlines()

    sizeX = len(Lines[0])
    sizeY = len(Lines)

    pipeMap = np.empty([sizeX, sizeY],dtype=np.str_)

    dots = []
    loop = []

    # convert map
    for x in range(sizeX):
        for y in range(sizeY):
            pipeMap[x,y] = Lines[y][x]

            if Lines[y][x] == '.':
                dots.append(np.array([x,y]))


    #find start pos
    for i,line in enumerate(Lines):
        pos = line.find('S')
        if pos != -1:
            startPosX = pos
            startPosY = i
            break
            
    startPos = np.array([startPosX, startPosY])
    currentPos = np.array([startPosX, startPosY])

    # 1st move:
    if pipeMap[startPosX+1, startPosY] in ['7','J','-']:
        currentPos = np.array([startPosX+1, startPosY])
        income = 'W'
    
    if pipeMap[startPosX-1, startPosY] in ['F','L','-']:
        currentPos = np.array([startPosX-1, startPosY])
        income = 'E'

    if pipeMap[startPosX, startPosY+1] in ['L','J','|']:
        currentPos = np.array([startPosX, startPosY+1])
        income = 'N'

    if pipeMap[startPosX, startPosY-1] in ['7','F','|']:
        currentPos = np.array([startPosX, startPosY+1])
        income = 'S'

    edgeX = []
    edgeY = []
    edgeX.append(startPos[0])
    edgeY.append(startPos[1])
    
    moves = 1       
    
    while np.array_equal(startPos, currentPos) == False:
        x = currentPos[0]
        y = currentPos[1]
        loop.append(currentPos.copy())
        
        direction = whereToMove(pipeMap, x, y, income)

        match direction:
            case 'N':
                currentPos += np.array([0,-1])
                income = 'S'
            case 'E':
                currentPos += np.array([1,0])
                income = 'W'
            case 'S':
                currentPos += np.array([0,1])
                income = 'N'
            case 'W':
                currentPos += np.array([-1,0])
                income = 'E'
        moves+=1    
    
    numOfDots = 0
    for dot in dots:
        if isInLoop(dot, loop):
            numOfDots+=1

    print(moves/2)
    print(numOfDots)
           
        


if __name__ == '__main__':
    main()