import re


def main() -> None:
    
    print( 'Loading input...' )
    file = open('day04/data.input', 'r')
    Lines = file.readlines()

    sum = 0

    for line in Lines:
        line = line.replace("\n","")

        line = line.split(":")
        line = line[1]

        line = line.split("|")
        
        winningNumbers = []
        userNumbers = []

        for num in line[0].split(" "):
            if num == "":
                continue
            winningNumbers.append(int(num))

        for num in line[1].split(" "):
            if num == "":
                continue
            userNumbers.append(int(num))

        score = 0

        for num in userNumbers:
            if num in winningNumbers:
                score = score + 1
        
        if score >0:
            sum = sum + 2**(score-1)
        

    print(sum)
    
    
    



if __name__ == '__main__':
    main()