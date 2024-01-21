import re


def main() -> None:
    
    print( 'Loading input...' )
    file = open('day04/data.input', 'r')
    Lines = file.readlines()


    Instances = [1] * len(Lines)

    

    for line, card in zip(Lines,range(len(Lines))):
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
        
        end = [card+1+score, len(Lines)]
        end = min(end)

        for i in range(card+1,end):
            Instances[i]  = Instances[i] + Instances[card]
        

    output = sum(Instances)
    print(output)
    
    
    



if __name__ == '__main__':
    main()