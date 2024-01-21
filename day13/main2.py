import numpy as np

def main():
    f = open("day13/data.input", "r")
    Patterns = f.read().split("\n\n")

    out = 0

    for text in Patterns:
        text = text.splitlines()
        numOfRows = len(text)
        numOfCols = len(text[0])

        pattern = np.empty([numOfRows, numOfCols], dtype=np.str_)

        # convert pattern
        for col in range(numOfCols):
            for row in range(numOfRows):
                pattern[row,col] = text[row][col]

        #rows
        for i in range(1,numOfRows):
            upper = pattern[0:i]
            lower = pattern[i:numOfRows]

            # match dimension
            dim = min([np.size(upper,0), np.size(lower,0)])
            
            upper = np.flipud(upper)
            upper = upper[0:dim,:]
            lower = lower[0:dim,:]

            # upper = upper[::-1]

            if np.count_nonzero(upper != lower) == 1:
                out += 100 * i
                break
        
        del lower
        del upper


        #cols
        for i in range(1,numOfCols):
            left = pattern[:,0:i]
            right = pattern[:,i:numOfCols]

            # match dimension
            dim = min([np.size(left,1), np.size(right,1)])
            
            left = np.fliplr(left)
            left = left[:,0:dim]
            right = right[:,0:dim]

            # upper = upper[::-1]

            if np.count_nonzero(left != right) == 1:
                out += i
                break    

    print(out)

   

if __name__ == '__main__':
    main()