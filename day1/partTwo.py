inputFile = open("input.txt")
count = 0
low_index = 0
high_index = 1
numbers = inputFile.readlines()
for i in range(len(numbers) - 3):
    first_sum = int(numbers[low_index]) + int(numbers[low_index + 1]) + int(numbers[low_index + 2])
    second_sum = int(numbers[high_index]) + int(numbers[high_index + 1]) + int(numbers[high_index + 2])
    if second_sum > first_sum:
        count += 1
    low_index += 1
    high_index += 1
return count
