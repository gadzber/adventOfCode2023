import numpy as np

def main():
    f = open("data.input", "r")
    text = f.read().splitlines()

    numOfRows = len(text)
    numOfCols = len(text[0])
    pattern = np.empty([numOfRows, numOfCols], dtype=np.str_)

    # convert pattern
    for col in range(numOfCols):
        for row in range(numOfRows):
            pattern[row,col] = text[row][col]

    out = 0
    outPrev = 0

    prevPattern = pattern.copy()

    for i in range(1000000000):
        
        # North
        cond = True
        while cond:
            cond = False

            for row in range(1,numOfRows):
                for col in range(numOfCols):
                    if pattern[row,col] == 'O' and pattern[row-1,col] == '.':
                        pattern[row-1,col] = 'O'
                        pattern[row,col] = '.'
                        cond = True

        # West
        cond = True
        while cond:
            cond = False

            for row in range(numOfRows):
                for col in range(1,numOfCols):
                    if pattern[row,col] == 'O' and pattern[row,col-1] == '.':
                        pattern[row,col-1] = 'O'
                        pattern[row,col] = '.'
                        cond = True           

        # South
        cond = True
        while cond:
            cond = False

            for row in range(numOfRows-1):
                for col in range(numOfCols):
                    if pattern[row,col] == 'O' and pattern[row+1,col] == '.':
                        pattern[row+1,col] = 'O'
                        pattern[row,col] = '.'
                        cond = True 

        # East
        cond = True
        while cond:
            cond = False

            for row in range(numOfRows):
                for col in range(numOfCols-1):
                    if pattern[row,col] == 'O' and pattern[row,col+1] == '.':
                        pattern[row,col+1] = 'O'
                        pattern[row,col] = '.'
                        cond = True

        out = 0
        # Calc Load
        for row in range(numOfRows):
            for col in range(numOfCols):
                if pattern[row,col] == 'O':
                    out += (numOfRows - row)

        
        print(str(i) + " " + str(out))

        # Check for updates
        if np.all( prevPattern == pattern ):
            break

        prevPattern = pattern.copy()




    for row in range(numOfRows):
        for col in range(numOfCols):
            if pattern[row,col] == 'O':
                out += (numOfRows - row)
 
    print(out)

if __name__ == '__main__':
    main()