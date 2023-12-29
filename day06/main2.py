import math

def main():
    f = open("data.input", "r")
    Lines = f.readlines()

    
    line = Lines[0]
    line = line.replace("\n","")
    line = line.split(":")
    line = line[1]
    line = line.replace(" ","")
    Time = int(line)

    line = Lines[1]
    line = line.replace("\n","")
    line = line.split(":")
    line = line[1]
    line = line.replace(" ","")
    Distance = int(line)

    # distance = windupTime * (time - windupTime)
    # distance = -windupTime**2 + windupTime*time
    
    a = -1
    b = Time
    c = -Distance

    delta = b**2 - 4*a*c
    x2 = (-b - math.sqrt(delta)) / (2*a)
    x1 = (-b + math.sqrt(delta)) / (2*a)

    x1 = math.ceil(x1)
    x2 = math.floor(x2)

    out = x2-x1+1
    print(out)






    return

if __name__ == '__main__':
    main()