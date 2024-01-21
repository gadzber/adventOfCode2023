def main():
    f = open("day08/data.input", "r")
    Lines = f.readlines()

    sequence = Lines[0].replace("\n","")
    sequence = [*sequence]
    Lines = Lines[2:]

    dictList = []
    nodes = []

    for line in Lines:
        tmp = line.split(" ")
        
        dictList.append(tmp[0])

        tmp[2] = tmp[2].replace("(","")
        tmp[2] = tmp[2].replace(",","")

        tmp[3] = tmp[3].replace(")","")
        tmp[3] = tmp[3].replace("\n","")
        
        nodes.append([tmp[2], tmp[3]])
    
    numbers = list(range(0,len(dictList)))

    graph = zip(dictList, numbers)
    graph = dict(graph)

    
    position = []

    for pos in dictList:
        if pos[-1] == 'A':
            position.append(pos)
    


    length = len(sequence)

    iter = 0
    cond = True
    while cond:
        cond = False
        direction = sequence[iter % length]

        for i, pos in enumerate(position):
            num = graph[pos]
            
            if direction == 'L':
                position[i] = nodes[num][0]

            else:
                position[i] = nodes[num][1]
        


        iter = iter+1
        
        for pos in position:
            if pos[-1] != 'Z':
                cond = True
                break
                


    print(iter)


        
        


if __name__ == '__main__':
    main()