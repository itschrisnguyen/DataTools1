def nth_power(n,power=2):
    """
    calculate the power for numbers up to n
    args:
        n: highest number of list of numbers
        power: power for number to raise, for default is 2
    """

    return [i**power for i in range(n)]

print(nth_power(10))
