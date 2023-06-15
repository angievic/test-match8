import sys


def find_number_pairs(numbers, target_sum):
    complements = {}
    for num in numbers:
        complement = target_sum - num
        if complement in complements:
            print("+", num, ",", complement)
        complements[num] = True


def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(num) for num in file.read().split(',')]
    return numbers


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <file_path> <target_sum>")
        sys.exit(1)

    file_path = sys.argv[1]
    target_sum = int(sys.argv[2])

    numbers = read_numbers_from_file(file_path)
    find_number_pairs(numbers, target_sum)