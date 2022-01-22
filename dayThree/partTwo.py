def answer():
    inputFile = open("input.txt")
    numbers = inputFile.readlines()
    oxygen = find_oxygen(numbers)
    CO2 = find_CO2(numbers)
    return turnBinaryToDecimal(oxygen)*turnBinaryToDecimal(CO2)



def find_oxygen(numbers):
    count_zero = 0
    count_one = 0
    oxygen = numbers.copy()
    most_common_bit = ""
    index = 0
    while len(oxygen) > 1:
        for bit in oxygen:
            if bit[index] == "1":
                count_one += 1
            else:
                count_zero += 1
        if count_one >= count_zero:
            most_common_bit = "1"
        else:
            most_common_bit = "0"

        temp = []
        for i in range(len(oxygen)):
            if oxygen[i][index] != most_common_bit:
                continue
            temp.append(oxygen[i])
        oxygen = temp.copy()
        temp.clear()
        count_zero = 0
        count_one = 0
        index += 1
    return oxygen[0]

def find_CO2(numbers):
    count_zero = 0
    count_one = 0
    CO2 = numbers.copy()
    least_common_bit = ""
    index = 0
    while len(CO2) > 1:
        for bit in CO2:
            if bit[index] == "1":
                count_one += 1
            else:
                count_zero += 1
        if count_one < count_zero:
            least_common_bit = "1"
        else:
            least_common_bit = "0"

        temp = []
        for i in range(len(CO2)):
            if CO2[i][index] != least_common_bit:
                continue
            temp.append(CO2[i])
        CO2 = temp.copy()
        temp.clear()
        count_zero = 0
        count_one = 0
        index += 1
    return CO2[0]



def turnBinaryToDecimal(binary_number):
    sum = 0
    length = len(binary_number)-1
    for i in range(length):
        sum += pow(2, i) * int(binary_number[length - i - 1])
    return sum


if __name__ == "__main__":
    print(answer())
