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

    i = 0
    position = 'AAA'

    length = len(sequence)

    while True:
        num = graph[position]
        direction = sequence[i % length]

        if direction == 'L':
            position = nodes[num][0]

        else:
            position = nodes[num][1]

        i = i+1
        if position == 'ZZZ':
            break


    print(i)


        
        


if __name__ == '__main__':
    main()