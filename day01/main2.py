

def main() -> None:
    
    print( 'Loading input...' )
    file = open('day01/data.input', 'r')
    Lines = file.readlines()

    calibration = 0

    Numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    Digits = ["0","1","2","3","4","5","6","7","8","9"]

    for line in Lines:
        
        # forward search
        Positions = []

        for number in Numbers:
            Positions.append(line.find(number))

        for i in range(len(Positions)):
            if Positions[i] == -1:
                Positions[i] = 9000

        num = Positions.index(min(Positions))

        if num in range(8000):
            line = line.replace(Numbers[num],Digits[num])

        # backward search
        Positions = []
        for number in Numbers:
            Positions.append(line[::-1].find(number[::-1]))

        
        for i in range(len(Positions)):
            if Positions[i] == -1:
                Positions[i] = 9000

        num = Positions.index(min(Positions))

        if num in range(8000):
            number = Numbers[num]
            line = line.replace(number[::-1],Digits[num])


        # calc calibration
        for c in line:
            if c.isdigit():
                calibration = calibration + 10*int(c)
                break


        for c in reversed(line):
            if c.isdigit():
                calibration = calibration + int(c)
                break
    
    print(calibration)

if __name__ == '__main__':
    main()