def main():
    f = open("data.input", "r")
    Lines = f.readlines()

    Times = []
    Distances = []
    Races = []

    line = Lines[0]
    line = line.replace("\n","")
    line = line.split(" ")

    for element in line:
        if element.isdigit():
            Times.append(int(element))
    
    line = Lines[1]
    line = line.replace("\n","")
    line = line.split(" ")

    for element in line:
        if element.isdigit():
            Distances.append(int(element))

    for time, distance in zip(Times, Distances):
        ways = 0

        for windupTime in range(1,time):
            dist = windupTime * (time - windupTime)
            if dist > distance:
                ways = ways+1
        
        Races.append(ways)
    
    out = 1
    for element in Races:
        out = out * element
    
    print(out)




    return

if __name__ == '__main__':
    main()