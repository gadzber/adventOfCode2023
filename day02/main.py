def main() -> None:
    
    print( 'Loading input...' )
    file = open('day02/data.input', 'r')
    Lines = file.readlines()

    limit_red = 12
    limit_green = 13
    limit_blue = 14
    
    sum = 0
    sum2 = 0

    for line in Lines:
        line = line.replace("\n","")
        line = line.replace(";",":")
        line = line.split(":")

        ID = [int(s) for s in line[0].split() if s.isdigit()][0]
        max_red = 0
        max_green = 0
        max_blue = 0

        possible = True
        for i in range(1,len(line)):
            pick = line[i]
            pick = pick.replace(",","")
            pick = pick.split()

            while pick:
                
                num = int(pick[0])

                if pick[1] == 'red':
                    max_red = max([max_red, num])
                    
                    if num > limit_red:
                            possible = False
                            
                
                if pick[1] == 'green':
                    max_green = max([max_green, num])
                    if num > limit_green:
                            possible = False
                            

                if pick[1] == 'blue':
                    max_blue = max([max_blue, num])
                    if num > limit_blue:
                            possible = False
                            

                del pick[:2]
        
        sum2 = sum2 + max_red * max_green * max_blue

        if possible:
            sum = sum + ID
    
    print(sum)
    print(sum2)



                
            


        

        
    


if __name__ == '__main__':
    main()