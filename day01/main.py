def main() -> None:
    
    print( 'Loading input...' )
    file = open('day01\input.txt', 'r')
    Lines = file.readlines()

    calibration = 0

    for line in Lines:
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