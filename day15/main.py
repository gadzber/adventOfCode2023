def hash(input):
    output = 0
    for c in input:
        output += ord(c)
        output = (output * 17) % 256
    return output

def main():
    f = open("day15/data.input", "r")
    text = f.read()
    text = text.replace("\n","")

    steps = text.split(',')

    output = 0
    for step in steps:
        output+=hash(step)

    print(output)

if __name__ == '__main__':
    main()