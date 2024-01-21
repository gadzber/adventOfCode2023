import numpy as np

def main():
    f = open("day09/data.input", "r")
    Lines = f.readlines()

    out = 0

    for line in Lines:
        line = line.split(" ")

        values = []
        for element in line:
            values.append(int(element))

        values = np.array(values)

        table = []
        table.append(values)

        while np.any(table[-1]):
            values = table[-1]
            diff = np.diff(values)
            table.append(diff)
        
        for values in table:
            out = out + values[-1]
    
    print(out)


if __name__ == '__main__':
    main()