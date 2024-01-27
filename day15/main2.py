def hash(input):
    output = 0
    for c in input:
        output += ord(c)
        output = (output * 17) % 256
    return output

class Lens():
    def __init__(self,name,focalLength):
        self.name = name
        self.focalLength = focalLength

class Box():
    def __init__(self) -> None:
        self.Lenses = []
        pass

    def append(self, name, focalLength):
        for i,lens in enumerate(self.Lenses):
            if lens.name == name:
                self.Lenses[i].focalLength = focalLength
                return
            
        self.Lenses.append(Lens(name, focalLength))
    
    def erase(self, name):
        for i, lens in enumerate(self.Lenses):
            if lens.name == name:
                del self.Lenses[i]
                break
    
def main():
    f = open("day15/data.input", "r")
    text = f.read()
    text = text.replace("\n","")

    steps = text.split(',')

    boxes = [ Box() for _ in range(256) ]
    
    output = 0
    for step in steps:
        
        if step[-1] == '-':
            name = step[:-1]
            id = hash(name)
            boxes[id].erase(name)
        
        else:
            name = step[:-2]
            focalLength = int(step[-1])
            id = hash(name)
            boxes[id].append(name, focalLength) 

    output = 0

    for boxNum,box in enumerate(boxes):
        for lensNum,lens in enumerate(box.Lenses):
            output += (1+boxNum) * (1+lensNum) * lens.focalLength
    
    print(output)

if __name__ == '__main__':
    main()