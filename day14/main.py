import numpy as np

def main():
    f = open("day14/data.input", "r")
    text = f.read().splitlines()

    numOfRows = len(text)
    numOfCols = len(text[0])
    pattern = np.empty([numOfRows, numOfCols], dtype=np.str_)

    # convert pattern
    for col in range(numOfCols):
        for row in range(numOfRows):
            pattern[row,col] = text[row][col]

    out = 0

    cond = True
    while cond:
        cond = False

        for row in range(1,numOfRows):
            for col in range(numOfCols):
                if pattern[row,col] == 'O' and pattern[row-1,col] == '.':
                    pattern[row-1,col] = 'O'
                    pattern[row,col] = '.'
                    cond = True
    
    for row in range(numOfRows):
        for col in range(numOfCols):
            if pattern[row,col] == 'O':
                out += (numOfRows - row)
 
    print(out)

if __name__ == '__main__':
    main()