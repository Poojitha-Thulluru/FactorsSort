def get_sorted_array(nums_array: list) -> list:
    nums_array.sort(key=lambda num: (count_factors(num), num))
    return nums_array


def count_factors(num: int) -> int:
    factors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors += 2 if num // i != i else 1
    return factors


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The factors sorted array is : ", get_sorted_array(num_array))
except ValueError:
    print("Invalid Input, Please enter only integer")
