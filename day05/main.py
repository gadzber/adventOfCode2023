class Map:
    def __init__(self):
        self.map = []
        self.inputType = ""
        self.outputType = ""

    def append(self,line):
        self.map.append(line)
    
    def convert(self,input):
        output = input

        for line in self.map:
            destination = line[0]
            source = line[1]
            length = line[2]
            
            if input in range(source,source+length):
                offset = input-source
                output = destination+offset
                return output
            
        return output
    

def main() -> None:
    
    print( 'Loading input...' )
    file = open('day05/data.input', 'r')
    Lines = file.readlines()

    # remove \n
    for i in range(0,len(Lines)):
        Lines[i] = Lines[i].replace("\n","")

    # read seeds
    seeds = []
    for number in Lines[0].split(" "):
        if number.isdigit():
            seeds.append(int(number))

    # load maps
    maps = []
    for i in range(2, len(Lines)):
        line = Lines[i].split(" ")
        
        # map type
        if line[-1] == "map:":
            maps.append(Map())
            types = line[0].split("-")
            maps[-1].inputType = types[0]
            maps[-1].outputType = types[2]
            continue

        # space 
        if line[0] == '':
            continue

        # map values
        map = []
        for element in line:
            map.append(int(element))
        maps[-1].append(map)

    locations = []

    for seed in seeds:
        for map in maps:
            seed = map.convert(seed)
        
        locations.append(seed)
    
        

    print(min(locations))


if __name__ == '__main__':
    main()