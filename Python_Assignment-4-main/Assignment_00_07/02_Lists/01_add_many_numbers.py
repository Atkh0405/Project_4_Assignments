def sum_of_numbers(numbers):

    total = 0
    for num in numbers:
        total += num
    return total

def sum():
    number_list = [10,20,30,40]
    total_num = sum_of_numbers(number_list)
    print("List:", number_list)
    print(f"total number= {total_num}")

sum()    