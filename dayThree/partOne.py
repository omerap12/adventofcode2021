def answer():
    inputFile = open("input.txt")
    gamma_rate = ""
    epsilon_rate = ""
    count_one = 0
    count_zero = 0
    numbers = inputFile.readlines()
    size_of_bit = len(numbers[0])
    for i in range(size_of_bit-1):
        for bit in numbers:
            if bit[i] == "1":
                count_one += 1
            else:
                count_zero += 1
        if count_one > count_zero:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"
            gamma_rate += "0"
        count_zero = 0
        count_one = 0
    decimal_gamma_rate = turnBinaryToDecimal(gamma_rate)
    decimal_epsilon_rate = turnBinaryToDecimal(epsilon_rate)
    return decimal_epsilon_rate * decimal_gamma_rate


def turnBinaryToDecimal(binary_number):
    sum = 0
    length = len(binary_number)
    for i in range(length):
        sum += pow(2, i) * int(binary_number[length-i-1])
    return sum


if __name__ == "__main__":
    print(answer())
