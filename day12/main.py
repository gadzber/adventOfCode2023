import numpy as np

class Line:
    def __init__(self, length, elements):
        self.elements = elements
        self.length = length
        self.distances = []
        self.numOfCombinations = 0

        self.fillDistances(self.length - sum(self.elements), len(self.elements))
        self.fillCombinations()

    def fillDistances(self, distanceSum, numOfElements, currentLine=[]):
        if len(currentLine) == 0:
            currentLine = [0]
            for i in range(0, (distanceSum - numOfElements + 2)):
                currentLine[0] = i
                self.fillDistances(distanceSum, numOfElements, currentLine.copy())

        elif len(currentLine) > 0 and len(currentLine) < numOfElements:
            currentLine.append(0)
            for i in range(1, (distanceSum - sum(currentLine) + 1)):
                currentLine[-1] = i
                self.fillDistances(distanceSum, numOfElements, currentLine.copy())

        else:
            self.distances.append(currentLine.copy())

    def fillLine(self, distances):
        line = []

        for i in range(len(self.elements)):
            line.extend([False] * distances[i])
            line.extend([True] * self.elements[i])

        line.extend([False] * (self.length - len(line)))
        line = np.array(line)

        return line

    def fillCombinations(self):
        self.numOfCombinations = len(self.distances)
        self.combMatrix = np.full((self.numOfCombinations, self.length), False, dtype=bool)

        for i in range(self.numOfCombinations):
            self.combMatrix[i, :] = self.fillLine(self.distances[i])

    def eraseCombinationWhenTrue(self, element):
        linesToErase = []
        for i in range(self.numOfCombinations):
            if self.combMatrix[i, element] == True:
                linesToErase.append(i)

        self.combMatrix = np.delete(self.combMatrix, linesToErase, 0)
        self.numOfCombinations = self.combMatrix.shape[0]

    def eraseCombinationWhenFalse(self, element):
        linesToErase = []
        for i in range(self.numOfCombinations):
            if self.combMatrix[i, element] == False:
                linesToErase.append(i)

        self.combMatrix = np.delete(self.combMatrix, linesToErase, 0)
        self.numOfCombinations = self.combMatrix.shape[0]




def main():
    f = open("day12/data.input", "r")
    Lines = f.read().splitlines()

    out = 0

    for line in Lines:
        line = line.split(" ")
        row = line[0]

        row2 = "."

        for element in row:
            if row2[-1] == '.' and element == '.':
                continue
            else:
                row2 = row2 + element
        
        row = row2[1:]

        # row = row + '?' + row + '?' + row + '?' + row + '?' + row

        if row[0] == '.':
            row = row[1:]
        
        if row[-1] == '.':
            row = row[:-1]
        

        numbers = line[1].split(",")

        #magic xD        
        numbers = [int(num) for num in numbers]

        # numbers = numbers + numbers + numbers + numbers + numbers

        comb = Line(len(row), numbers)
        print(comb.numOfCombinations)

        for i, element in enumerate(row):
            if element == '?':
                continue

            if element == '#':
                comb.eraseCombinationWhenFalse(i)
                continue
            
            if element == '.':
                comb.eraseCombinationWhenTrue(i)
                continue
        
        out += comb.numOfCombinations

    print("result:")
    print(out)
    


if __name__ == '__main__':
    main()