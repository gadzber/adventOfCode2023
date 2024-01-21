import numpy as np
def main():
    f = open("day11/data.input", "r")
    Lines = f.read().splitlines()

    sizeX = len(Lines[0])
    sizeY = len(Lines)

    galaxyMap = np.empty([sizeY, sizeX],dtype=np.str_)
    galaxies = []

    expansionRate=1000000

    # convert map
    for x in range(sizeX):
        for y in range(sizeY):
            galaxyMap[y,x] = Lines[y][x]


    emptyRows = []
    emptyCols = []

    # find empty rows and columns
    for i in range(sizeY):
        if np.all( galaxyMap[i, :] == '.' ):
           emptyRows.append(i)
    
    for i in range(sizeX):
        if np.all( galaxyMap[:, i] == '.' ):
           emptyCols.append(i)

    x_exp = 0
    y_exp = 0

    # Create list of galaxies in expanded universe
    for x in range(sizeX):
        y_exp = 0
        if x in emptyCols:
            x_exp += (expansionRate-1)
        
        else:
            for y in range(sizeY):
                if y in emptyRows:
                    y_exp += (expansionRate-1)
                else:
                    if galaxyMap[y,x] == '#':
                        galaxies.append(np.array([x+x_exp,y+y_exp], dtype=np.int64))

    shortestDist = []
    
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            dist = galaxies[j] - galaxies[i]
            dist = np.abs(dist[0]) + np.abs(dist[1])
            
            shortestDist.append(dist)


    print(sum(shortestDist))


if __name__ == '__main__':
    main()