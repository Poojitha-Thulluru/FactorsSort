def get_sorted_factors(nums_array: list) -> list:
    factors_counts = [(num, count_factors(num)) for num in nums_array]
    factors_counts.sort(key=lambda x: (x[1], x[0]))
    result = [num for num, _ in factors_counts]
    return result


def count_factors(num: int) -> int:
    factors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors += 2 if num // i != i else 1
    return factors


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The factors sorted array is : ", get_sorted_factors(num_array))
except ValueError:
    print("Invalid Input, Please enter only integer")
