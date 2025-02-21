def sum_of_evens(numbers):
    sum = 0

    for num in numbers:
        if num % 2 == 0:
            sum = num

    return sum


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_evens(list)
print(result)
