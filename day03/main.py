import re

class Part:
    def __init__(self,xPos, yPos, char):
        self.xPos = xPos
        self.yPos = yPos
        self.char = char
        self.adj = 0
        self.gearRatio = 1

class Number:
    def __init__(self,xPos, yPos, lenght, value):
        self.xPos = xPos
        self.yPos = yPos
        self.lenght = lenght
        self.value = value

def isAdjacent(part, number):
    if (part.yPos - number.yPos) in [-1,0,1]:
        if(part.xPos - number.xPos) in range(-1,number.lenght+1):
            if part.char == '*':
                part.gearRatio = part.gearRatio * number.value
                part.adj = part.adj+1
            
            return True
    return False

    



def main() -> None:
    
    print( 'Loading input...' )
    file = open('day03/data.input', 'r')
    Lines = file.readlines()

    for line in Lines:
        line = line.replace("\n","")

    # numbers
    Numbers = []

    for y in range(len(Lines)):
        results = re.finditer(r'\d+', Lines[y])
        
        for res in results:
            xPos = res.start()
            yPos = y
            lenght = res.end()-res.start()
            value = int(res.group())

            Numbers.append(Number(xPos,yPos,lenght,value))
    
    # parts
    Parts = []
    for y in range(len(Lines)):
        line = Lines[y]
        line = line.replace("\n","")

        for x in range(len(line)):
            c = line[x]
            if c.isdigit() or c == '.':
                continue
            else:
                Parts.append(Part(x,y,c))
    

    sum = 0

    for part in Parts:
        for number in Numbers:
           if isAdjacent(part, number):
               sum = sum + number.value

    ratio = 0
    for part in Parts:
        if part.char == '*' and part.adj == 2:
            ratio = ratio + part.gearRatio
    
    print(sum)
    print(ratio)

    



if __name__ == '__main__':
    main()