def answer():
    inputFile = open("input.txt")
    horizontal_position = 0
    depth = 0
    commands = inputFile.readlines()
    for line in commands:
        command = line.split(" ")
        if command[0] == "forward":
            horizontal_position += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    return horizontal_position * depth


if __name__ == "__main__":
    print(answer())
