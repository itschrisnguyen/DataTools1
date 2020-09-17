def nth_power(n,power):
    """
    calculate the power for numbers up to n
    """

    return [i**power for i in range(n)]

print(nth_power(10,4))
