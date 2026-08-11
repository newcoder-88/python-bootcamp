numbers = [10, 45, 23, 67, 12]
def print_numbers(numbers):
    for number in numbers:
        print(number)
print_numbers(numbers)


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print (calculate_sum(numbers))

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest(numbers))