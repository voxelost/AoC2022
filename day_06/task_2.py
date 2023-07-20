with open("day_06/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())

BUF_SIZE = 14
for line in input_:
    buf = []
    for i in range(len(line) - BUF_SIZE-1):
        buf = line[i:i+BUF_SIZE]
        if all(buf.count(char) == 1 for char in buf):
            print(i+BUF_SIZE)
            break
