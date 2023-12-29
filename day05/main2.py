class Map:
    def __init__(self):
        self.inputRangeStarts = []
        self.outputRangeStops = []
        self.rangeLengths = []
        self.inputType = ""
        self.outputType = ""

    def append(self,inputRangeStart,outputRangeStop,rangeLength ):
        self.inputRangeStarts.append(inputRangeStart)
        self.outputRangeStops.append(outputRangeStop)
        self.rangeLengths.append(rangeLength)


    
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

class Layer:
    def __init__(self):
        self.name = ""
        self.rangeStarts = []
        self.rangeLengths = []
        self.ranges = []
    
    def append(self, start, length)
        self.rangeStarts.append(start)
        self.rangeLengths.append(length)

    def calcRanges(self)
        for i in range(len(self.rangeStarts)):
            self.ranges.append(range(self.rangeStarts[i],self.rangeStarts[i]+self.rangeLengths[i]))
    

def main() -> None:
    
    print( 'Loading input2...' )
    file = open('day05\data.input', 'r')
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
        map.append(int(line[0]), int(line[1]), int(line(2)))

        maps[-1].append(map)

    # load seed ranges
    layers = []
    layers.append(Layer())
    
    for i in range(0,len(seeds),2):
        layers[0].append(seeds[0],seeds[1])
    

    # iterate maps
    for iterMap in len(maps):



    

    
    


if __name__ == '__main__':
    main()